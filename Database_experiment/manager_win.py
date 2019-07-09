import datetime
from admin_win import *
from book import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
class Manager_Window(QtWidgets.QMainWindow):
    def __init__(self,MainWindow):
        super(Manager_Window,self).__init__()
        self.MainWindow = MainWindow

    def setupUi(self, mainWindow,name):
        manager = Manager()
        user = manager.Search_by_Username(name)
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(705, 448)
        mainWindow.setMinimumSize(QtCore.QSize(705, 448))
        mainWindow.setMaximumSize(QtCore.QSize(705, 448))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(590, 20, 75, 23))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 60, 661, 350))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(200, 140, 421, 141))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setEditTriggers(QTableView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(220, 30, 54, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_bno = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_bno.setGeometry(QtCore.QRect(280, 30, 113, 20))
        self.lineEdit_bno.setObjectName("lineEdit_bno")
        self.lineEdit_press = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_press.setGeometry(QtCore.QRect(280, 70, 113, 20))
        self.lineEdit_press.setObjectName("lineEdit_press")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(220, 70, 54, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(440, 30, 54, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(440, 72, 54, 20))
        self.label_7.setObjectName("label_7")
        self.lineEdit_bname = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_bname.setGeometry(QtCore.QRect(500, 30, 113, 20))
        self.lineEdit_bname.setObjectName("lineEdit_bname")
        self.lineEdit_author = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_author.setGeometry(QtCore.QRect(500, 70, 113, 20))
        self.lineEdit_author.setObjectName("lineEdit_author")
        self.pushButton_booksearch = QtWidgets.QPushButton(self.tab)
        self.pushButton_booksearch.setGeometry(QtCore.QRect(50, 150, 91, 23))
        self.pushButton_booksearch.setObjectName("pushButton_booksearch")
        self.checkBox_bno = QtWidgets.QCheckBox(self.tab)
        self.checkBox_bno.setGeometry(QtCore.QRect(220, 110, 71, 16))
        self.checkBox_bno.setObjectName("checkBox_bno")
        self.checkBox_bname = QtWidgets.QCheckBox(self.tab)
        self.checkBox_bname.setGeometry(QtCore.QRect(340, 110, 71, 16))
        self.checkBox_bname.setObjectName("checkBox_bname")
        self.checkBox_author = QtWidgets.QCheckBox(self.tab)
        self.checkBox_author.setGeometry(QtCore.QRect(440, 110, 71, 16))
        self.checkBox_author.setObjectName("checkBox_author")
        self.checkBox_press = QtWidgets.QCheckBox(self.tab)
        self.checkBox_press.setGeometry(QtCore.QRect(540, 110, 71, 16))
        self.checkBox_press.setObjectName("checkBox_press")
        self.pushButton_bookadd = QtWidgets.QPushButton(self.tab)
        self.pushButton_bookadd.setGeometry(QtCore.QRect(50, 250, 91, 23))
        self.pushButton_bookadd.setObjectName("pushButton_bookadd")
        self.lineEdit_booknum = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_booknum.setGeometry(QtCore.QRect(90, 30, 113, 20))
        self.lineEdit_booknum.setObjectName("lineEdit_booknum")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 54, 20))
        self.label_3.setObjectName("label_3")
        self.pushButton_bookchange = QtWidgets.QPushButton(self.tab)
        self.pushButton_bookchange.setGeometry(QtCore.QRect(50, 200, 91, 23))
        self.pushButton_bookchange.setObjectName("pushButton_bookchange")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(210, 20, 421, 192))
        self.tableWidget_2.setObjectName("tableWidget_2")

        self.tableWidget_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_2.setEditTriggers(QTableView.NoEditTriggers)
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.pushButton_usersearch = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_usersearch.setGeometry(QtCore.QRect(60, 190, 75, 23))
        self.pushButton_usersearch.setObjectName("pushButton_usersearch")
        self.pushButton_userdelete = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_userdelete.setGeometry(QtCore.QRect(310, 240, 75, 23))
        self.pushButton_userdelete.setObjectName("pushButton_userdelete")
        self.pushButton_usergrant = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_usergrant.setGeometry(QtCore.QRect(460, 240, 75, 23))
        self.pushButton_usergrant.setObjectName("pushButton_usergrant")
        self.lineEdit_rno = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_rno.setGeometry(QtCore.QRect(80, 30, 113, 20))
        self.lineEdit_rno.setObjectName("lineEdit_rno")
        self.lineEdit_rname = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_rname.setGeometry(QtCore.QRect(80, 80, 113, 20))
        self.lineEdit_rname.setObjectName("lineEdit_rname")
        self.checkBox_rno = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_rno.setGeometry(QtCore.QRect(30, 140, 71, 20))
        self.checkBox_rno.setObjectName("checkBox_rno")
        self.checkBox_rname = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_rname.setGeometry(QtCore.QRect(130, 140, 71, 20))
        self.checkBox_rname.setObjectName("checkBox_rname")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(20, 30, 54, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(20, 80, 54, 12))
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_name = QtWidgets.QLabel(self.tab_3)
        self.label_name.setGeometry(QtCore.QRect(60, 40, 54, 12))
        self.label_name.setObjectName("label_name")
        self.lineEdit_Mname = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_Mname.setGeometry(QtCore.QRect(130, 40, 113, 20))
        self.lineEdit_Mname.setObjectName("lineEdit_Mname")
        self.lineEdit_Mphone = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_Mphone.setGeometry(QtCore.QRect(130, 110, 113, 20))
        self.lineEdit_Mphone.setObjectName("lineEdit_Mphone")
        self.lineEdit_Mage = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_Mage.setGeometry(QtCore.QRect(410, 40, 113, 20))
        self.lineEdit_Mage.setObjectName("lineEdit_Mage")
        self.lineEdit_Musername = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_Musername.setGeometry(QtCore.QRect(410, 110, 113, 20))
        self.lineEdit_Musername.setObjectName("lineEdit_Musername")
        self.label_age = QtWidgets.QLabel(self.tab_3)
        self.label_age.setGeometry(QtCore.QRect(340, 40, 54, 12))
        self.label_age.setObjectName("label_age")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(60, 110, 54, 12))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(60, 180, 54, 12))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(340, 110, 54, 12))
        self.label_12.setObjectName("label_12")
        self.lineEdit_Mpwd = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_Mpwd.setGeometry(QtCore.QRect(130, 180, 113, 20))
        self.lineEdit_Mpwd.setObjectName("lineEdit_Mpwd")
        self.lineEdit_Mnewpwd = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_Mnewpwd.setGeometry(QtCore.QRect(410, 180, 113, 20))
        self.lineEdit_Mnewpwd.setObjectName("lineEdit_Mnewpwd")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(340, 180, 54, 12))
        self.label_13.setObjectName("label_13")
        self.pushButton_enter = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_enter.setGeometry(QtCore.QRect(200, 250, 75, 23))
        self.pushButton_enter.setObjectName("pushButton_enter")
        self.pushButton_cancel2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_cancel2.setGeometry(QtCore.QRect(370, 250, 75, 23))
        self.pushButton_cancel2.setObjectName("pushButton_cancel2")
        self.tabWidget.addTab(self.tab_3, "")
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
        self.pushButton_booksearch.clicked.connect(self.Serch_book)
        self.pushButton_bookchange.clicked.connect(self.Change_book)
        self.pushButton_bookadd.clicked.connect(self.Add_book)
        self.pushButton_usersearch.clicked.connect(self.Search_user)
        self.pushButton_userdelete.clicked.connect(self.Delete_user)
        self.pushButton_usergrant.clicked.connect(self.Grant)
        self.pushButton_enter.clicked.connect(self.Change)
        self.pushButton_cancel2.clicked.connect(self.Cancel)


        self.retranslateUi(mainWindow,user)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow,user):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "图书管理系统"))
        self.label.setText(_translate("mainWindow", "【管理员端】"))
        self.pushButton_exit.setText(_translate("mainWindow", "注销"))
        self.label_4.setText(_translate("mainWindow", "图书编号"))
        self.label_5.setText(_translate("mainWindow", "出版社"))
        self.label_6.setText(_translate("mainWindow", "书名"))
        self.label_7.setText(_translate("mainWindow", "作者"))
        self.pushButton_booksearch.setText(_translate("mainWindow", "查询"))
        self.checkBox_bno.setText(_translate("mainWindow", "图书编号"))
        self.checkBox_bname.setText(_translate("mainWindow", "书名"))
        self.checkBox_author.setText(_translate("mainWindow", "作者"))
        self.checkBox_press.setText(_translate("mainWindow", "出版社"))
        self.pushButton_bookadd.setText(_translate("mainWindow", "添加"))
        self.label_3.setText(_translate("mainWindow", "图书数量"))
        self.pushButton_bookchange.setText(_translate("mainWindow", "修改"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mainWindow", "图书管理"))
        self.pushButton_usersearch.setText(_translate("mainWindow", "用户查询"))
        self.pushButton_userdelete.setText(_translate("mainWindow", "用户删除"))
        self.pushButton_usergrant.setText(_translate("mainWindow", "用户授权"))
        self.checkBox_rno.setText(_translate("mainWindow", "学号"))
        self.checkBox_rname.setText(_translate("mainWindow", "姓名"))
        self.label_8.setText(_translate("mainWindow", "学生学号"))
        self.label_9.setText(_translate("mainWindow", "学生姓名"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mainWindow", "授权管理"))
        self.label_name.setText(_translate("mainWindow", "姓名"))
        self.label_age.setText(_translate("mainWindow", "年龄"))
        self.label_10.setText(_translate("mainWindow", "电话号码"))
        self.label_11.setText(_translate("mainWindow", "旧密码"))
        self.label_12.setText(_translate("mainWindow", "用户名"))
        self.label_13.setText(_translate("mainWindow", "新密码"))
        self.pushButton_enter.setText(_translate("mainWindow", "确定"))
        self.pushButton_cancel2.setText(_translate("mainWindow", "取消"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("mainWindow", "信息修改"))
        self.label_2.setText(_translate("mainWindow", "欢迎！"))
        self.label_username.setText(_translate("mainWindow", "用户名"))
        self.label_username.setText(_translate("mainWindow", user[5]))

        self.lineEdit_Mname.setText(_translate("mainWindow", user[1]))
        self.lineEdit_Mage.setText(_translate("mainWindow", str(user[3])))
        self.lineEdit_Musername.setText(_translate("mainWindow", user[5]))
        self.lineEdit_Mphone.setText(_translate("mainWindow", user[4]))

    def Win_exit(self):
        self.close()
        self.MainWindow.show()

    def Change(self):
        controller = Manager()
        oldusername = self.label_username.text()
        old = controller.Search_by_Username(oldusername)
        mno = old[0]
        name = self.lineEdit_Mname.text()
        age = self.lineEdit_Mage.text()
        phone = self.lineEdit_Mphone.text()
        uname = self.lineEdit_Musername.text()
        oldpwd = self.lineEdit_Mpwd.text()
        newpwd = self.lineEdit_Mnewpwd.text()
        user = []
        user.append(mno)
        user.append(name)
        user.append(age)
        user.append(phone)
        user.append(uname)
        user.append(newpwd)
        if oldpwd != old[6]:
            QMessageBox.warning(None, "警告", "原密码输入错误！", QMessageBox.Ok)
            self.lineEdit_Mpwd.setFocus()
        elif controller.Judge_Username(mno,uname):
            QMessageBox.warning(None, "警告", "该用户名已被使用", QMessageBox.Ok)
            self.lineEdit_Musername.setFocus()
        else:
            self.label_username.setText(uname)
            controller.Update(user)
            QMessageBox.information(None, "提示", "修改成功！", QMessageBox.Ok)
            self.lineEdit_Mpwd.setText('')
            self.lineEdit_Mnewpwd.setText('')

    def Cancel(self):
        controller = Manager()
        oldusername = self.label_username.text()
        user = controller.Search_by_Username(oldusername)
        self.lineEdit_Mname.setText(user[1])
        self.lineEdit_Mage.setText(str(user[3]))
        self.lineEdit_Musername.setText(user[5])
        self.lineEdit_Mphone.setText(user[4])
        self.lineEdit_Mpwd.setText('')
        self.lineEdit_Mnewpwd.setText('')

    def Serch_book(self):
        controller = Manager()
        bno = self.lineEdit_bno.text()
        bname = self.lineEdit_bname.text()
        bpress = self.lineEdit_press.text()
        author = self.lineEdit_author.text()
        sql = "select * from book where 1 "
        if (self.checkBox_bno.isChecked()
                or self.checkBox_author.isChecked()
                or self.checkBox_bname.isChecked()
                or self.checkBox_press.isChecked()):
            if (self.checkBox_bno.isChecked()):
                sql = sql + "and Bno = '" + bno + "'"
            if (self.checkBox_bname.isChecked()):
                sql = sql + "and Bname = '" + bname + "'"
            if (self.checkBox_author.isChecked()):
                sql = sql + "and Bauthor like '%" + author + "%'"   #作者可能有多个，所以采用模糊查询
            if (self.checkBox_press.isChecked()):
                sql = sql + "and Bpress = '" + bpress + "'"
        books = controller.Search(sql)
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

    def Change_book(self):
        book = Book()
        rownum = self.tableWidget.currentRow()
        if rownum < 0:
            QMessageBox.information(None, "提示", "请先选择一本书！", QMessageBox.Ok)
            return
        Bno = self.tableWidget.item(rownum, 0).text()
        newnum = self.lineEdit_booknum.text()
        if newnum == '':
            QMessageBox.information(None, "提示", "请填写修改后书本的数量", QMessageBox.Ok)
            return
        bookmsg = []
        bookmsg.append(Bno)
        bookmsg.append(newnum)
        book.Set_book_num(bookmsg)
        QMessageBox.information(None, "提示", "修改成功！", QMessageBox.Ok)
        num = newnum
        item = QTableWidgetItem(str(num))
        self.tableWidget.setItem(rownum, 4, item)

    def Add_book(self):
        book = Book()
        Bno = self.lineEdit_bno.text()
        Bname = self.lineEdit_bname.text()
        Bauthor = self.lineEdit_author.text()
        Bpress = self.lineEdit_press.text()
        Bnum = self.lineEdit_booknum.text()
        bookmsg = []
        bookmsg.append(Bno)
        bookmsg.append(Bname)
        bookmsg.append(Bauthor)
        bookmsg.append(Bpress)
        bookmsg.append(Bnum)
        if(Bno == '' or Bname == '' or Bauthor == '' or Bpress == '' or Bnum == ''):
            QMessageBox.information(None, "提示", "请将课本信息填写完整！", QMessageBox.Ok)
            return
        elif book.Check_bno(Bno):
            QMessageBox.information(None, "提示", "书本编号重复！", QMessageBox.Ok)
            return
        elif book.Insert_book(bookmsg):
            QMessageBox.information(None, "提示", "添加成功！", QMessageBox.Ok)
            return

    def Search_user(self):
        controller = Manager()
        Rno = self.lineEdit_rno.text()
        Rname = self.lineEdit_rname.text()
        sql = "select * from reader where 1 "
        if (self.checkBox_rno.isChecked()
                or self.checkBox_rname.isChecked()):
            if (self.checkBox_rno.isChecked()):
                sql = sql + "and Rno = '" + Rno + "'"
            if (self.checkBox_rname.isChecked()):
                sql = sql + "and Rname = '" + Rname + "'"
        users = controller.Search(sql)
        if users:
            self.tableWidget_2.setColumnCount(len(users[0]))
            self.tableWidget_2.setRowCount(len(users))
            self.tableWidget_2.setHorizontalHeaderLabels(['学号', '姓名', '性别', '年龄', '电话号码','用户名','密码'])
            for i in range(len(users)):
                for j in range(len(users[0])):
                    item = QTableWidgetItem(str(users[i][j]))
                    self.tableWidget_2.setItem(i, j, item)
        else:
            self.tableWidget_2.setColumnCount(0)
            self.tableWidget_2.setRowCount(0)
        return True

    def Delete_user(self):
        book = Book()
        reader = Reader()
        rownum = self.tableWidget_2.currentRow()
        if rownum < 0:
            QMessageBox.information(None, "提示", "请选择要删除的用户", QMessageBox.Ok)
            return
        rno = self.tableWidget_2.item(rownum,0).text()
        borrow = reader.Check_borrow(rno)
        if borrow:
            for i in range(len(borrow)):
                reader.Back(borrow[i][0],borrow[i][1])
                book.Add_book_num(borrow[i][1])
        if reader.Delete(rno):
            QMessageBox.information(None, "提示","用户删除成功！", QMessageBox.Ok)
            self.tableWidget_2.removeRow(rownum)
            return

    def Grant(self):
        controller = Manager()
        book = Book()
        reader = Reader()
        rownum = self.tableWidget_2.currentRow()
        if rownum < 0:
            QMessageBox.information(None, "提示", "请选择要授权的用户", QMessageBox.Ok)
            return
        rno = self.tableWidget_2.item(rownum,0).text()
        borrow = reader.Check_borrow(rno)
        if borrow:
            for i in range(len(borrow)):
                reader.Back(borrow[i][0],borrow[i][1])
                book.Add_book_num(borrow[i][1])
        user = reader.Search_by_Rno(rno)
        user1 = []
        user1.append(user[0])
        user1.append(user[1])
        user1.append(user[2])
        user1.append(user[3])
        user1.append(user[4])
        user1.append(user[0])
        user1.append(user[6])
        if reader.Delete(rno) and controller.Insert(user1):
            QMessageBox.information(None, "提示", "设置管理员成功！", QMessageBox.Ok)
            self.tableWidget_2.removeRow(rownum)
            return