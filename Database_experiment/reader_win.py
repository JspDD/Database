import datetime,time
from admin_win import *
from book import *
from PyQt5 import QtCore, QtGui, QtWidgets
from reader import *
import sys

class Student_Window(QtWidgets.QMainWindow):
    def __init__(self,MainWindow):
        super(Student_Window,self).__init__()
        self.MainWindow = MainWindow
    def setupUi(self, mainWindow,name):

        reader_1 = Reader()
        user =  reader_1.Search_by_Username(name)
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(705, 448)
        mainWindow.setMinimumSize(QtCore.QSize(705, 448))
        mainWindow.setMaximumSize(QtCore.QSize(705, 448))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(590, 20, 75, 23))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 60, 661, 321))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(30, 140, 591, 141))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setEditTriggers(QTableView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(40, 30, 54, 12))
        self.label_4.setObjectName("label_4")
        self.lineEdit_bno = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_bno.setGeometry(QtCore.QRect(110, 30, 113, 20))
        self.lineEdit_bno.setObjectName("lineEdit_bno")
        self.lineEdit_press = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_press.setGeometry(QtCore.QRect(110, 70, 113, 20))
        self.lineEdit_press.setObjectName("lineEdit_press")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(40, 71, 54, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(280, 30, 54, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(280, 70, 54, 12))
        self.label_7.setObjectName("label_7")
        self.lineEdit_bname = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_bname.setGeometry(QtCore.QRect(340, 30, 113, 20))
        self.lineEdit_bname.setObjectName("lineEdit_bname")
        self.lineEdit_author = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_author.setGeometry(QtCore.QRect(340, 70, 113, 20))
        self.lineEdit_author.setObjectName("lineEdit_author")
        self.pushButton_search = QtWidgets.QPushButton(self.tab)
        self.pushButton_search.setGeometry(QtCore.QRect(500, 30, 75, 23))
        self.pushButton_search.setObjectName("pushButton_search")
        self.checkBox_bno = QtWidgets.QCheckBox(self.tab)
        self.checkBox_bno.setGeometry(QtCore.QRect(90, 110, 71, 16))
        self.checkBox_bno.setObjectName("checkBox_bno")
        self.checkBox_bname = QtWidgets.QCheckBox(self.tab)
        self.checkBox_bname.setGeometry(QtCore.QRect(190, 110, 71, 16))
        self.checkBox_bname.setObjectName("checkBox_bname")
        self.checkBox_author = QtWidgets.QCheckBox(self.tab)
        self.checkBox_author.setGeometry(QtCore.QRect(290, 110, 71, 16))
        self.checkBox_author.setObjectName("checkBox_author")
        self.checkBox_press = QtWidgets.QCheckBox(self.tab)
        self.checkBox_press.setGeometry(QtCore.QRect(380, 110, 71, 16))
        self.checkBox_press.setObjectName("checkBox_press")
        self.pushButton_borrow = QtWidgets.QPushButton(self.tab)
        self.pushButton_borrow.setGeometry(QtCore.QRect(500, 70, 75, 23))
        self.pushButton_borrow.setObjectName("pushButton_borrow")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(40, 20, 571, 192))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_2.setEditTriggers(QTableView.NoEditTriggers)
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.pushButton_show = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_show.setGeometry(QtCore.QRect(220,250, 75, 23))
        self.pushButton_show.setObjectName("pushButton_show")
        self.pushButton_back = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_back.setGeometry(QtCore.QRect(360, 250, 75, 23))
        self.pushButton_back.setObjectName("pushButton_back")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_name = QtWidgets.QLabel(self.tab_4)
        self.label_name.setGeometry(QtCore.QRect(60, 40, 54, 12))
        self.label_name.setObjectName("label_name")
        self.lineEdit_Rname = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_Rname.setGeometry(QtCore.QRect(130, 40, 113, 20))
        self.lineEdit_Rname.setObjectName("lineEdit_Rname")
        self.lineEdit_phone = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_phone.setGeometry(QtCore.QRect(130, 110, 113, 20))
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.lineEdit_age = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_age.setGeometry(QtCore.QRect(410, 40, 113, 20))
        self.lineEdit_age.setObjectName("lineEdit_age")
        self.lineEdit_username = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_username.setGeometry(QtCore.QRect(410, 110, 113, 20))
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.label_age = QtWidgets.QLabel(self.tab_4)
        self.label_age.setGeometry(QtCore.QRect(340, 40, 54, 12))
        self.label_age.setObjectName("label_age")
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        self.label_10.setGeometry(QtCore.QRect(60, 110, 54, 12))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(60, 180, 54, 12))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(340, 110, 54, 12))
        self.label_12.setObjectName("label_12")
        self.lineEdit_pwd = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_pwd.setGeometry(QtCore.QRect(130, 180, 113, 20))
        self.lineEdit_pwd.setObjectName("lineEdit_pwd")
        self.lineEdit_newpwd = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_newpwd.setGeometry(QtCore.QRect(410, 180, 113, 20))
        self.lineEdit_newpwd.setObjectName("lineEdit_newpwd")
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setGeometry(QtCore.QRect(340, 180, 54, 12))
        self.label_13.setObjectName("label_13")
        self.pushButton_enter = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_enter.setGeometry(QtCore.QRect(200, 250, 75, 23))
        self.pushButton_enter.setObjectName("pushButton_enter")
        self.pushbutton_cancel2 = QtWidgets.QPushButton(self.tab_4)
        self.pushbutton_cancel2.setGeometry(QtCore.QRect(370, 250, 75, 23))
        self.pushbutton_cancel2.setObjectName("pushbutton_cancel2")
        self.tabWidget.addTab(self.tab_4, "")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(420, 20, 110, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_username = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_username.setFont(font)
        self.label_username.setObjectName("label_username")
        self.horizontalLayout.addWidget(self.label_username)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 705, 23))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.pushButton_exit.clicked.connect(self.Win_exit)
        self.pushButton_search.clicked.connect(self.Serch_book)
        self.pushButton_borrow.clicked.connect(self.Borrow)
        self.pushButton_show.clicked.connect(self.Show_record)
        self.pushButton_back.clicked.connect(self.Return_book)
        self.pushButton_enter.clicked.connect(self.Change)
        self.pushbutton_cancel2.clicked.connect(self.Cancel)

        self.retranslateUi(mainWindow,user)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
    def retranslateUi(self, mainWindow,user):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "图书管理系统"))
        self.label.setText(_translate("mainWindow", "【学生端 】"))
        self.pushButton_exit.setText(_translate("mainWindow", "注销"))
        self.label_4.setText(_translate("mainWindow", "图书编号"))
        self.label_5.setText(_translate("mainWindow", "出版社"))
        self.label_6.setText(_translate("mainWindow", "书名"))
        self.label_7.setText(_translate("mainWindow", "作者"))
        self.pushButton_search.setText(_translate("mainWindow", "查询"))
        self.checkBox_bno.setText(_translate("mainWindow", "图书编号"))
        self.checkBox_bname.setText(_translate("mainWindow", "书名"))
        self.checkBox_author.setText(_translate("mainWindow", "作者"))
        self.checkBox_press.setText(_translate("mainWindow", "出版社"))
        self.pushButton_borrow.setText(_translate("mainWindow", "借阅"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mainWindow", "图书查询"))
        self.pushButton_show.setText(_translate("mainWindow", "借阅查询"))
        self.pushButton_back.setText(_translate("mainWindow", "还书"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mainWindow", "图书归还"))
        self.label_name.setText(_translate("mainWindow", "姓名"))
        self.label_age.setText(_translate("mainWindow", "年龄"))
        self.label_10.setText(_translate("mainWindow", "电话号码"))
        self.label_11.setText(_translate("mainWindow", "旧密码"))
        self.label_12.setText(_translate("mainWindow", "用户名"))
        self.label_13.setText(_translate("mainWindow", "新密码"))
        self.pushButton_enter.setText(_translate("mainWindow", "确定"))
        self.pushbutton_cancel2.setText(_translate("mainWindow", "取消"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("mainWindow", "信息修改"))
        self.label_2.setText(_translate("mainWindow", "欢迎！"))
        self.label_username.setText(_translate("mainWindow",user[5]))

        self.lineEdit_Rname.setText(_translate("mainWindow", user[1]))
        self.lineEdit_age.setText(_translate("mainWindow", str(user[3])))
        self.lineEdit_username.setText(_translate("mainWindow", user[5]))
        self.lineEdit_phone.setText(_translate("mainWindow", user[4]))
    #退出
    def Win_exit(self):
        self.close()
        self.MainWindow.show()
    #查阅书籍
    def Serch_book(self):
        stu = Reader()
        bno = self.lineEdit_bno.text()
        bname = self.lineEdit_bname.text()
        bpress = self.lineEdit_press.text()
        author = self.lineEdit_author.text()
        sql = "select * from book where 1 "
        if(    self.checkBox_bno.isChecked()
            or self.checkBox_author.isChecked()
            or self.checkBox_bname.isChecked()
            or self.checkBox_press.isChecked() ):

            if(self.checkBox_bno.isChecked()):
                sql = sql + "and Bno = '"+ bno + "'"
            if (self.checkBox_bname.isChecked()):
                sql = sql + "and Bname = '" + bname + "'"
            if (self.checkBox_author.isChecked()):
                sql = sql + "and Bauthor like '%" + author + "%'"
            if (self.checkBox_press.isChecked()):
                sql = sql + "and Bpress = '" + bpress + "'"
        books = stu.Search(sql)
        if books:
            self.tableWidget.setColumnCount(len(books[0]))
            self.tableWidget.setRowCount(len(books))
            self.tableWidget.setHorizontalHeaderLabels(['图书编号', '书名', '作者', '出版社', '剩余数量'])
            for i in range(len(books)):
                for j in range(len(books[0])):
                    item = QTableWidgetItem(str(books[i][j]))
                    self.tableWidget.setItem(i, j, item)
        else:
            self.tableWidget.setColumnCount(0)
            self.tableWidget.setRowCount(0)
        return True
    #修改个人信息
    def Change(self):
        stu = Reader()
        oldusername = self.label_username.text()
        old = stu.Search_by_Username(oldusername)
        rno = old[0]
        name = self.lineEdit_Rname.text()
        age = self.lineEdit_age.text()
        phone = self.lineEdit_phone.text()
        uname = self.lineEdit_username.text()
        oldpwd = self.lineEdit_pwd.text()
        newpwd = self.lineEdit_newpwd.text()
        user = []
        user.append(rno)
        user.append(name)
        user.append(age)
        user.append(phone)
        user.append(uname)
        user.append(newpwd)
        if oldpwd != old[6]:
            QMessageBox.warning(None, "警告", "原密码输入错误！", QMessageBox.Ok)
            self.lineEdit_pwd.setFocus()
        elif stu.Judge_Username(rno,uname):
            QMessageBox.warning(None, "警告", "该用户名已被使用", QMessageBox.Ok)
            self.lineEdit_username.setFocus()
        else:
            self.label_username.setText(uname)
            stu.Update(user)
            QMessageBox.information(None, "提示", "修改成功！", QMessageBox.Ok)
            self.lineEdit_pwd.setText('')
            self.lineEdit_newpwd.setText('')
    #取消修改个人信息
    def Cancel(self):
        stu = Reader()
        oldusername = self.label_username.text()
        user = stu.Search_by_Username(oldusername)
        self.lineEdit_Rname.setText(user[1])
        self.lineEdit_age.setText(str(user[3]))
        self.lineEdit_username.setText(user[5])
        self.lineEdit_phone.setText(user[4])
        self.lineEdit_pwd.setText('')
        self.lineEdit_newpwd.setText('')
    #借书
    def Borrow(self):
        stu = Reader()
        book = Book()
        username = self.label_username.text()
        message = stu.Search_by_Username(username)
        Rno =  message[0]

        rownum = self.tableWidget.currentRow()
        if rownum < 0:
            QMessageBox.information(None, "提示", "请先选择一本书！", QMessageBox.Ok)
            return
        Bno = self.tableWidget.item(rownum,0).text()
        start = datetime.datetime.now()
        end = start + datetime.timedelta(days=30)
        start = str(start.strftime('%Y-%m-%d'))
        end = str(end.strftime('%Y-%m-%d'))
        borrow = []
        borrow.append(Rno)
        borrow.append(Bno)
        borrow.append(start)
        borrow.append(end)
        num = book.Get_book_num(Bno)
        if num <= 0:
            QMessageBox.information(None, "提示", "书本已借完！", QMessageBox.Ok)
            return
        else:
            if stu.Judge_bno(Rno,Bno):
                QMessageBox.information(None, "提示", "您已经借阅该书本！", QMessageBox.Ok)
                return
            elif stu.Borrow_book(borrow):
                QMessageBox.information(None, "提示", "借阅成功！", QMessageBox.Ok)
                num = num - 1
                item = QTableWidgetItem(str(num))
                self.tableWidget.setItem(rownum,4,item)
                book.Sub_book_num(Bno)
    #显示借阅记录
    def Show_record(self):
        stu = Reader()
        username = self.label_username.text()
        message = stu.Search_by_Username(username)
        Rno = message[0]
        records = stu.Borrow_record(Rno)
        if records:
            self.tableWidget_2.setColumnCount(len(records[0]))
            self.tableWidget_2.setRowCount(len(records))
            self.tableWidget_2.setHorizontalHeaderLabels(['借阅编号', '图书编号', '借阅日期', '应还日期'])
            for i in range(len(records)):
                for j in range(len(records[0])):
                    item = QTableWidgetItem(str(records[i][j]))
                    self.tableWidget_2.setItem(i,j,item)
        else:
            self.tableWidget_2.setColumnCount(0)
            self.tableWidget_2.setRowCount(0)
    #还书
    def Return_book(self):
        stu = Reader()
        book = Book()
        username = self.label_username.text()
        message = stu.Search_by_Username(username)
        Rno = message[0]
        rownum = self.tableWidget_2.currentRow()
        if rownum < 0:
            QMessageBox.information(None, "提示", "没有要换的书！", QMessageBox.Ok)
            return

        Bno = self.tableWidget_2.item(rownum,1).text()
        if stu.Back(Rno,Bno):
            QMessageBox.information(None, "提示", "还书成功！", QMessageBox.Ok)
            self.tableWidget_2.removeRow(rownum)
            book.Add_book_num(Bno)
        return