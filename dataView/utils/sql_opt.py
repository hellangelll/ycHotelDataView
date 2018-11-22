# -*- encoding:utf8 -*-
import sys
import psycopg2
import psycopg2.extras

reload(sys)
sys.setdefaultencoding("utf-8")


class SqlOpt:
    #获取数据库连接
    def getCon(self):
        try:
            conn=psycopg2.connect(database="hotel_local_db", user="postgres", password="angel", host="localhost", port="54321")
            return conn
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    def select(self,sql):
        try:
            con=self.getCon()
            cur=con.cursor(cursor_factory=psycopg2.extras.DictCursor)
            count=cur.execute(sql)
            # print(sql)
            fc=cur.fetchall()
            return fc
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()
            con.close()
    #带参数的更新方法,eg:sql='insert into pythontest values(%s,%s,%s,now()',params=(6,'C#','good book')
    def updateByParam(self,sql,params):
        try:
            con=self.getCon()
            cur=con.cursor(cursor_factory=psycopg2.extras.DictCursor)
            count=cur.execute(sql,params)
            con.commit()
            return count
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            con.rollback()
        finally:
            cur.close()
            con.close()
    #不带参数的更新方法
    def update(self,sql):
        try:
            con=self.getCon()
            cur=con.cursor(cursor_factory=psycopg2.extras.DictCursor)
            count=cur.execute(sql)
            con.commit()
            return count
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            con.rollback()
        finally:
            cur.close()
            con.close()
