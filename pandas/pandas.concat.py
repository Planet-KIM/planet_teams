import pandas as pd

s1 = pd.Series([0, 1], index=['A', 'B'])
s2 = pd.Series([2, 3, 4], index=['A', 'B', 'C'])
print(s1)
print(s2)
print(pd.concat([s1, s2]))