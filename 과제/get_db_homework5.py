#pymysql 모듈을 가져옴
import pymysql
#DatabaseError라는 모듈을 가져옴
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

        except DatabaseError:
            error = print("접속 에러")

        finally:
            print("접속 성공")
        #conn을 return시킴
        return conn

#해당 class를 불러온다.
conn = getdb(host="127.0.0.1", user="root", pwd="secret", db="mysql").dbconnect()
#커서 객체를 생성
cur = conn.cursor()
#execute()메소드를 호출하여 sql 명령 수행
cur.execute("USE uiju")
#insert문을 sql이라는 변수에 넣는다
sql = """insert into user(name, email, pwd) values(%s,%s, %s)"""
#값을 입력받아 sql 실행
cur.execute(sql, ('박의주', 'dmlwn@naver.com','부산'))
#commit을 날려준다 -commit을 날리지 않으면 execute()를 아무리 해도 결과가 반영되지 않음
conn.commit()
