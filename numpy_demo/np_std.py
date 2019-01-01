#numpy.std
import numpy as np
a = np.array([[1,2],[3,4]])
a2 = np.array([[1,2],[10,16]])
print(a)
print(a.std())#1.118033988749895 # 1.1180339887498949
print(a.std(axis = 0))
print(np.std(a,axis = 0))#[1. 1.]
print(np.std(a,axis = 1))#[0.5 0.5]
print(np.std(a2,axis = 0))#[4.5 7. ]        [(10-1) / 2, (16-2) / 2]
print(np.std(a2,axis = 1))#[0.5 3. ]        [(2-1) / 2, (16-10) / 2]

a3 = np.zeros((2, 512*512), dtype = np.float32)
a3[0,:] = 1.0
a3[1,:] = .1
print(np.std(a3))
print(np.std(a3,dtype = np.float64))
