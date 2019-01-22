import numpy as np

a = np.array([[1,2,3],[4,5,6]])
#a = np.array([1,2,3],dtype=np.float64)
#a = np.array([1,2,3],dtype=np.float128)
#a = np.array([1,2,3])
print(type(a))
print(a.dtype)
print(a)


z = np.zeros((3,4))
print(z)

o = np.ones((4,4),dtype=np.float16)
print(o)

#e = np.empty((3,4))
e = np.empty((3,4))
print(e)


#ar = np.arange(12).reshape(3,4)
ar = np.arange(0,12).reshape(3,4)
print(ar)
print("ndim:",ar.ndim)
ar = ar.reshape(1,3,4)
print(ar)
print("ndim:",ar.ndim)


lin = np.linspace(1,10,5)
print(lin)

lin = np.linspace(1,10,5,endpoint=False)
print(lin)


A = np.arange(12).reshape(3,4)
print("A:",A)
print(np.diff(A))
print(A.T)
print(np.transpose(A))
print(np.clip(A,5,9))
print(np.nonzero(A))

