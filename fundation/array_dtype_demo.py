import numpy as np

a = np.zeros((3,3))
print('zeros:',a.dtype,' a is ',a)

a = np.ones((3,3))
print('ones:',a.dtype,' a is ',a)

a = np.array([1,2,3])
print('array:',a.dtype,' a is ',a)

a[0] = 0.1
print('assign:',a.dtype,' a is ',a)

a = a + 1.5
print('upcast:',a.dtype,' a is ',a)


a = np.array([1,2,3.7])
print('array:',a.dtype,' a is ',a)
b = a.astype(int)
print('force cast:',b.dtype,' b is ',b)
c = np.round(a)
print('round:',c.dtype,' c is ',c)

import tensorflow as tf
sess = tf.Session()
a = [[0.2,0.3,0.5],[0.1,0.8,0.1]]
c = tf.argmax(a,1)
b = tf.multinomial(a,1)
print(sess.run(c))
print(sess.run(b))














