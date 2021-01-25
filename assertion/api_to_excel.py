import pandas as pd
import json, openpyxl

def save(df, filename):
    writer = pd.excelWriter(filename)
    df.to_excel(writer, "sheet1")
    writer.save()

df =  pd.read_json("./nonPayment.json")
print(df.count())

save(df, "nonPayment.xlsx")
