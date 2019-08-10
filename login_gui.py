# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(202, 215)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 171, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Nickname")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText("Email")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setPlaceholderText("Password")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setPlaceholderText("Password")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lineEdit_4)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.pushButton)
        self.lab_nick = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lab_nick.setText("")
        self.lab_nick.setObjectName("lab_nick")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lab_nick)
        self.lab_email = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lab_email.setText("")
        self.lab_email.setObjectName("lab_email")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lab_email)
        self.lab_password = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lab_password.setText("")
        self.lab_password.setObjectName("lab_password")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lab_password)
        self.lab_password2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lab_password2.setText("")
        self.lab_password2.setObjectName("lab_password2")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lab_password2)
        self.verticalLayout.addLayout(self.formLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 202, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Random"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

