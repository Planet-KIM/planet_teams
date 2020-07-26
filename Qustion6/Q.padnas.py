import pandas as pd

values = [['영어', '수학', '체육', '미술', '과학'], ['과학', '영어', '체육', '미술', '국어'], ['국어', '과학', '컴퓨터', '수학', '과학']]
index = [['1교시', '2교시', '3교시']]
columns = ['월요일', '화요일', '수요일', '목요일', '금요일']

df = pd.DataFrame(values, index=index, columns=columns)
print(df)
