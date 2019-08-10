import sys
from login_gui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.Resault)

    # check nickname
    def Resault(self):
        # check nickname
        true = 0
        false = 0
        bag = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@', '_', '-', '+', '-', ]
        name = self.ui.lineEdit.text()
        name1 = name.split()
        namelist = []
        for i in range(0, len(name1)):
            for j in range(0, len(name1[i])):
                namelist.append(name1[i][j])

        if len(namelist) >= 1:
            for i in range(0, len(namelist)):
                for j in range(0, len(bag)):
                    if namelist[i] != bag[j]:
                        true += 1
                    elif namelist[i] == bag[j]:
                        false += 1
        if false != 0:
            print("Problem")
            pixmapfalse = QPixmap('icons/cancel-icon.png')
            self.ui.lab_nick.setPixmap(pixmapfalse)
        elif true > 0:
            print("Nice")
            pixmaptrue = QPixmap('icons/check-icon.png')
            self.ui.lab_nick.setPixmap(pixmaptrue)
        else:
            print("Вы нечего не написали")
            pixmapexceptio = QPixmap('icons/cancel-icon.png')
            self.ui.lab_nick.setPixmap(pixmapexceptio)
        #check email
        true_email = 0
        false_email = 0
        email = self.ui.lineEdit_2.text()
        eamil1 = email.split()
        emaillist = []
        for i in range(0, len(eamil1)):
            for j in range(0, len(eamil1[i])):
                emaillist.append(eamil1[i][j])
        if len(emaillist) >= 1:
            for i in range(0, len(emaillist)):
                if emaillist[i] == "@":
                    true_email += 1
        if true_email == 1:
            print("Nice")
            pixmaptrue1 = QPixmap('icons/check-icon.png')
            self.ui.lab_email.setPixmap(pixmaptrue1)
        elif true_email > 1:
            print("Вы нечего не написали")
            pixmapexceptio1 = QPixmap('icons/cancel-icon.png')
            self.ui.lab_email.setPixmap(pixmapexceptio1)
        else:
            print("Вы нечего не написали")
            pixmapexceptio2 = QPixmap('icons/cancel-icon.png')
            self.ui.lab_email.setPixmap(pixmapexceptio2)
        # check password

        password = self.ui.lineEdit_3.text()
        password1 = password.split()
        passwordlist = []
        password_1 = self.ui.lineEdit_4.text()
        password_2 = password_1.split()
        passwordlist2 = []
        count = 0 
        for i in range(0, len(password1)):
            for j in range(0, len(password1[i])):
                passwordlist.append(password1[i][j])
        for i in range(0, len(password_1)):
            for j in range(0, len(password_1[i])):
                passwordlist2.append(password_1[i][j])
        if len(passwordlist) != 0:
            if len(passwordlist) == len(passwordlist2):
                for i in range(0, len(passwordlist)):
                    if passwordlist[i] == passwordlist2[i]:
                        count += 1
                if count == len(passwordlist):
                    print("Nice")
                    pixmaptrue3 = QPixmap('icons/check-icon.png')
                    self.ui.lab_password.setPixmap(pixmaptrue3)
                    self.ui.lab_password2.setPixmap(pixmaptrue3)
                elif count > len(passwordlist) or count < len(passwordlist):
                    print("problem")
                    pixmapexcepti = QPixmap('icons/cancel-icon.png')
                    self.ui.lab_password.setPixmap(pixmapexcepti)
                    self.ui.lab_password2.setPixmap(pixmapexcepti)
            else:
                pixmapexcepti = QPixmap('icons/cancel-icon.png')
                self.ui.lab_password.setPixmap(pixmapexcepti)
                self.ui.lab_password2.setPixmap(pixmapexcepti)
        else:
            pixmapexcepti = QPixmap('icons/cancel-icon.png')
            self.ui.lab_password.setPixmap(pixmapexcepti)
            self.ui.lab_password2.setPixmap(pixmapexcepti)
            

        


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())