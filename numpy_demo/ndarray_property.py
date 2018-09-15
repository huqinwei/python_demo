import numpy as np


#print np.zeros((3,4))
#print np.ones((3,4))
#print("np.twos((3,4)):",np.twos((3,4)))#error no api
print("np.eye(3):",np.eye(3))
print("np.zeros((3,4,5)):",np.zeros((3,4,5)))

a = np.zeros((2,2,2),dtype = np.int32)
print("a:\n",a)
print("a.ndim:",a.ndim)

print("a.shape:",a.shape)

print("a.size:",a.size)

print("a.dtype:",a.dtype)

print("a.itemsize:",a.itemsize)








