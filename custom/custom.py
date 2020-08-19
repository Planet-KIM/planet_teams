#랜덤(1~10)값을 10개 넣은 한 배열을 만들기 그 배열안에 각 숫자의 갯수를 카운트, 중복인 것을 한개로 만들어 출력

import random

content = []
for i in range(10):
    A = random.randint(1,10)
    content.append(A)
print(content)

for i in range(1,11):
    count = 0
    for j in content:
        if j == i:
            count = count+1

    print("{number}는 {count}개 입니다.".format(number = i, count=count))

    #위랑 의미는 같은 카운트지만 새로만들어줘야 함


for i in range(1,11):
    count = 0
    for j in content:
        if j == i:
            count = count + 1
        if count >= 2:
            del content[i]
#for i ing content 하나만 만들고 인덱스 새로운 것을 만들어주기
print(content)