#pymysql 모듈을 가져옴
import pymysql
#
from pymysql.err import DatabaseError

#getdb라는 클래스생성
class getdb:

    #생성자
    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    #dbconnect기능 생성
    def dbconnect(self):

        #예외명령어
        try:
            #mysql과 내컴퓨터와 연결을 하기위함
            conn = pymysql.connect(host=self.host, user=self.user, passwd=self.pwd, db=self.db)
            #cursor
            cur = conn.cursor()
            #eceucute insert into
            cur.execute("USE uiju")

        except DatabaseError:
            error = print("접속 에러")
        finally:
            print("접속 성공")
        return cur

    #selectAll 기능 생성
    def selectAll(self):
        cur = self.dbconnect()
        query = 'SELECT * FROM user'
        cur.execute(query)
        rows = cur.fetchall()
        return rows

#getdb 클래스 불러옴
cur = getdb(host="127.0.0.1", user="root", pwd="secret", db="mysql").selectAll()
#cur 출력
print(cur)
