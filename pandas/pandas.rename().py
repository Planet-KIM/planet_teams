import pandas as pd

df = pd.DataFrame({'$a': [1, 2], '$b': [10, 20]})
df.columns = ['a', 'b']
print(df)

df.rename(columns={'a': 'first', 'b': 'second'}, inplace=True)
print(df)
