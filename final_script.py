from facebookapp import *
import sys
from PyQt4 import QtCore, QtGui

def main():
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    

if __name__=='__main__':
    main()
