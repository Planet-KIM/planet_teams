#for 문을 통해서 arrayval이라는 배열에 랜덤수를 10개등록 다만 이 랜덤수의 범위는 1에서 15까지 그리고 배열에 넣을 값의 범위는 7이상만 이상이면 7이상입니다, 아니면 7이하입니다.

import random

arrayval = []

while(1):

    a= random.randint(1,15)

    print(a)
    if (a > 7):

        print("7이상 입니다.")
        arrayval.append(a)

    else :
        print("7이하 입니다.")

    if (len(arrayval)>9) :
        break
print(arrayval)

