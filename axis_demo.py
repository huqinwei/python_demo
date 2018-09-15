import numpy as np

a = np.array([[[1,2,3,2],[1,2,3,1],[2,3,4,1]],[[1,0,2,0],[2,1,2,0],[2,1,1,1]]])
print(a)


print('a dim:',a.ndim)
print('a shape:',a.shape)


print('sum,axis0:\n',np.sum(a,axis = 0))
print('axis0 shape:\n',np.sum(a,axis=0).shape)
print('axis1:\n',np.sum(a,axis = 1))
print('axis1 shape:\n',np.sum(a,axis = 1).shape)
print('axis2:\n',np.sum(a,axis = 2))
print('axis2 shape:\n',np.sum(a,axis = 2).shape)

print('sum,axis none:\n',np.sum(a))
print('axis none shape:\n',np.sum(a,axis=None).shape)
print('sum,axis (0,1,2):\n',np.sum(a, axis=(0,1,2)))
print('axis (0,1,2) shape:\n',np.sum(a,axis=(0,1,2)).shape)
print('sum,axis (1,2):\n',np.sum(a, axis=(1,2)))
print('axis (1,2) shape:\n',np.sum(a,axis=(1,2)).shape)
print('sum,axis (0,1):\n',np.sum(a, axis=(0,1)))
print('axis (0,1) shape:\n',np.sum(a,axis=(0,1)).shape)
