from PyQt5.QtGui import QIcon
from Registration_win import *
from manager_win import *
from manager import*
from reader import*
from reader_win import*
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(766, 458)
        MainWindow.setMinimumSize(QtCore.QSize(766, 458))
        MainWindow.setMaximumSize(QtCore.QSize(766, 458))
        MainWindow.setStyleSheet("#MainWindow{border-image:url(./img/beijing.jpg);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(340, 240, 141, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 240, 41, 16))
        self.label.setStyleSheet("color:rgb(255, 255, 255);")
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 290, 31, 20))
        self.label_2.setStyleSheet("color:rgb(255,255,255);")

        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(280, 330, 47, 16))
        #self.radioButton.setStyleSheet("color:rgb(255, 255, 255);")

        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(410, 330, 59, 16))
        #self.radioButton_2.setStyleSheet("color:rgb(255, 255, 255);")


        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 370, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 370, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(640, 360, 61, 20))
        self.label_3.setStyleSheet("color:rgb(255, 255, 255);")

        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(670, 390, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 290, 141, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setFocus()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 766, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.User_login)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton_3.clicked.connect(self.Sign_up)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图书管理系统"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "请输入帐号"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "请输入密码"))
        self.label.setText(_translate("MainWindow", "用户名"))
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.radioButton.setText(_translate("MainWindow", "学生"))
        self.radioButton_2.setText(_translate("MainWindow", "管理员"))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.pushButton_2.setText(_translate("MainWindow", "取消"))
        self.label_3.setText(_translate("MainWindow", "没有账号？"))
        self.pushButton_3.setText(_translate("MainWindow", "注册"))

    def User_login(self):
        username1 = self.lineEdit.text()
        password = self.lineEdit_2.text()
        user = []
        user.append(username1)
        user.append(password)

        if self.radioButton.isChecked() == True:
            flag = reader.Reader_login(user)
            if flag:
                student.setupUi(student,username1)
                student.show()
                MainWindow.close()
            else:
                QMessageBox.warning(None, "警告", "用户名或密码错误！", QMessageBox.Ok)
                self.lineEdit_2.setFocus()

        elif self.radioButton_2.isChecked() == True:
            manager = Manager()
            flag = manager.Manager_login(user)
            if flag:
                controller.setupUi(controller,username1)
                controller.show()
                MainWindow.close()
            else:
                QMessageBox.warning(None, "警告", "用户名或密码错误！", QMessageBox.Ok)
                self.lineEdit_2.setFocus()
        else:
            QMessageBox.warning(None,"警告","请选择一个身份",QMessageBox.Ok)
            self.lineEdit_2.setFocus()

    def Sign_up(self):
        MainWindow.hide()
        win.Win_clear()
        win.show()

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    reader = Reader()
    MainWindow = Ui_MainWindow()
    win = Registration_Window(MainWindow)
    controller = Manager_Window(MainWindow)
    student = Student_Window(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
