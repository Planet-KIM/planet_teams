import numpy as np
import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as plt


#랜덤수 5*5만들기
A = np.random.randn(5,5)
print(A)

#0,1로 바꾸기

def Data(A):

    countA =0
    for i in A:

        countB = 0
        for j in i:

            if A[countA][countB] < 0:
                A[countA][countB] = 0

            else:
                A[countA][countB] = 1

            countB = countB + 1
        countA = countA + 1

    return A
D = Data(A=A)
print(D)
def graph(A):

    graph = pd.DataFrame(A)
    graph.to_excel(excel_writer='etog.xlsx',sheet_name='sheet1')

    df = pd.read_excel('etog.xlsx',sheet_name='sheet1')


    numA = [1, 2, 3, 4, 5]
    count = 221
    for i in range(4):
        plt.subplot(count)
        plt.plot(numA,df[i],"o-")

        count = count + 1

    plt.show()
 
graph(A=A)
