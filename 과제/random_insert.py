#배열을 만들고 넘겨주고, 그 배열에 랜덤수를 입력받는데 사용자가 범위와 횟수를 정하는 프로그램
#random 모듈 불러오
import random
#from 파일이름 import class 이름
from getdbb import cal
#randominsert 클래스생성
class randominsert():
    #생성자
    def __init__(self,arraycount):
        self.arraycount = arraycount
    #rinsert 기능 생성
    def rinsert(self, random1, range1):
        #range1입력값을 받아 1에서부터의 횟수를 정하는 for문
        for i in range(1, range1):
            #
            self.arraycount.append(random.randint(1,random1))
        #arraycount의 값을 return
        return self.arraycount
#arraycount라는 리스트 생성
arraycount = []
#a와 b의 값을 입력받기
a= int(input('random1: '))
b= int(input('range1 : '))
#class를 불러오고 array1 변수에 넣음
array1 = randominsert(arraycount=arraycount).rinsert(random1=a,range1 = b)
#array1 출력
print(array1)
#arraycal.arrayavg
cal = cal(array1)
#cal클래스에서 listavg기능을 가져오고 이를 출력
print(cal.listavg())


