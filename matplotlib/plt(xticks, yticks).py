import matplotlib as mpl
import matplotlib.pylab as plt

plt.figure()
plt.plot([1, 2, 3], [1, 2, 3])
plt.xticks([1, 2, 3])
plt.yticks([1, 2, 3])
plt.show()

"""
문자일경우
import matplotlib as mpl
import matplotlib.pylab as plt

plt.figure()
plt.plot([1, 2, 3], [1, 2, 3])
plt.xticks([1, 2, 3],['Mon', 'Tue', 'Wed'])
plt.yticks([1, 2, 3],['January', 'February', 'March'])
plt.show()
"""