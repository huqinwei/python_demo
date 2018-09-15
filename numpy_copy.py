import numpy as np
import copy

a = np.arange(12).reshape(3,4)
print(a)
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
print(b)
print(c)
print(d)



print(e)
print(f)


