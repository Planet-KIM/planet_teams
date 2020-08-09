import pymysql
from pymysql.err import DatabaseError, MySQLError
import os
from bcrypt import *

#Planetdb 클래스 생성
class Planetdb:

    #고정값
    UIJU_HOST = '34.64.72.197'
    UIJU_USER = 'root'
    UIJU_PWD = 'secret'
    UIJU_DB = 'uijuweb'

    #생성자
    def __init__(self,host = UIJU_HOST, user = UIJU_USER, password = UIJU_PWD, database = UIJU_DB):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    #dbconnect 기능을 생성
    def dbconnect(self):

        #예외명령어 사용
        try:
            conn = pymysql.connect(host = self.host, user = self.user, passwd = self.password, db = self.database)

        #에러가 발생할 시 해당문구 출력
        except MySQLError as error:
            print("Find this Error : {}".format(error))
            return error

        except DatabaseError as error:
            print("Find this Error : {}".format(error))
            return error

        #연결 성공 시 해당문구 출력
        finally:
            print("Databases Connect Success!!!")
            print("Databases is {}".format(self.database))
            return conn

    #dbcursor 기능 생성
    def dbcursor(self):
        conn = self.dbconnect()
        cur = conn.cursor()

        print("Make the cursor used in Pymysql Module")
        return cur

#planetqurey클래스 생성
class Planetquery:

    #생성자
    def __init__(self, conn=Planetdb().dbconnect()):

        self.conn = conn

    #qureyData_All 기능 생성
    def qureyData_All(self, query):
        cur = self.conn.cursor()
        #query문장을  db서버에 전송
        cur.execute(query)

        #fetchall의 메소드 사용하여 데이터를 서버로부터 가져옴
        rows = cur.fetchall()
        return rows

    #selectAll 기능 생성
    def selectAll(self, table):

        #query문 실행
        query = "SELECT * FROM {}".format(table)

        rows = self.queryData(query = query)

        count = 1
        for item in rows :
            #count.row(item)출력
            print("{count}. row : {item}".format(count=count, item = item))
            count = count + 1

