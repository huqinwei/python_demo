import numpy as np
import copy

a = np.arange(12).reshape(3,4)
print("a:",a)
b = a
c = a
d = b

e = a.copy()
f = copy.copy(a)



a[0] = 9
a[1][:] = 8
a[2,:] = 7
#a[2,:] = 7,6,5 not allowed
a[2,:] = 7,6,5,4
a[0][2] = 99
print('change a')
print("a:\n",a)
print('shallow copy--b:\n',b)
print('shallow copy--c:\n',c)
print('shallow shallow copy--d:\n',d)



print("deep copy--e:\n",e)
print("another deep copy--f:\n",f)


