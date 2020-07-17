import pymysql
from pymysql.err import DatabaseError, MySQLError
import os 

class planetdb:

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    # Connect를 생성해주고 해당 부분에 대한
    # 예외처리를 해주는 부분입니다.
    def dbconnect(self):
        try:
            conn = pymysql.connect(
                    host=self.host,
                    user=self.user,
                    passwd=self.password,
                    db=self.database
                    )
            #cur = conn.cursor()
            #cur.execute("USE Planetweb")

        except MySQLError as error:
            print("Find this Error : {}".format(error))
            return error
        
        except DatabaseError as error:
            print("Find this Error : {}".format(error))
            return error
        
        finally:
            print("Database Connect Success!!!")

        return conn

    def dbcursor(self):
        conn = self.dbconnect()
        cur = conn.cursor()
        
        print("Make the cursor used in Pymysql Module")
        return cur


####### This is test version #######
cur = planetdb(host="127.0.0.1", 
        user="root",
        password="secret",
        database="mysql").dbcursor()
