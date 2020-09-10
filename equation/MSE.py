import numpy as np

def numerical_diff(f,x):
    h = np.float32(10e-50)
    print(h)

    return (f(x+h)-f(x-h))/2*h

def mean_square_error(y,t):

    return ((y-t)**2).mean()

def cross_entropy_error(y,t):

    if y.ndim == 1:
        y = y.reshape(1, y.size)
        t = t.reshape(1, t.size)
        print(" y format : {y}, t format : {t}".format(y=y,t=t))

    delta = 1e-7

    return -np.sum(np.log(y + delta) * t)/y.shape[0]

y = [0.15, 0.30, 0.45]
t = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
s = []

for i in range(len(t)):
    s.append(mean_square_error(np.array(y), np.array(t[i])))

print(s)
print("np.min(s) = {}".format(np.min(s)))
print("np.argmin(s) = {}".format(np.argmin(s)))
print("np.max(s) = {}".format(np.max(s)))
print("np.argmax(s) = {}".format(np.argmax(s)))

print("------------------------------------")

s = []

for i in range(len(t)):
    s.append(cross_entropy_error(np.array(y), np.array(t[i])))

print(s)
print("np.min(s) = {}".format(np.min(s)))
print("np.argmin(s) = {}".format(np.argmin(s)))
print("np.max(s) = {}".format(np.max(s)))
print("np.argmax(s) = {}".format(np.argmax(s)))