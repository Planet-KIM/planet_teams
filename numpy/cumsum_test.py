import numpy as np

a = int(input("누적값을 계산 할 시작 수를 입력해주세요:"))
b = int(input("누적값을 계산 할 마지막 수를 입력해주세요:"))

def pluscal(a, b):

    array = np.arange(a, b+1)
    print("생성된 리스트 : {array}".format(array = array))

    arraycal = np.cumsum(array)
    print("계산된 값 : {arraycal}".format(arraycal = arraycal))

pluscal(a=a, b=b)