#text생성하는 textfile을 만들고 hello world을 출력하고 저장
#리스트에 각각 요소들을 담아서 출력
from openpyxl import load_workbook
from pandas import ExcelWriter
import openpyxl

#file.txt파일 생성
f = open("C:/temp/python/planet_teams/file/file.txt",'w')
A = "hello world"
f.write(A)
f.close()

#txt파일 읽어오기
f1 = open("C:/temp/python/planet_teams/file/file.txt",'r')
line = f1.readline()
B = list(line)

#excel파일 불러오기
wb = openpyxl.load_workbook('file.xlsx')
S = wb.active

S['A1']=B[0]
S['B1']=B[1]
S['C1']=B[2]
S['D1']=B[3]
S['E1']=B[4]
S['F1']=B[5]
S['G1']=B[6]
S['H1']=B[7]
S['I1']=B[8]
S['J1']=B[9]
S['K1']=B[10]

wb.save('file.xlsx')
wb.close()


