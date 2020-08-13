import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
array = np.random.randn(10, 5)

print(array)
df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D', 'E'])
print(df)

def nono(array):
    counta = 0
    for i in array:
        countb = 0
        for j in i:

            if 0 < array[counta][countb]:
                array[counta][countb] = 1

            else:
                array[counta][countb] = 0

            countb= countb + 1
        counta= counta + 1
    return array
content = nono(array=array)

#0,1만든걸 mat로 신호로 그리기 한 리스트마다. 한배열에 0과 1이 몇개있는지 출력

array1 = [1, 2, 3, 4, 5]
"""
def customscatter(x, y):
    plt
"""

plt.scatter(array1, array[0])
plt.show()
plt.scatter(array1, array[1])
plt.show()
plt.scatter(array1, array[2])
plt.show()
plt.scatter(array1, array[3])
plt.show()

#plt그래프 분할로 보기
def counter(array):

    for i in array:
        counta = 0
        countb = 0
        for j in i:
            if j == 0:
                counta = counta + 1

            else:
                countb = countb + 1

        print(counta, " ",countb)

counter(array=array)
