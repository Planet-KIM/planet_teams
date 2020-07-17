def bubblesort(array):

    arraylen = len(array)

    for i in range(arraylen):
        for j in range(arraylen-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

import random

randomarray = []
for item in range(10):
    randomarray.append(random.randint(1, 10))

print("정리 전 배열 : ", randomarray)

bubblesort(array=randomarray)
print("정리 후 배열 : ", randomarray)    
