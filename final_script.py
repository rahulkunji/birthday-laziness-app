from facebookapp import *
from Helper import *
import sys
from PyQt4 import QtCore, QtGui

class Facebook():
    
    def start(self):
        self.MainWindow=QtGui.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.ui.help.clicked.connect(self.help_screen)
        self.ui.submit.clicked.connect(self.submit_button)
        self.MainWindow.show()
    
    def help_screen(self):  #shows help screen on click
        self.Form=QtGui.QWidget()
        ui1=Ui_Form()
        ui1.setupUi(self.Form)
        self.Form.show()

    
    def submit_button(self):
        self.key=str(self.ui.keytext.toPlainText())
        self.msg_p=str(self.ui.prefix_msg.toPlainText())
        self.msg_s=str(self.ui.suffix_msg.toPlainText())
        self.date1=str(self.ui.dateEdit.date())
        print self.key,self.msg_p,self.msg_s,self.date1
        #Facebook connectivity code to be added here

def main():
    app=QtGui.QApplication(sys.argv)
    F=Facebook()
    F.start()
    sys.exit(app.exec_())


if __name__=='__main__':
    main()
