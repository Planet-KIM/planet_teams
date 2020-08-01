#랜덤배열(1,10)의 크기를 임의로 주고, 그 배열의 크기를 예처리로 맞추는것
import random

array = []
class raise_array :

    def __init__(self,array):
        self.array = array

    def raise_test(self):
        try:
            length = len(array)

            if (length != b):
                raise Exception("정답이 아닙니다.")

            else:
                print("정답입니다.")

        except Exception as e:
            print(e)


b = int(input('예상 값을 입력하세요.:'))
A = raise_array(array=array)

for i in range(random.randint(1, 10)):
    a= random.randint(1, 10)
    array.append(a)

print(array)




















