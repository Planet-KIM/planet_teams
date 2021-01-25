import numpy as np
import pandas as pd
from openpyxl import Workbook
import openpyxl

A = np.random.randn(10,10)
graph = pd.DataFrame(A)
print(graph)
#graph.to_excel(excel_writer ='ptoe.xlsx')

#엑셀불러오기
df = pd.read_excel('ptoe.xlsx',sheet_name='Sheet1')

count = 0
newlist = []
for array in df.values:
    list = []
    for item in array:

        if count %11 == 0:
            count = count + 1
            continue

        if item < 0:
            item = 0
            #print(item)

        elif item > 0:
            item = 1
            #print(item)


        if count % 11 <= 10:
            list.append(item)

        count = count + 1

    newlist.append(list)

print(newlist)
"""
count = 0
for i in i
"""
#dfsheet = pd.DataFrame(df.values)

newlistdf = pd.DataFrame(newlist)
print(newlistdf)

wb = Workbook()
ws2 = wb.create_sheet()
wb.save()
newlistdf.to_excel(excel_writer ='ptoe.xlsx',sheet_name='sheet2')
#newlistdf.to_excel('ptoe.xlsx',sheet_name='Sheet2')



