import numpy as np
import copy
a = np.arange(2,14).reshape(3,4)
print(a)
print(type(a))
a = [1,2,[3,4]]
print(type(a))
print(type(a[0]))
print(type(a[1]))
print(type(a[2]))
b = a
c = copy.copy(a)
d = copy.deepcopy(a)

a[0] = 100
a[2][0] = 300


print('a:',a)
print('b(assign):',b)
print('c(copy:different memory,same value, pointer the same):',c)
print('d(deepcopy):',d)

a2 = [1,2,[3,[4,5]]]
e = copy.deepcopy(a2)
print('a2:\n',a2)
print('change a2')
a2[2][1][0] = 400
print('a2:\n',a2)
#print('a2 dim:\n',a2.shape)
print('e:',e)


