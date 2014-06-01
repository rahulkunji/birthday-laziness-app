# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'facebookapp.ui'
#
# Created: Sun Jun  1 09:53:13 2014
#      by: PyQt4 UI code generator 4.10.4
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
        MainWindow.resize(485, 481)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralWidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(170, 20, 281, 41))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.centralWidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(170, 120, 281, 61))
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.plainTextEdit_3 = QtGui.QPlainTextEdit(self.centralWidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(170, 200, 281, 61))
        self.plainTextEdit_3.setObjectName(_fromUtf8("plainTextEdit_3"))
        self.dateEdit = QtGui.QDateEdit(self.centralWidget)
        self.dateEdit.setGeometry(QtCore.QRect(170, 80, 301, 24))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.radioButton = QtGui.QRadioButton(self.centralWidget)
        self.radioButton.setGeometry(QtCore.QRect(170, 290, 102, 20))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.centralWidget)
        self.radioButton_2.setGeometry(QtCore.QRect(280, 290, 102, 20))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.centralWidget)
        self.radioButton_3.setGeometry(QtCore.QRect(380, 290, 102, 20))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.checkBox = QtGui.QCheckBox(self.centralWidget)
        self.checkBox.setGeometry(QtCore.QRect(170, 330, 87, 20))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 380, 114, 32))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 131, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 131, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 131, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 131, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(30, 290, 91, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(30, 330, 131, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 485, 22))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.radioButton.setText(_translate("MainWindow", "Prefix", None))
        self.radioButton_2.setText(_translate("MainWindow", "Suffix", None))
        self.radioButton_3.setText(_translate("MainWindow", "Both", None))
        self.checkBox.setText(_translate("MainWindow", "Like ", None))
        self.pushButton.setText(_translate("MainWindow", "Submit", None))
        self.label.setText(_translate("MainWindow", "Facebook Key", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Birthdate</p></body></html>", None))
        self.label_3.setText(_translate("MainWindow", "Prefix Message", None))
        self.label_4.setText(_translate("MainWindow", "Suffix Message", None))
        self.label_5.setText(_translate("MainWindow", "Message Format", None))
        self.label_6.setText(_translate("MainWindow", "Like also", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

