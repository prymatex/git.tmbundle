require ENV['TM_SUPPORT_PATH'] + '/lib/ui.rb'
require File.dirname(__FILE__) + "/../stream_progress_methods.rb"

class SCM::Git::Fetch < SCM::Git
  include StreamProgressMethods
  FETCH_ALL = "...fetch all remotes..."
  def initialize
    chdir_base
  end
  
  def run
    c_branch = current_branch
    branch_remote_config_key = "branch.#{c_branch}.remote"
    branch_remote_merge_key = "branch.#{c_branch}.merge"
    branch_default_source = self[branch_remote_config_key]
    branch_default_merge = self[branch_remote_merge_key]
    sources_with_default = sources
    sources_with_default = ([branch_default_source] + sources_with_default).uniq if branch_default_source
    TextMate::UI.request_item(:title => "Fetch", :prompt => "Fetch from which shared repository?", :items => sources_with_default + [FETCH_ALL]) do |selected_source|
      ((selected_source == FETCH_ALL) ? sources_with_default : [source]).each do |source|
        puts "<h2>Fetching from #{source}</h2>"
        flush
        puts htmlize(fetch(source))
        puts "<p>Done.</p>"
      end
      flush
    end
  end
  
  def fetch(source)
    command("fetch", source)
  end
  
  def process_fetch(stream, callbacks = {})
  end
end