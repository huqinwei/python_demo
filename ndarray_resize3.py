import numpy as np
import scipy.misc
img2 = np.array([[1,2,3]])

print(img2)
#print("img2 size:",type(img2))
print("img2 size:",img2.size)
print("img2 shape:",img2.shape)
img2 = scipy.misc.imresize(img2,2.0)
print("after imresize:",img2)
print("img2 size:",img2.size)
print("img2 shape:",img2.shape)
