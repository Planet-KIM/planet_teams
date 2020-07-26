import matplotlib as mpl
import matplotlib.pylab as plt
import numpy as np

x = np.arange(1,10,0.1)
y = x*0.2
y2 = np.sin(x)

plt.plot(x,y,'b',label='first')
plt.plot(x,y2,'r',label='second')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('matplotlib sample')
plt.legend(loc='upper right')
plt.show()