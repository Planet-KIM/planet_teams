#텍스트파이라 txt파일을 오픈하고 0,1울 카운트 바꾸고 데이터프레임으로 바꾸ㅗ 엑셀로 보내기
import pandas as pd
import numpy as np

f = open("C:/temp/python/planet_teams/fileread/test.txt","r")
lines = f.readlines()
content = []

for i in lines:
    A = list(i)
    for j in A:
        content.append(j.strip())

print(content)

#하나씩 뽑아
#print(content)