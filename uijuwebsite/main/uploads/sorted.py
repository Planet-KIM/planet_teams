#배열에 랜덤수 총 10개를 넣고,그 배열을 class에 주면 작은 순서대로 정리해서 이를 보여줘라
#random모듈 가져오기
import random
#content라는 배열 만들기
content = []
#arrayval이라는 기능 생성
def arrayval(array):

    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

for i in range(10):
    a = random.randint(1,10)
    content.append(a)

print(content)

arrayval(array=content)
print(content)



