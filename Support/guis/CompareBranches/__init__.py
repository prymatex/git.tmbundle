#!/usr/bin/env python
#-*- encoding: utf-8 -*-
from operator import itemgetter

from PyQt4 import QtGui, QtCore
from prymatex.core import PMXBaseDialog

from CompareBranches.ui_compare import Ui_CompareBranchesDialog

class CompareBranchesDialog(QtGui.QDialog, Ui_CompareBranchesDialog, PMXBaseDialog):
    
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        PMXBaseDialog.__init__(self)
        self.__callback = None
        self.setupUi(self)
        
    def setParameters(self, parameters):
        if 'title' in parameters:
            self.setWindowTitle(parameters["title"])
        if 'branches' in parameters:
            for branch in parameters["branches"]:
                self.listWidgetOptions.addItem(QtGui.QListWidgetItem(branch["name"]))
    
    def allSelectedBranches(self):
        branches = []
        for index in xrange(self.listWidgetSelected.count()):
            branches.append(self.listWidgetSelected.item(index).data(QtCore.Qt.DisplayRole))
        return branches
    
    def allOptionsBranches(self):
        branches = []
        for index in xrange(self.listWidgetOptions.count()):
            branches.append(self.listWidgetOptions.item(index).data(QtCore.Qt.DisplayRole))
        return branches
    
    def waitForInput(self, callback):
        self.__callback = callback
        
    def on_pushButtonOk_pressed(self):
        selected = map(lambda b: {"name": b}, self.allSelectedBranches())
        options = map(lambda b: {"name": b}, self.allOptionsBranches())
        if self.__callback is not None:
            self.__callback({"returnArgument": options, "currentBranch": selected})
            self.__callback = None

    def on_pushButtonCancel_pressed(self):
        print self.allSelectedBranches()
        if self.__callback is not None:
            self.__callback({})
            self.__callback = None

dialogClass = CompareBranchesDialog