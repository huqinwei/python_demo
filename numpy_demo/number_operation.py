import numpy as np
a = np.array([10,20,30,40])
b = np.arange(4)
print(a,b)
c = b**2
print(c)
c = 10 * np.sin(a)
print(c)

print(b==3)


a = np.array([[1,1],[0,1]])
b = np.arange(4).reshape((2,2))
print('a:',a)
print('b:',b)

print(a*b)
print(np.dot(a,b))
print(a.dot(b))
print(b.dot(a))


a = np.random.random((2,4))
#a = np.random.random((2,4),seed = 12)
print(a)
print('sum:',np.sum(a))
print('axis=1:',np.sum(a,axis=1))
print('min:',np.min(a))
print('axis=0:',np.min(a,axis=0))
print('max:',np.max(a))
print('axis=1',np.max(a,axis=1))
print(np.mean(a))










