# 클래스 만들고, sum이랑 곱하는 함수를 만들고 리스트를 변수로 생성

import random

array = []

class cal:

    def __init__(self, array):


        if not array:
            for i in range(0,10):
                R = random.randint(1, 10)
                array.append(R)


        self.array = array

    def __repr__(self):
        return "{array}입니다.".format(array = self.array)

    def half(self):
        array1 = []
        array2 = []

        count = 0

        for i in self.array:
            count = count + 1
            if count < 6:
                array1.append(i)
            else:
                array2.append(i)

        print(array)
        print(array1)
        print(array2)
        return array1, array2

    def sum(self):
        array1 = self.half()

        A = 0
        for i in array1:
            A = A + i

        print("각 요소의 합은 {A}입니다.".format(A=A))

    def gob(self):
        array2 = self.half()

        B = 0
        for i in array2:
            B = B * i

        print("각 요소의 곱은 {B}입니다.".format(B=B))

    def complex(self):




cal(array=array).half()
