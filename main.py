import sys
from login_gui import *
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.Resault)
    def Resault(self):
        true = 0
        false = 0
        bag = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@']
        name = self.ui.lineEdit.text()
        name1 = name.split()
        namelist = []
        for i in range(0, len(name1)):
            for j in range(0, len(name1[i])):
                namelist.append(name1[i][j])
        print(namelist)
        for i in range(0, len(namelist)):
            for j in range(0, len(bag)):
                if namelist[i] != bag[j]:
                    true += 1
                elif namelist[i] == bag[j]:
                    false += 1
        if false == 0:
            print("Problem")
        else:
            print("Nice")
                    
            
        self.ui.lineEdit.setPlaceholderText("123")

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())