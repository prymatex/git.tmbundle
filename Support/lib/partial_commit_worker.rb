# encoding: utf-8

require ENV['TM_SUPPORT_PATH'] + '/lib/ui.rb'
CWNib = ENV['TM_SCM_COMMIT_WINDOW']

module PartialCommitWorker
  class NotOnBranchException < Exception; end
  class NothingToCommitException < Exception; end
  class NothingToAmendException < Exception; end
  class CommitCanceledException < Exception; end
  
  def self.factory(_type, *args)
    klass = (_type == "amend" ? PartialCommitWorker::Amend : PartialCommitWorker::Normal)
    klass.new(*args)
  end
  
  class Base
    attr_reader :git
    
    def initialize(git)
      @git = git
      @base = git.path
    end
  
    def ok_to_proceed_with_partial_commit?
      git.rebase_in_progress? || (! git.branch.current_name.nil?) || git.initial_commit_pending?
    end
    
    def target_paths
      @target_paths ||= git.paths
    end
    
    def split_file_statuses
      [file_candidates.map{ |fc| fc[0] }, file_candidates.map{ |fc| fc[1] }]
    end
    
    def status_helper_tool
      ENV['TM_BUNDLE_SUPPORT'] + '/gateway/commit_dialog_helper.rb'
    end
    
    def tm_scm_commit_window
      files, statuses = split_file_statuses

      res = ""
      res << "cd \"#{git.path}\" && \"$TM_SCM_COMMIT_WINDOW\""
      res << " --log #{Shellwords.escape(git.log(:limit => 1).first[:msg])}" if amend?
      res << " --diff-cmd '#{git.git},diff,HEAD,--'"
      res << " --action-cmd 'M,D:${TM_DISPLAYNAME:?Revert “${TM_DISPLAYNAME}”:Revert},#{status_helper_tool},revert'"
      res << " --action-cmd '?:${TM_DISPLAYNAME:?Delete “${TM_DISPLAYNAME}”:Delete},#{status_helper_tool},delete'"
      res << " --status #{statuses.join(':')}" if !amend? || (amend? && !file_candidates.empty?)
      res << " #{files.map{ |f| e_sh(f) }.join(' ')} 2>/dev/console"

      res
    end

    def exec_commit_dialog
      files, statuses = split_file_statuses
      
      params = {
            'title' => "Commit", 
            'base-path' => git.path,
            'diff-cmd' => git.git + ',diff', 
            'action-cmd' => [ "M,D:Revert," + status_helper_tool + ",revert", "?:Delete," + status_helper_tool + ",delete" ],
            'status' => statuses.join(':'),
            'files' => files.map{ |f| e_sh(f) }.join(' ')
            }
    
      res = %x{#{TM_DIALOG} -cmp #{e_sh params.to_plist} #{e_sh(CWNib)}}
      canceled = ($? != 0)
      
      res = OSX::PropertyList::load(res)
      res = res['result']
      
      res   = Shellwords.shellwords(res)
      canceled = res[0] == 'cancel'
      msg = res[1]
      files = res[2..-1]
      return canceled, msg, files
    end
    
    def show_commit_dialog
      canceled, msg, files = exec_commit_dialog
      raise CommitCanceledException if canceled
      [msg, files]
    end
    
    def file_candidates
      @file_candidates ||=
        git.status(target_paths).map do |e|
          [shorten(e[:path], @base), e[:status][:short]]
        end
    end
    
    def run
      raise NotOnBranchException unless ok_to_proceed_with_partial_commit?
      raise NothingToCommitException if nothing_to_commit?

      if amend?
        raise NothingToAmendException if nothing_to_amend?
      end

      msg, files = show_commit_dialog
      git.auto_add_rm(files)
      res = git.commit(msg, files, :amend => amend?)
      { :files => files, :message => msg, :result => res}
    end
    
    def title
      "#{title_prefix} in #{target_paths.map { |e| htmlize("‘" + shorten(e, ENV['TM_PROJECT_DIRECTORY'] || @base) + "’") } * ', '} on branch ‘#{htmlize(git.branch.current_name)}’"
    end
    
    def nothing_to_commit?
      amend? ? false : file_candidates.empty?
    end

    def nothing_to_amend?
      git.initial_commit_pending?
    end
  end
  
  class Normal < Base
    def title_prefix
      "Committing Files"
    end

    def amend?
      false
    end
  end
  
  class Amend < Base

    def title_prefix
      "Amending the commit"
    end

    def amend?
      true
    end
    
    def show_commit_dialog(*args)
      msg, files = super(*args)
      [msg, files]
    end
    
    def file_candidates
      return @file_candidates if @file_candidates
      super
      @file_candidates
    end
  end
end
