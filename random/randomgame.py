#배열을 값을 랜덤값 10개 범위는 1에서 50 사용자에게 입력값을 받는데 기회는 3번/ 3개틀린거를 예외로하고 3개이상 틀렸습니다 출력
#맞을경우 입력받은 값출력하고 몇번맞았습니다.
import random

content = []

for i in range(10):
    a = random.randint(1, 50)
    content.append(a)

#무한루프
while(1):

    countA = 0
    countB = 0

    #content안의 요소를 하나씩 읽는다.
    for i in content:
        #질문을 정수로 받고 b라는 변수에 넣기
        b = int(input("예상되는 수를 입력하세요 : "))
        #요소가 입력값과 같을 조건
        if i == b:
            countA = countA + 1

        else:
            countB = countB + 1
            #countB가 4와같을 조건이면 정지
            if countB == 4:
                break
            #print("{}번 틀렸습니다".format(countB))

    #countB가 4일때의 예외처리
    try:
        if countB == 4:
            raise Exception("정답이 아닙니다.")

        else:
            print("{count}번 맞췄습니다.".format(count=countA))

    except Exception as e:
        print(e)
        break