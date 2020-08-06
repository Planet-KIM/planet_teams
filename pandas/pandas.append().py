import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D '])
print(df)
s = df.iloc[3]
print(df.append(s, ignore_index = True))
