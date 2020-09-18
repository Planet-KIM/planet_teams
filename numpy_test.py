#numpy 를 가지고 2차원 배열만드는데 000 001 011 111이걸 각각하고 배열 2차원으로 만들고
import numpy as np

array1 = [0, 0, 0]
array2 = [0, 0, 1]
array3 = [0, 1, 0]
array4 = [1, 0, 0]
array5 = [0, 1, 1]
array6 = [1, 0, 1]
array7 = [1, 1, 0]
array8 = [1, 1, 1]

array = np.array([array1, array2, array3, array4, array5, array6, array7, array8])
print(array)


count = 2

for i in array:
    bcd = []
    for j in i:

        if j == 1:
            bcd.append(2 ** count)

            print(bcd)

        count = count-1

        if count == 0:
            break

    #print(sum(bcd))



