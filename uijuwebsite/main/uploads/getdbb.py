#배열을 넣어서 합을 내주는 메소드와 평균을 내주는 메소드를 만든다.
import random

class cal():

    def __init__ (self, arraycal):
        self.arraycal = arraycal

    def listsum(self):
        sum = 0

        for i in self.arraycal:
            sum = sum + i

        return sum

    def listavg(self):

        return self.listsum() / len(self.arraycal)
"""
arraycal = []
for i in range(3):
    a=random.randint(1,10)
    arraycal.append(a)
print(arraycal)

cal = cal(arraycal = arraycal)
print(cal.listsum())
print(cal.listavg())"""
