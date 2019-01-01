import numpy as np

a = np.arange(0,40,10)[:,np.newaxis]


# print(a)
# #a = np.tile(a,(3,))
# a = np.tile(a,(3,1))
# print(a)
# print(a.T)


# [[ 0,  0,  0],
#        [10, 10, 10],
#        [20, 20, 20],
#        [30, 30, 30]]

# a = np.tile(np.arange(0, 40, 10), (3, 1)).T
print(a)

b = np.array([0, 1, 2])
c = a + b
print(a.shape)#(4,1)
print(b.shape)#(3,)
print(c)
print(c.shape)#(4,3)
# array([[ 0,  1,  2],
#        [10, 11, 12],
#        [20, 21, 22],
#        [30, 31, 32]])
