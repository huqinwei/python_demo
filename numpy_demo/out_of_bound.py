import numpy as np
x = np.arange(12)
print('x:',x)

x2 = np.reshape(x,(3,4))
print('x2:',x2)

x3 = x2[0:2,0:3]

print("x2[0:2,0:3]:",x3)

x4 = x2[0:3,0:4]
print("x2[0:3,0:4]:",x4)
print("shape:",x4.shape)

x5 = x2[0:4,0:5]
print("x2[0:4,0:5]:",x5)
print("shape:",x5.shape)

x6 = x2[0:100,0:100]
print("x2[0:100,0:100]:",x6)
print("shape:",x6.shape)

x7 = x2[2:100,2:100]
print("x2[2:100,2:100]:",x7)
print("shape:",x7.shape)


