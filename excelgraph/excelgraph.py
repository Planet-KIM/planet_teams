from pandas import ExcelWriter
from openpyxl import load_workbook
import openpyxl
import pandas as pd
import numpy as np

content = np.random.randn(10, 6)
graph = pd.DataFrame(content, columns = ['5', '6', '7', '8', '9', '10'])
print(graph)

graph.to_excel(excel_writer ='graph.xlsx')
wb = openpyxl.load_workbook('graph.xlsx')

def nono(content):
    counta = 0
    for i in content:
        countb= 0
        for j in i:

            if 0 < [counta][countb]:
                content[counta][countb] = 1

            else:
                content[counta][countb] = 0

            countb = countb + 1
        counta = counta + 1
    return content
A = nono(content=content)

wbb = wb.creat_sheet('result')
