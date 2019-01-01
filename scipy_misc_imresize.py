import numpy as np
import scipy.misc
#compare:img and img2

img = np.random.uniform(size=(2, 2, 3)) + 100.0
img = img - 117.0
img2 = img.copy()
###################################################################
#with preprocessing
print('img :', img)
print('img size:', img.size)
print('img type:', type(img))

min = img.min()
max = img.max()
img = (img - min) / (max - min) * 255
#you can do this N times!!it's just a linear operation
for i in range(10):
    min = img.min()
    max = img.max()
    img = (img - min) / (max - min) * 255

print('after preprocessing, img:\n', img)#0~255
print('size:', img.shape)
img = np.float32(scipy.misc.imresize(img, 2.))
print('after imresize, img:\n', img)#0~255
print('size:', img.shape)
img = img / 255 * (max - min) + min
print('finally, img:\n', img)#
print('size:', img.shape)
print('****************************************')
##################################################################
#without preprocessing before imresize

print('img2:', img2)
print('size:', img2.shape)
img2 = np.float32(scipy.misc.imresize(img2, 2.))
print('after imresize, img2:\n', img2)#0~255
print('size:', img2.shape)
img2 = img2 / 255 * (max - min) + min
print('finally, img:\n', img2)#
print('size:', img2.shape)
############################################################
#compare:img and img2
print(img == img2)