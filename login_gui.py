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
        MainWindow.resize(464, 389)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(140, 80, 191, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout_3 = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout_3.setLabelAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.formLayout_3.setContentsMargins(0, 10, 0, 0)
        self.formLayout_3.setHorizontalSpacing(0)
        self.formLayout_3.setVerticalSpacing(5)
        self.formLayout_3.setObjectName("formLayout_3")
        self.reg_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.reg_name.setObjectName("reg_name")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.reg_name)
        self.lab_name = QtWidgets.QLabel(self.layoutWidget)
        self.lab_name.setText("")
        self.lab_name.setObjectName("lab_name")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lab_name)
        self.reg_email = QtWidgets.QLineEdit(self.layoutWidget)
        self.reg_email.setObjectName("reg_email")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.reg_email)
        self.lab_email = QtWidgets.QLabel(self.layoutWidget)
        self.lab_email.setText("")
        self.lab_email.setObjectName("lab_email")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lab_email)
        self.reg_password = QtWidgets.QLineEdit(self.layoutWidget)
        self.reg_password.setObjectName("reg_password")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.reg_password)
        self.reg_password_confirmation = QtWidgets.QLineEdit(self.layoutWidget)
        self.reg_password_confirmation.setObjectName("reg_password_confirmation")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.reg_password_confirmation)
        self.lab_password_confirmation = QtWidgets.QLabel(self.layoutWidget)
        self.lab_password_confirmation.setEnabled(False)
        self.lab_password_confirmation.setSizeIncrement(QtCore.QSize(30, 30))
        self.lab_password_confirmation.setText("")
        self.lab_password_confirmation.setObjectName("lab_password_confirmation")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lab_password_confirmation)
        self.registration_button = QtWidgets.QPushButton(self.layoutWidget)
        self.registration_button.setObjectName("registration_button")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.registration_button)
        self.lab_password = QtWidgets.QLabel(self.layoutWidget)
        self.lab_password.setText("")
        self.lab_password.setObjectName("lab_password")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lab_password)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 464, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.registration_button.setText(_translate("MainWindow", "Registration"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

