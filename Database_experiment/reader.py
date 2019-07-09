import pymysql
class Reader:
    #登录
    def Reader_login(self,user):
        conn = pymysql.connect("localhost", "root", "shuaipeng", "library")
        sql = "select * from reader where Ruser = '" + user[0] + "' and Rpassword = '" + user[1] + "'"
        cursor = conn.cursor()
        cursor.execute(sql)
        num = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        if num:
            return True
        else:
            return False
    #插入用户
    def Insert_user(self,user):
        conn = pymysql.connect("localhost", "root", "shuaipeng", "library")
        sql = "insert into reader(Rno,Rname,Rsex,Rage,Rphone,Ruser,Rpassword) values(%s,%s,%s,%s,%s,%s,%s)"
        cursor = conn.cursor()
        cursor.execute(sql,(user[0],user[1],user[2],user[3],user[4],user[5],user[6]))
        conn.commit()
        cursor.close()
        conn.close()
    #根据借阅证号查询读者信息
    def Search_by_Rno(self,rno):
        conn = pymysql.connect("localhost", "root", "shuaipeng", "library")
        sql = "select * from reader where Rno = '"+ rno + "'"
        cursor = conn.cursor()
        cursor.execute(sql)
        user = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return user
    # 根据用户名查询读者信息
    def Search_by_Username(self,username):
        conn = pymysql.connect("localhost", "root", "shuaipeng", "library")
        sql = "select * from reader where Ruser = '"+ username + "'"
        cursor = conn.cursor()
        cursor.execute(sql)
        user = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return user
    # 判断用户名是否被其他人使用
    def Judge_Username(self,Rno,username):
        conn = pymysql.connect("localhost", "root", "shuaipeng", "library")
        sql = "select * from reader where Ruser = '"+ username + "' and Rno != '"+ Rno + "'"
        cursor = conn.cursor()
        cursor.execute(sql)
        user = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return user
    #根据输入的sql语句查询
    def Search(self,sql):
        conn = pymysql.connect("localhost", "root", "shuaipeng", "library")
        cursor = conn.cursor()
        cursor.execute(sql)
        book = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return book
    #更新读者信息
    def Update(self,user):
        conn = pymysql.connect("localhost", "root", "shuaipeng", "library")
        cursor = conn.cursor()
        sql = "update reader " \
              "set Rname =  '" + user[1] + "'" \
              ",Rage = '" + user[2] +"'" \
              ",Rphone = '" + user[3] + "'" \
              ",Ruser = '" + user[4] + "'" \
              ",Rpassword = '" + user[5] + "'" \
              " where Rno = '" + user[0] + "'"
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    #借书
    def Borrow_book(self,b_book):
        conn = pymysql.connect("localhost", "root", "shuaipeng", "library")
        sql = "insert into borrow(Rno,Bno,Bstart,Bend) values(%s,%s,%s,%s)"
        cursor = conn.cursor()
        cursor.execute(sql,(b_book[0],b_book[1],b_book[2],b_book[3]))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    #判断用户是否借阅该书
    def Judge_bno(self,rno,bno):
        conn = pymysql.connect("localhost", "root", "shuaipeng", "library")
        sql = "select * from borrow where Bno = '"+ bno + "' and Rno = '"+ rno +"'"
        cursor = conn.cursor()
        cursor.execute(sql)
        user = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return user
    #查询用户的借阅记录
    def Borrow_record(self,rno):
        conn = pymysql.connect("localhost", "root", "shuaipeng", "library")
        sql = "select * from borrow where Rno = '"+ rno +"'"
        cursor = conn.cursor()
        cursor.execute(sql)
        user = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return user
    #还书
    def Back(self,rno,bno):
        conn = pymysql.connect("localhost", "root", "shuaipeng", "library")
        sql = " delete from borrow where Rno = '"+ rno +"' and Bno = '"+ bno +"'"
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    #根据图书编号查询借阅记录中的图书信息
    def Check_borrow(self,rno):
        conn = pymysql.connect("localhost", "root", "shuaipeng", "library")
        sql = "select * from borrow where Rno = '"+ rno + "'"
        cursor = conn.cursor()
        cursor.execute(sql)
        user = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return user
    #删除借阅记录
    def Delete(self,rno):
        conn = pymysql.connect("localhost", "root", "shuaipeng", "library")
        sql = " delete from reader where Rno = '"+ rno +"'"
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return True