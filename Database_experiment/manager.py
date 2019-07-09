import pymysql
class Manager:
    #登录
    def Manager_login(self,user):
        conn = pymysql.connect("localhost", "root", "shuaipeng", "library")
        sql = "select * from manager " \
              "where Muser = '" + user[0] + "' " \
              "and Mpassword = '" + user[1] + "'"
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
    #根据用户名查询管理员信息
    def Search_by_Username(self,username):
        conn = pymysql.connect("localhost", "root", "shuaipeng", "library")
        sql = "select * from manager where Muser = '"+ username + "'"
        cursor = conn.cursor()
        cursor.execute(sql)
        user = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return user
    #判断用户名是否被使用
    def Judge_Username(self,mno,username):
        conn = pymysql.connect("localhost", "root", "shuaipeng", "library")
        sql = "select * from manager where Muser = '"+ username + "' and Mno != '"+ mno + "'"
        cursor = conn.cursor()
        cursor.execute(sql)
        user = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return user
    #修改个人信息
    def Update(self,user):
        conn = pymysql.connect("localhost", "root", "shuaipeng", "library")
        cursor = conn.cursor()
        sql = "update manager " \
              "set Mname =  '" + user[1] + "'" \
              ",Mage = '" + user[2] +"'" \
              ",Mphone = '" + user[3] + "'" \
              ",Muser = '" + user[4] + "'" \
              ",Mpassword = '" + user[5] + "'" \
              " where Mno = '" + user[0] + "'"
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    #根据传入的sql语句进行查询
    def Search(self,sql):
        conn = pymysql.connect("localhost", "root", "shuaipeng", "library")
        cursor = conn.cursor()
        cursor.execute(sql)
        book = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return book
    #插入新用户
    def Insert(self,user):
        conn = pymysql.connect("localhost", "root", "shuaipeng", "library")
        sql = "insert into manager(Mno,Mname,Msex,Mage,Mphone,Muser,Mpassword)" \
              " values(%s,%s,%s,%s,%s,%s,%s)"
        cursor = conn.cursor()
        cursor.execute(sql,(user[0],user[1],user[2],user[3],user[4],user[5],user[6]))
        conn.commit()
        cursor.close()
        conn.close()
        return True