import random

arrayval = []
#count = 1

for i in range(10):
    a = random.randint(1,6)
    arrayval.append(a)
    #print(a)

for i in arrayval:
    print(i)
    if (i == 3):
        print("도둑입니다.")

#for i in arrayval:
    #print("{A}번 {B}입니다.".format(A = count, B = i ))
    #count = count + 1

#print("합계는 {A}입니다.".format(A = sum(arrayval)))
#for i in arrayval:

#print(random.randint(1,10))

#print(sum(arrayval))