#랜덤수 10개 , 2배열은 배열중에 큰수 5 3배열은 12345 2,3 상관분석
import random
import numpy as np

contentA = []
for i in range(100):
    a = random.randint(1, 100)
    contentA.append(a)

print(contentA)

contentB = []

for i in range(len(contentA)):
    for j in range(len(contentA) - 1):
        if contentA[j] < contentA[j + 1]:
            contentA[j], contentA[j + 1] = contentA[j + 1], contentA[j]


for i in contentA:
    contentB.append(i)

    if len(contentB) == 5:
        break

print(contentB)


contentC =[]
for i in range(100):
    if len(contentC) == 100:
        break
    contentC.append(i)
print(contentC)

print(np.corrcoef(contentC, contentA))


