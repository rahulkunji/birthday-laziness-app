from facebookapp import *
from Helper import *
import sys,datetime,time
from PyQt4 import QtCore, QtGui
import ConnectionTester
import requests
class Facebook():
    
    def start(self):
        self.MainWindow=QtGui.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.ui.help.clicked.connect(self.help_screen)
        self.ui.submit.clicked.connect(self.submit_button)
        self.ui.Connection.clicked.connect(self.test_connection)
        self.MainWindow.show()
    
    def get_posts(self):
        temp = "SELECT post_id, actor_id, message FROM stream WHERE "
        "filter_key = 'others' AND source_id = me() AND "
        "created_time > %s limit 200",self.time_stamp
        query=(temp)
        payload = {'q': query, 'access_token': self.key}
        r = requests.get('https://graph.facebook.com/fql', params=payload)
        result = json.loads(r.text)
        return result['data']

    def help_screen(self):  #shows help screen on click
        self.Form=QtGui.QWidget()
        ui1=Ui_Form()
        ui1.setupUi(self.Form)
        Form.show()

    def post_function(self,wallposts):
        for wallpost in wallposts:
            self.r = requests.get('https://graph.facebook.com/%s' %
                wallpost['actor_id'])
            self.url = 'https://graph.facebook.com/%s/comments' % wallpost['post_id']
            self.user = json.loads(self.r.text)
            self.message = 'Thanks %s :)' % user['first_name']
            self.payload = {'access_token': TOKEN, 'message': message}
            self.s = requests.post(url, data=payload)
            print "Wall post %s done" % wallpost['post_id']

    def test_connection(self):
        self.Form2=QtGui.QWidget()
        self.ui2=ConnectionTester.Ui_Form()
        self.ui2.setupUi(self.Form2)
        self.Form2.show()
        #code to be tested
        '''for wallpost in wallposts:
            r = requests.get('https://graph.facebook.com/%s' %
                wallpost['actor_id'])
            url = 'https://graph.facebook.com/%s/comments' % wallpost['post_id']
            user = json.loads(r.text)
            x= x + "Wall post %s done" % wallpost['post_id']
        self.ui2.textBrowser.setText(x)'''
 
    
    def submit_button(self):
        self.key=str(self.ui.keytext.toPlainText())
        self.msg_p=str(self.ui.prefix_msg.toPlainText())
        self.msg_s=str(self.ui.suffix_msg.toPlainText())
        self.date1=str(self.ui.dateEdit.date().toPyDate())
        self.time_stamp=int(time.mktime(datetime.datetime.strptime(self.date1, "%Y-%m-%d").timetuple())) 
        print self.time_stamp
        self.post_function(self.get_posts())
        
        #Facebook connectivity code to be added here

def main():
    app=QtGui.QApplication(sys.argv)
    F=Facebook()
    F.start()
    sys.exit(app.exec_())


if __name__=='__main__':
    main()
