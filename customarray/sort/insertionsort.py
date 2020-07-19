
def insertionsort(array):
    
    for item in range(1, len(array)):

        index = item - 1

        key = array[item]

        while((array[index] > key) and (index >= 0)):
            
            array[index + 1] = array[index]

            index = index - 1

        array[index + 1] = key

    return array

import random

array = []

for item in range(1, 10):
    array.append(random.randint(1, 10))

print("정렬 전 : ", array)

print("정렬 후 : ", insertionsort(array))


