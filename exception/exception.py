#함수로 만들어/길이를 맞추는 함수 / 배열길이를 랜덤으로(1,6)/길이 맞추면 맞춘걸 리턴/틀리면 예외처리 발생, 에러구문을 리턴
import random

content = []
for i in range(random.randint(1,10)):
    A= random.randint(1,10)
    content.append(i)
print(content)

B = int(input("수를 입력하세요 : "))

def array(content):
    try:
        if len(content) == B:
            print(B)
            return B

        else:
            raise Exception("틀렸습니다.")

    except Exception as e:
        print(e)
        return e

array(content = content)