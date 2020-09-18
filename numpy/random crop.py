import numpy as np
import time
import os


A = np.random.randn(5,5)


counta = 0

for i in A:
    countb = 0
    for j in i:

        if 0 < A[counta][countb]:
            A[counta][countb] = 1

        else:
            A[counta][countb] = 0

        countb = countb + 1
    counta = counta + 1


print(A)
start = time.time()


print("time:", time.time()-start)

