#배열에 랜덤값1,에서 10, 배열의 크기는 15def , class이배열을 변수로 받아서 sorted를 해주고 (정렬-내림차순),짝수와 홀수를 출력하고 이를 각각 배열에 넣기, 이를 반환시켜주기
#이 두 배열을 메소드로 받아서 짝수배열의 길이가 더 크면 except가 뜨겜만들기
import random


def first():
    contentA = []
    for i in range(15):
        a = random.randint(1, 10)
        contentA.append(a)

    return contentA

contentA = first()
print(contentA)

def second(contentA):
    for i in range(len(contentA)):
        for j in range(len(contentA) - 1):
            if contentA[j] < contentA[j + 1]:
                contentA[j], contentA[j + 1] = contentA[j + 1], contentA[j]

second(contentA)

print(contentA)

contentB = []
contentC = []

for i in contentA:
    if i % 2 == 0:
        contentB.append(i)

    else:
        contentC.append(i)

print(contentB)
print(contentC)

try:

    if len(contentB) > len(contentC):
        raise Exception ("짝수가 더 깁니다.")

except Exception as e:
    print(e)



