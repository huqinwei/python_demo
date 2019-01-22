import numpy as np
import scipy.misc
img = np.ndarray(shape = (3,3,3))
#img2 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
img2 = np.array([[[11,12,13],[4,5,6]],[[7,8,9],[10,11,12]]])

print(img)
print(img2)

print("img's max is ",img.max())
print("img2's max is ",img2.max())
#print("img2[0]'s max is ",img2[0].max())
#print("img2[1]'s max is ",img2[1].max())

#print("img2[0][0]'s max is ",img2[0][0].max())
#print("img2[1][0]'s max is ",img2[1][0].max())


#print("img2[1][0]'s min is ",img2[1][0].min())
max_ = img2.max()
min_ = img2.min()
img2 = (img2 - img2.min())    /(img2.max() - img2.min())
#print(img2)
img2 = img2 * 255
print(img2)

print("before imresize: shape is ",img2.shape)
img2 = scipy.misc.imresize(img2,2.0)
print("after imresize:",img2)
print("after imresize: shape is ",img2.shape)
img2 = np.float32(img2)
print("after float trans:",img2)

img2 = img2 / 255 * (max_ - min_) + min_
print("final:",img2)


img3 = np.float32(scipy.misc.imresize(img2,100.0))
img3 = img3 / 255 * (max_ - min_) + min_

def savearray(img_array, img_name):
	scipy.misc.toimage(img_array).save(img_name)
	print("img saved:%s"%img_name)

savearray(img2,'to_img.jpg')
savearray(img3,'to_img_large.jpg')





