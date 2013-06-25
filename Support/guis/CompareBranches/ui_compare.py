# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compare.ui'
#
# Created: Sun Oct 14 19:00:17 2012
#      by: PyQt4 UI code generator snapshot-4.9.6-95094339d25b
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CompareBranchesDialog(object):
    def setupUi(self, CompareBranchesDialog):
        CompareBranchesDialog.setObjectName(_fromUtf8("CompareBranchesDialog"))
        CompareBranchesDialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(CompareBranchesDialog)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.listWidgetOptions = QtGui.QListWidget(CompareBranchesDialog)
        self.listWidgetOptions.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.listWidgetOptions.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listWidgetOptions.setAlternatingRowColors(True)
        self.listWidgetOptions.setObjectName(_fromUtf8("listWidgetOptions"))
        self.horizontalLayout.addWidget(self.listWidgetOptions)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.toolButtonAdd = QtGui.QToolButton(CompareBranchesDialog)
        self.toolButtonAdd.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("arrow-right"))
        self.toolButtonAdd.setIcon(icon)
        self.toolButtonAdd.setAutoRaise(True)
        self.toolButtonAdd.setObjectName(_fromUtf8("toolButtonAdd"))
        self.verticalLayout_2.addWidget(self.toolButtonAdd)
        self.toolButtonRemove = QtGui.QToolButton(CompareBranchesDialog)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("arrow-left"))
        self.toolButtonRemove.setIcon(icon)
        self.toolButtonRemove.setAutoRaise(True)
        self.toolButtonRemove.setObjectName(_fromUtf8("toolButtonRemove"))
        self.verticalLayout_2.addWidget(self.toolButtonRemove)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.listWidgetSelected = QtGui.QListWidget(CompareBranchesDialog)
        self.listWidgetSelected.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.listWidgetSelected.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listWidgetSelected.setAlternatingRowColors(True)
        self.listWidgetSelected.setObjectName(_fromUtf8("listWidgetSelected"))
        self.horizontalLayout.addWidget(self.listWidgetSelected)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pushButtonOk = QtGui.QPushButton(CompareBranchesDialog)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("dialog-ok"))
        self.pushButtonOk.setIcon(icon)
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.horizontalLayout_2.addWidget(self.pushButtonOk)
        self.pushButtonCancel = QtGui.QPushButton(CompareBranchesDialog)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("dialog-cancel"))
        self.pushButtonCancel.setIcon(icon)
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.horizontalLayout_2.addWidget(self.pushButtonCancel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(CompareBranchesDialog)
        QtCore.QMetaObject.connectSlotsByName(CompareBranchesDialog)

    def retranslateUi(self, CompareBranchesDialog):
        CompareBranchesDialog.setWindowTitle(QtGui.QApplication.translate("CompareBranchesDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonRemove.setText(QtGui.QApplication.translate("CompareBranchesDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonOk.setText(QtGui.QApplication.translate("CompareBranchesDialog", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancel.setText(QtGui.QApplication.translate("CompareBranchesDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

