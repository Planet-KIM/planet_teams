import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


array = []
array1 = []
array2 = []

array = np.random.randn(5, 5)
print(array)
df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D', 'E'])

count = 0
for i in array:
    count = count + 1
    if 0 < i:
        array[count] = 1
    else:
        array[count] = -1


print(array)


plt.title("random_signal")

plt.plot(df)
plt.show()



"""
count = 0
for i in array:
    count = count + 1

    if count < 6:
        array1.append(i)

    else:
        array2.append(i)

print(array1)
print(array2)
"""