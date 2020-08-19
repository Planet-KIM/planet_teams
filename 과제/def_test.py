#변수를 3개로 받고 그 변수를 피타고라스의 정리로 만들기
#a^2+b^2=c^2을 증명

class math():

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def abcprintf(self):
        d = (self.a ** 2) +(self.b ** 2)
        print(d)
        c = self.c ** 2
        print(c)

        if (d==c):
            print("피타고라스 정리가 가능합니다.")
        else :
            print("아니오.")



import random
c = random.randint(1,6)
math(a=3,b=4,c=c).abcprintf()


"""
    if a ** 2 + b ** 2 == c**2:
        print ("피타고라스 정리가 가능합니다.")

    else :
        print("아니오.")"""



