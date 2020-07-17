import random

class array():

    def __init__(self, a, b, c, cho):
        self.a = a
        self.b = b
        self.c = c
        self.cho =cho

    #생성자 변수를 사용하기 위해서 기능을 만들어줌
    def abcprintf(self):
        content = [self.a, self.b, self.c]

        d= 0
        for i in content:
            d = d + i
        print(d)
        return d / len(content)
        #if self.cho == 0:
            #print("sum")
            #return d
        #elif self.cho == 1:
            #print("avg")
            #return d/len(content)

a = random.randint(1, 10)
b = random.randint(1, 10)
c = random.randint(1, 10)

F= array(a=a, b=b, c=c, cho=1).abcprintf()
print(F)

