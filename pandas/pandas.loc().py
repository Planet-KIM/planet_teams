import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(10, 22).reshape(3,4), index = ["a", "b", "c"], columns = ["A", "B", "C", "D"])
print(df)


print(df.loc["a"])