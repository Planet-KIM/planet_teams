#def 있을 때
import numpy as np
import random
import matplotlib as mpl
import matplotlib.pylab as plt
import time

array = np.random.randn(5,5)

print(array)

def graph(array):
    newarray = []
    #array 배열 수 세주기
    count = 0
    for i in array:
        for j in i:
            count = count + 1

    print(count)


    for i in range(5):
        r = random.randint(1,count)
        counta = 0

        for A in array:
            for B in A:

                if r == counta:
                    newarray.append(B)
                counta = counta + 1

    print(newarray)
    return newarray

new = graph(array=array)

def matplot(newarray):

    plt.plot(newarray)
    plt.show()
matplot(newarray=new)


start = time.time()

print("time:", time.time()-start)






