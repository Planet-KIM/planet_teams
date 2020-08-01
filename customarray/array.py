#랜덤수 10개 , 2배열은 배열중에 큰수 5 3배열은 12345 2,3 상관분석
import random
import numpy as np

contentA = []
for i in range(10):
    a = random.randint(1, 10)
    contentA.append(a)

print(contentA)

contentB = []

for i in range(len(contentA)):
    for j in range(len(contentA) - 1):
        if contentA[j] > contentA[j + 1]:
            contentA[j], contentA[j + 1] = contentA[j + 1], contentA[j]


        if len(contentB[j]) < 6:
            break



