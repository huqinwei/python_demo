import numpy as np
import scipy.misc


#x = np.random.randint(1,255,size=(100,100))
x = np.random.uniform(1,255,size=(100,100))
x = np.random.uniform(1,255,size=(100,100))
x = np.random.standard_cauchy(size=(100,100))
print("x:",x)


scipy.misc.toimage(x).save('test.jpg')
