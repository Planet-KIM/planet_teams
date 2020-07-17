import random

class arraycal:

    def __init__(self, array):
        self.array= array


    def arraysum(self):
        
        cal = 0
        for item in self.array:
            cal = cal + item
        
        print('합계 : {}'.format(cal))
        return cal

    def arrayavg(self):

        calsum = self.arraysum()
        calavg = calsum / len(self.array)

        print('평균 : {}'.format(calavg))
        return calavg
"""
# This is test version #
arrayval = []
for i in range(3):
    a = random.randint(1, 10)
    arrayval.append(a)

print(arrayval)

arraycal = arraycal(array=arrayval)
arraycal.arrayavg()
"""        
