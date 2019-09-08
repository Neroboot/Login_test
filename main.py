import sys
import re
from login_gui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap



class MainWindow(QtWidgets.QMainWindow):


    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.registration_button.clicked.connect(self.Get_registration_user)
        self.registrationform = []


    def Get_registration_user(self):
        self.get_nick = self.ui.reg_name.text()
        if self.get_nick != "" and len(self.get_nick) >= 5:
            self.user_get_registration_nick = self.User_verification_for_registration_nick()
        self.get_email = self.ui.reg_email.text()
        if self.get_email != "":
            self.user_get_registration_email = self.User_verification_for_registration_email()
        self.Choosing_qmassagebox()
        
        


    def User_verification_for_registration_email(self):
        for_check_email = re.findall('.', self.get_email)
        if "@" not in for_check_email:
            print("this is not a valid email")
            return False
        return True


    def User_verification_for_registration_nick(self):
        forbidden_items = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@', '_', '-', '+', '-']
        for i in range(0, len(self.get_nick.lower())):
            if self.get_nick[i] in forbidden_items:
                print("this is not a valid nick")
                return False
        return True


            
    def Choosing_qmassagebox(self):
        if self.get_email == "" or self.get_nick == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Вы ничего не ввели")
            msgBox.exec()
        elif self.user_get_registration_email != True or self.user_get_registration_nick != True:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Вы ввели некорректное имя или email")
            msgBox.exec()
        else:    
            self.User_created_profile()
    def User_created_profile(self):
        pass

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())