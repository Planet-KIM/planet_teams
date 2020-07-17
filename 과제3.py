#random 모듈을 가져오기
import random

#첫번째 배열에 고정 요소값으로 1,2,3을 넣음
contentA = [1, 2, 3]

contentB = [] #contentB 리스트 생성

for i in range(3): # 수의 범위를 3으로 지정
    a = random.randint(1,3) #1에서 3사이의 랜덤값을 추출
    contentB.append(a) #contenB 리스트에 요소 추가

print(contentA,contentB) #contentA와 conetentB를 출력

if (contentA == contentB): #contentA와 contentB가 같을 경우 해당 문장이 출력될 수 있도록 하는 조건문
    print("로또 당첨입니다.")

else : #contentA와 contentB가 같을 않을 경우 해당 문장이 출력될 수 있도록 하는 조건문
    print("로또 당첨 실패입니다.")