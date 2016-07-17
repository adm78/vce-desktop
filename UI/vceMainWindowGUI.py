# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vceMainWindowGUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_vceMainWindow(object):
    def setupUi(self, vceMainWindow):
        vceMainWindow.setObjectName(_fromUtf8("vceMainWindow"))
        vceMainWindow.resize(1096, 753)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(vceMainWindow.sizePolicy().hasHeightForWidth())
        vceMainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/vcelogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        vceMainWindow.setWindowIcon(icon)
        self.vcecentralwidget = QtGui.QWidget(vceMainWindow)
        self.vcecentralwidget.setObjectName(_fromUtf8("vcecentralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.vcecentralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.vcehorizontalLayout = QtGui.QHBoxLayout()
        self.vcehorizontalLayout.setObjectName(_fromUtf8("vcehorizontalLayout"))
        self.vcelineEdit = QtGui.QLineEdit(self.vcecentralwidget)
        self.vcelineEdit.setObjectName(_fromUtf8("vcelineEdit"))
        self.vcehorizontalLayout.addWidget(self.vcelineEdit)
        self.vcepushButton = QtGui.QPushButton(self.vcecentralwidget)
        self.vcepushButton.setObjectName(_fromUtf8("vcepushButton"))
        self.vcehorizontalLayout.addWidget(self.vcepushButton)
        self.verticalLayout.addLayout(self.vcehorizontalLayout)
        self.vce = vceflashWidget(self.vcecentralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vce.sizePolicy().hasHeightForWidth())
        self.vce.setSizePolicy(sizePolicy)
        self.vce.setObjectName(_fromUtf8("vce"))
        self.verticalLayout.addWidget(self.vce)
        vceMainWindow.setCentralWidget(self.vcecentralwidget)
        self.vcemenubar = QtGui.QMenuBar(vceMainWindow)
        self.vcemenubar.setGeometry(QtCore.QRect(0, 0, 1096, 26))
        self.vcemenubar.setObjectName(_fromUtf8("vcemenubar"))
        self.vcemenuFile = QtGui.QMenu(self.vcemenubar)
        self.vcemenuFile.setObjectName(_fromUtf8("vcemenuFile"))
        self.menuEdit = QtGui.QMenu(self.vcemenubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuSimulate = QtGui.QMenu(self.vcemenubar)
        self.menuSimulate.setEnabled(True)
        self.menuSimulate.setGeometry(QtCore.QRect(380, 151, 171, 80))
        self.menuSimulate.setObjectName(_fromUtf8("menuSimulate"))
        self.menuAnalyse = QtGui.QMenu(self.vcemenubar)
        self.menuAnalyse.setObjectName(_fromUtf8("menuAnalyse"))
        self.menuView = QtGui.QMenu(self.vcemenubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        vceMainWindow.setMenuBar(self.vcemenubar)
        self.vcetoolBar = QtGui.QToolBar(vceMainWindow)
        self.vcetoolBar.setIconSize(QtCore.QSize(50, 50))
        self.vcetoolBar.setObjectName(_fromUtf8("vcetoolBar"))
        vceMainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.vcetoolBar)
        self.vceactionOpen = QtGui.QAction(vceMainWindow)
        self.vceactionOpen.setObjectName(_fromUtf8("vceactionOpen"))
        self.actionSettings = QtGui.QAction(vceMainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionFlash_tank = QtGui.QAction(vceMainWindow)
        self.actionFlash_tank.setObjectName(_fromUtf8("actionFlash_tank"))
        self.actionFlashTank = QtGui.QAction(vceMainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/flash_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFlashTank.setIcon(icon1)
        self.actionFlashTank.setObjectName(_fromUtf8("actionFlashTank"))
        self.vceactionQuit = QtGui.QAction(vceMainWindow)
        self.vceactionQuit.setObjectName(_fromUtf8("vceactionQuit"))
        self.vcemenuFile.addAction(self.vceactionOpen)
        self.vcemenuFile.addSeparator()
        self.vcemenuFile.addAction(self.vceactionQuit)
        self.menuEdit.addAction(self.actionSettings)
        self.menuSimulate.addAction(self.actionFlashTank)
        self.vcemenubar.addAction(self.vcemenuFile.menuAction())
        self.vcemenubar.addAction(self.menuEdit.menuAction())
        self.vcemenubar.addAction(self.menuSimulate.menuAction())
        self.vcemenubar.addAction(self.menuAnalyse.menuAction())
        self.vcemenubar.addAction(self.menuView.menuAction())
        self.vcetoolBar.addAction(self.actionFlashTank)

        self.retranslateUi(vceMainWindow)
        QtCore.QMetaObject.connectSlotsByName(vceMainWindow)

    def retranslateUi(self, vceMainWindow):
        vceMainWindow.setWindowTitle(_translate("vceMainWindow", "vce", None))
        self.vcepushButton.setText(_translate("vceMainWindow", "Parse this file", None))
        self.vcemenuFile.setTitle(_translate("vceMainWindow", "File", None))
        self.menuEdit.setTitle(_translate("vceMainWindow", "Edit", None))
        self.menuSimulate.setTitle(_translate("vceMainWindow", "Simulate", None))
        self.menuAnalyse.setTitle(_translate("vceMainWindow", "Analyse", None))
        self.menuView.setTitle(_translate("vceMainWindow", "View", None))
        self.vcetoolBar.setWindowTitle(_translate("vceMainWindow", "toolBar", None))
        self.vceactionOpen.setText(_translate("vceMainWindow", "Open", None))
        self.actionSettings.setText(_translate("vceMainWindow", "Settings", None))
        self.actionFlash_tank.setText(_translate("vceMainWindow", "Flash tank", None))
        self.actionFlashTank.setText(_translate("vceMainWindow", "Flash Tank", None))
        self.vceactionQuit.setText(_translate("vceMainWindow", "Exit", None))

from vceflashwidget import vceflashWidget
import GUIresources_rc
