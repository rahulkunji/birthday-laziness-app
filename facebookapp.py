# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'facebookapp.ui'
#
# Created: Sun Jun 01 12:16:46 2014
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(511, 565)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.keytext = QtGui.QPlainTextEdit(self.centralWidget)
        self.keytext.setGeometry(QtCore.QRect(170, 50, 281, 41))
        self.keytext.setObjectName(_fromUtf8("keytext"))
        self.prefix_msg = QtGui.QPlainTextEdit(self.centralWidget)
        self.prefix_msg.setGeometry(QtCore.QRect(170, 150, 281, 61))
        self.prefix_msg.setObjectName(_fromUtf8("prefix_msg"))
        self.suffix_msg = QtGui.QPlainTextEdit(self.centralWidget)
        self.suffix_msg.setGeometry(QtCore.QRect(170, 230, 281, 61))
        self.suffix_msg.setObjectName(_fromUtf8("suffix_msg"))
        self.dateEdit = QtGui.QDateEdit(self.centralWidget)
        self.dateEdit.setGeometry(QtCore.QRect(170, 110, 301, 24))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.prefix_radioButton = QtGui.QRadioButton(self.centralWidget)
        self.prefix_radioButton.setGeometry(QtCore.QRect(170, 320, 102, 20))
        self.prefix_radioButton.setObjectName(_fromUtf8("prefix_radioButton"))
        self.suffix_radioButton = QtGui.QRadioButton(self.centralWidget)
        self.suffix_radioButton.setGeometry(QtCore.QRect(280, 320, 102, 20))
        self.suffix_radioButton.setObjectName(_fromUtf8("suffix_radioButton"))
        self.Both_radioButton = QtGui.QRadioButton(self.centralWidget)
        self.Both_radioButton.setGeometry(QtCore.QRect(380, 320, 102, 20))
        self.Both_radioButton.setObjectName(_fromUtf8("Both_radioButton"))
        self.submit = QtGui.QPushButton(self.centralWidget)
        self.submit.setGeometry(QtCore.QRect(140, 410, 114, 32))
        self.submit.setObjectName(_fromUtf8("submit"))
        self.fblbl = QtGui.QLabel(self.centralWidget)
        self.fblbl.setGeometry(QtCore.QRect(30, 60, 131, 21))
        self.fblbl.setObjectName(_fromUtf8("fblbl"))
        self.birthdate = QtGui.QLabel(self.centralWidget)
        self.birthdate.setGeometry(QtCore.QRect(30, 110, 131, 21))
        self.birthdate.setObjectName(_fromUtf8("birthdate"))
        self.prefixmg = QtGui.QLabel(self.centralWidget)
        self.prefixmg.setGeometry(QtCore.QRect(30, 150, 131, 21))
        self.prefixmg.setObjectName(_fromUtf8("prefixmg"))
        self.postfixmsg = QtGui.QLabel(self.centralWidget)
        self.postfixmsg.setGeometry(QtCore.QRect(30, 230, 131, 21))
        self.postfixmsg.setObjectName(_fromUtf8("postfixmsg"))
        self.msgformat = QtGui.QLabel(self.centralWidget)
        self.msgformat.setGeometry(QtCore.QRect(30, 320, 91, 21))
        self.msgformat.setObjectName(_fromUtf8("msgformat"))
        self.likelbl = QtGui.QLabel(self.centralWidget)
        self.likelbl.setGeometry(QtCore.QRect(30, 370, 91, 21))
        self.likelbl.setObjectName(_fromUtf8("likelbl"))
        self.no_radioButton = QtGui.QRadioButton(self.centralWidget)
        self.no_radioButton.setGeometry(QtCore.QRect(260, 370, 102, 20))
        self.no_radioButton.setObjectName(_fromUtf8("no_radioButton"))
        self.yes_radioButton = QtGui.QRadioButton(self.centralWidget)
        self.yes_radioButton.setGeometry(QtCore.QRect(170, 370, 102, 20))
        self.yes_radioButton.setObjectName(_fromUtf8("yes_radioButton"))
        self.help = QtGui.QPushButton(self.centralWidget)
        self.help.setGeometry(QtCore.QRect(280, 410, 114, 32))
        self.help.setObjectName(_fromUtf8("help"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 511, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Facebook - Bulk reply App", None))
        self.prefix_radioButton.setText(_translate("MainWindow", "Prefix", None))
        self.suffix_radioButton.setText(_translate("MainWindow", "Suffix", None))
        self.Both_radioButton.setText(_translate("MainWindow", "Both", None))
        self.submit.setText(_translate("MainWindow", "Submit", None))
        self.fblbl.setText(_translate("MainWindow", "Facebook Key", None))
        self.birthdate.setText(_translate("MainWindow", "<html><head/><body><p>Birthdate</p></body></html>", None))
        self.prefixmg.setText(_translate("MainWindow", "Prefix Message", None))
        self.postfixmsg.setText(_translate("MainWindow", "Suffix Message", None))
        self.msgformat.setText(_translate("MainWindow", "Message Format", None))
        self.likelbl.setText(_translate("MainWindow", "Like posts?", None))
        self.no_radioButton.setText(_translate("MainWindow", "No", None))
        self.yes_radioButton.setText(_translate("MainWindow", "Yes", None))
        self.help.setText(_translate("MainWindow", "View Help", None))

