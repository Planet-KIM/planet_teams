import random

array = []
class custom_array:

    def __init__(self, array):

        self.array = array


    def arraysum(self):

        d = 0
        for i in self.array:
            d = d + i

        print(d)

    def arraygob(self):

        d = 1
        for i in self.array:
            d = d * i

        print(d)

for i in range(10):
    a = random.randint(1, 10)
    array.append(a)

try:
    length = len(array)
    print('length : ', length)
    if(length != 9):
        raise Exception("array length not 10")

except Exception as e:
    print(e)


print(array)
c = custom_array(array=array)

c.arraysum()
c.arraygob()