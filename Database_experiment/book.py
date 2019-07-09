import pymysql
class Book:
    #得到图书的剩余数量
    def Get_book_num(self,bno):
        conn = pymysql.connect("localhost", "root", "shuaipeng", "library")
        sql = "select * from book where Bno = '"+ bno + "'"
        cursor = conn.cursor()
        cursor.execute(sql)
        user = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return user[4]
    #图书数量减一
    def Sub_book_num(self,bno):
        conn = pymysql.connect("localhost", "root", "shuaipeng", "library")
        cursor = conn.cursor()
        sql = "update book set Bnum = Bnum - 1 where Bno = '" + bno + "'"
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    #图书数量加一
    def Add_book_num(self,bno):
        conn = pymysql.connect("localhost", "root", "shuaipeng", "library")
        cursor = conn.cursor()
        sql = "update book set Bnum = Bnum + 1 where Bno = '" + bno + "'"
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    #设置图书数量
    def Set_book_num(self,book):
        conn = pymysql.connect("localhost", "root", "shuaipeng", "library")
        cursor = conn.cursor()
        sql = "update book set Bnum = '"+book[1] + "' where Bno = '" + book[0] + "'"
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    #用图书编号得到图书的所有信息
    def Check_bno(self,bno):
        conn = pymysql.connect("localhost", "root", "shuaipeng", "library")
        sql = "select * from book where Bno = '"+ bno + "'"
        cursor = conn.cursor()
        cursor.execute(sql)
        user = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return user
    #插入图书
    def Insert_book(self,book):
        conn = pymysql.connect("localhost", "root", "shuaipeng", "library")
        sql = "insert into book(Bno,Bname,Bauthor,Bpress,Bnum)" \
              " values(%s,%s,%s,%s,%s)"
        cursor = conn.cursor()
        cursor.execute(sql,(book[0],book[1],book[2],book[3],book[4]))
        conn.commit()
        cursor.close()
        conn.close()
        return True
