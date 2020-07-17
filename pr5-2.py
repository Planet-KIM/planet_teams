import random
from cal import cal

arrayval = []

while(1):

    a= random.randint(1,15)

    print(a)
    if (a > 7):

        print("7이상 입니다.")
        arrayval.append(a)

    else :
        print("7이하 입니다.")

    if (len(arrayval)>9) :
        break

cal = cal(arrayval)
print(cal.custom_sum())
