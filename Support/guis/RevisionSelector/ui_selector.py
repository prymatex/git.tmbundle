# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selector.ui'
#
# Created: Mon Aug 27 23:17:12 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_RevisionSelectorDialog(object):
    def setupUi(self, RevisionSelectorDialog):
        RevisionSelectorDialog.setObjectName(_fromUtf8("RevisionSelectorDialog"))
        RevisionSelectorDialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(RevisionSelectorDialog)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableViewRevision = QtGui.QTableView(RevisionSelectorDialog)
        self.tableViewRevision.setObjectName(_fromUtf8("tableViewRevision"))
        self.verticalLayout.addWidget(self.tableViewRevision)
        self.plainTextEdit = QtGui.QPlainTextEdit(RevisionSelectorDialog)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.buttonBox = QtGui.QDialogButtonBox(RevisionSelectorDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(RevisionSelectorDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), RevisionSelectorDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), RevisionSelectorDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(RevisionSelectorDialog)

    def retranslateUi(self, RevisionSelectorDialog):
        RevisionSelectorDialog.setWindowTitle(QtGui.QApplication.translate("RevisionSelectorDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))

