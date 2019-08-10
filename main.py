import sys
from login_gui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.Resault)
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
        

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())