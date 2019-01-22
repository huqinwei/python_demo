import numpy as np

A = np.arange(12).reshape(3,4)

print("A:",A)
print('array_split to 2:\n',np.split(A,2,axis = 1))
print('array_split to 3:\n',np.array_split(A,3,axis=1))
print(np.split(A,(1,2),axis = 1))
print('split to 1,2,1:\n',np.split(A,(1,2,1),axis = 1))
#print(np.split(A,2,axis = 0))#not allowed
print(np.vsplit(A,3))
print(np.hsplit(A,2))


B = np.arange(12).reshape(4,3)
print(np.split(B,2,axis = 0))




