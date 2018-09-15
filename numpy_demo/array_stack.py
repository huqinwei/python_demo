import numpy as np


A = np.array([1,1,1])
B = np.array([2,2,2])

print(np.vstack((A,B)))
print(np.hstack((A,B)))

print(A.shape)
print(A.T.shape)

print(A[np.newaxis,:])
print(A[np.newaxis,:].shape)
print(A[:,np.newaxis].shape)
#print(A[:,np.newaxis,:].shape)



A = np.array([1,1,1])[:,np.newaxis]
B = np.array([2,2,2])[:,np.newaxis]
print(A.shape)
print("A:",A)
print(B.shape)
print("B:",B)
C = np.vstack((A,B))
print("vstack:\n|\n|\n|\n",C.shape)
print("C:\n",C)
C = np.hstack((A,B))
print("hstack:------\n",C.shape)
print("C:\n",C)
C = np.hstack((A,B))

C = np.concatenate((A,B,B,A))
print('concatenate:',C)
C = np.concatenate((A,B,B,A),axis=1)
print(C)



