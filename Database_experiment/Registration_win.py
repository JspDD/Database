# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zhuce.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from reader import*
from PyQt5.QtWidgets import *
import sys

class Registration_Window(QtWidgets.QMainWindow):
    def __init__(self,MainWindow):
        super(Registration_Window,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.MainWindow = MainWindow

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(618, 547)
        mainWindow.setMinimumSize(QtCore.QSize(618, 547))
        mainWindow.setMaximumSize(QtCore.QSize(618, 547))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 400, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 400, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(100, 140, 421, 201))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_Rno = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_Rno.setMaximumSize(QtCore.QSize(140, 20))
        self.lineEdit_Rno.setObjectName("lineEdit_Rno")
        self.gridLayout.addWidget(self.lineEdit_Rno, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_name.setMaximumSize(QtCore.QSize(140, 20))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_sex = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_sex.setMaximumSize(QtCore.QSize(140, 20))
        self.lineEdit_sex.setObjectName("lineEdit_sex")
        self.gridLayout.addWidget(self.lineEdit_sex, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)
        self.lineEdit_age = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_age.setMaximumSize(QtCore.QSize(140, 20))
        self.lineEdit_age.setObjectName("lineEdit_age")
        self.gridLayout.addWidget(self.lineEdit_age, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_phone = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_phone.setMaximumSize(QtCore.QSize(140, 20))
        self.lineEdit_phone.setText("")
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.gridLayout.addWidget(self.lineEdit_phone, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 2, 1, 1)
        self.lineEdit_username = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_username.setMaximumSize(QtCore.QSize(140, 20))
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.gridLayout.addWidget(self.lineEdit_username, 2, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_password = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_password.setMaximumSize(QtCore.QSize(140, 20))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.gridLayout.addWidget(self.lineEdit_password, 3, 1, 1, 1)
        self.lineEdit_password_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_password_2.setMaximumSize(QtCore.QSize(140, 20))
        self.lineEdit_password_2.setObjectName("lineEdit_password_2")
        self.gridLayout.addWidget(self.lineEdit_password_2, 3, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 2, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 618, 23))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.sign_up)
        self.pushButton_2.clicked.connect(self.Win_cancel)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "注册"))
        self.pushButton.setText(_translate("mainWindow", "确定"))
        self.pushButton_2.setText(_translate("mainWindow", "取消"))
        self.label.setText(_translate("mainWindow", "学号"))
        self.label_5.setText(_translate("mainWindow", "    姓名"))
        self.label_2.setText(_translate("mainWindow", "性别"))
        self.label_6.setText(_translate("mainWindow", "    年龄"))
        self.label_3.setText(_translate("mainWindow", "电话"))
        self.label_7.setText(_translate("mainWindow", "  用户名"))
        self.label_4.setText(_translate("mainWindow", "密码"))
        self.label_8.setText(_translate("mainWindow", " 确认密码"))


    def sign_up(self):
        Rno = self.lineEdit_Rno.text()
        Rname = self.lineEdit_name.text()
        Rsex = self.lineEdit_sex.text()
        Rage = self.lineEdit_age.text()
        Rphone = self.lineEdit_phone.text()
        Ruser = self.lineEdit_username.text()
        Rpassword = self.lineEdit_password.text()
        Rpassword_2 = self.lineEdit_password_2.text()
        user = []
        user.append(Rno)
        user.append(Rname)
        user.append(Rsex)
        user.append(Rage)
        user.append(Rphone)
        user.append(Ruser)
        user.append(Rpassword)
        reader = Reader()
        if (Rno == '' or Rname == '' or Rage == '' or Rphone == '' or Ruser == '' or Rsex == '' or Rpassword == ''):
            QMessageBox.warning(None, "警告", "请填写提示内容", QMessageBox.Ok)
            self.lineEdit_Rno.setFocus()
        elif Rpassword != Rpassword_2:
            QMessageBox.warning(None, "警告","两次密码不一样", QMessageBox.Ok)
            self.lineEdit_password.setFocus()
        elif reader.Search_by_Rno(Rno):
            QMessageBox.warning(None, "警告", "该用户已经注册", QMessageBox.Ok)
            self.lineEdit_Rno.setFocus()
        elif reader.Search_by_Username(Ruser):
            QMessageBox.warning(None, "警告", "该用户名已被使用", QMessageBox.Ok)
            self.lineEdit_username.setFocus()
        else:
            QMessageBox.information(None, "提示","注册成功", QMessageBox.Ok)
            reader.Insert_user(user)
            self.close()
            self.MainWindow.show()

    def Win_clear(self):
        self.lineEdit_Rno.clear()
        self.lineEdit_name.clear()
        self.lineEdit_sex.clear()
        self.lineEdit_age.clear()
        self.lineEdit_phone.clear()
        self.lineEdit_username.clear()
        self.lineEdit_password.clear()
        self.lineEdit_password_2.clear()

    def Win_cancel(self):
        self.close()
        self.MainWindow.show()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Registration_Window()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())