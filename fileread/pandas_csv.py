#판다스로 np10*10 랜덤수 배열해서 채워넣고 거기서 최댓값과 최솟값을 찾아서 사용자가 입력받은 값이랑 그값보다 크면 정답입니다. 크다 둘다작으면raise
import numpy as np
import pandas as pd
import os

pth = os.path.dirname(os.path.realpath(__file__))

A = int(input("최댓값을 입력하세요: "))
B = int(input("최솟값을 입력하세요: "))

array = np.random.randn(10, 10)

max = np.max(array)
min = np.min(array)
print(array)
print(max)
print(min)

try:
    if max <= A and min >= B:
        print("정답입니다.")
    else:
        raise Exception ("정답이 아닙니다.")

except Exception as e:
    print(e)

excel = pd.DataFrame(array)
excel.to_excel(excel_writer = os.path.join(pth,'pandas_excel.xlsx') )


