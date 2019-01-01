import numpy as np
##np.save('temp/123',np.array([[1,2,3],[4,5,6]]))#default postfix .npy
'''
a = np.load('temp/123')
!!!!!!!!!!!!!!!!error,default postfix is .npy,then the file is 123.npy
'''
##a = np.load('temp/123.npy')
##print(a)

##a = np.array([[1,2,3],[4,5,6]])
##b = np.array([1,2])
##np.savez('temp2/123',a=a,b=b)#savez's default postfix is npz
data = np.load('temp2/123.npz')
print(data)
print(data['a'])
print(data['b'])
data.close()

'''
print(data['a'])
!!!!!!!!!!!AttributeError: 'NoneType' object has no attribute 'open'
'''


x = np.load('temp/123.npy',mmap_mode='r')
print(x[0,:])

'''
y = np.load('temp2/123.npz',mmap_mode='r')
print(y[0,:])
!!!!!!!!!!!TypeError: not all arguments converted during string formatting
'''









