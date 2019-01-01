import numpy as np
a = np.array([1,2,3,4])
import time
a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()
c = np.dot(a,b)
toc = time.time()
print('vectorized vesion:' + str(1000*(toc-tic)) + 'ms')

c = 0
tic = time.time()
for i in range(1000000):
    c += a[i] * b[i]
toc = time.time()
print('non-vectorized vesion:' + str(1000*(toc-tic)) + 'ms')




A = np.array([[56.0,0.0,4.4,68.0],
              [1.2,104.0,52.0,8.0],
              [1.8,135.0,99.0,0.9]])
print(A.sum())
print(A.sum(axis=0))
print(A.sum(axis=1))
print(A[0] / A.sum(axis=0))
cal = A.sum(axis=0)
print(100 * A/cal)
print(100 * A/cal.reshape(1,4))











