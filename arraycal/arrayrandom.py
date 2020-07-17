import random
from arraycal import arraycal

class randominsert:

    def __init__(self, array):
        self.array = array


    def rinsert(self, random1, range1):

        for item in range(1, range1):
            
            self.array.append(random.randint(1, random1))

        return self.array

array = []
a = int(input('random1 : '))
b = int(input('range1  : '))

array1 = randominsert(array=array).rinsert(random1=a, range1=b)
print(array1) 
arraycal = arraycal(array1)

arraycal.arrayavg()
