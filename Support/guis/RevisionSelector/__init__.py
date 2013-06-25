#!/usr/bin/env python
#-*- encoding: utf-8 -*-
from operator import itemgetter

from PyQt4 import QtGui, QtCore
from prymatex.core import PMXBaseDialog

from RevisionSelector.ui_selector import Ui_RevisionSelectorDialog

class RevisionModel(QtGui.QStandardItemModel):
    ROWS = (
            ('rev', 'Revision'),
            ('author', 'Author'),
            ('date', 'Date'),
            ('msg', 'Log'),
            )
    def __init__(self, parent = None):
        QtGui.QStandardItemModel.__init__(self, 0,len(self.ROWS))
        for n, (name, title) in enumerate(self.ROWS):
            self.setHeaderData(n, QtCore.Qt.Horizontal, title,)

class RevisionSelectorDialog(QtGui.QDialog, Ui_RevisionSelectorDialog, PMXBaseDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        PMXBaseDialog.__init__(self)
        self.setupUi(self)
        self.model = RevisionModel(self)
        self.tableViewRevision.setModel(self.model)
        self.tableViewRevision.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableViewRevision.verticalHeader().hide()
        
    def setParameters(self, parameters):
        if 'title' in parameters:
            self.setWindowTitle(parameters["title"])
        if 'entries' in parameters:
            self.updateEntries(parameters["entries"])
        
    def updateEntries(self, entries):
        item_names = map(itemgetter(0), self.model.ROWS)
        self.model.removeRows(0, self.model.rowCount())
        for entry in entries:
            row = map(lambda name: QtGui.QStandardItem(unicode(entry.get(name, ''))), item_names)
            self.model.appendRow(row)
        self.tableViewRevision.resizeColumnsToContents()
        self.tableViewRevision.resizeRowsToContents()
        
dialogClass = RevisionSelectorDialog