import numpy as np

A = np.arange(12).reshape(3,4)

print(A)

print(np.split(A,2,axis = 1))
print('array_split:',np.array_split(A,3,axis=1))
print(np.split(A,(1,2),axis = 1))
print('split 1,2,1:',np.split(A,(1,2,1),axis = 1))
#print(np.split(A,2,axis = 0))#not allowed
print(np.vsplit(A,3))
print(np.hsplit(A,2))


B = np.arange(12).reshape(4,3)
print(np.split(B,2,axis = 0))




