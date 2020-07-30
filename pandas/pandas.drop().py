import pandas as pd
import numpy as np

array = pd.Series(np.arange(5.), index = ['a', 'b', 'c', 'd', 'e' ] )
newarray = array.drop('c')
print(array.drop(['d', 'c']))

