import numpy as np
import scipy.misc
img2 = np.array([[6,5,4],[3,2,1]])

print(img2)
#print("img2 size:",type(img2))
print("img2 size:",img2.size)
print("img2 shape:",img2.shape)
img2 = scipy.misc.imresize(img2,2.0)
print("after imresize:",img2)
print("img2 size:",img2.size)
print("img2 shape:",img2.shape)
