#from Pillow import Image
from PIL import Image
import sys
#2*3

def fill_image(image):
	width,height = image.size
	new_image_length = width if width > height else height
	new_image = Image.new(image.mode, (int(new_image_length * 3 / 2),int(new_image_length)),color='white')
	print("new width:",new_image.width)
	print("new height:",new_image.height)
	if width > height:
		new_image.paste(image,(0,int((new_image_length - height)/2)))
	else:
		new_image.paste(image,(int((int(new_image_length * 3 / 2) - width)/2),0))
	return new_image
def cut_image(image):
	width,height = image.size
	#item_width = int(width / 3)
	item_width = int(width / 3)
	item_height = int(height / 2)
	box_list = []
	for i in range(0,2):
		for j in range(0,3):
			print((j*item_width,i*item_height,(j+1)*item_width,(i+1)*item_height))
			box = ((j*item_width,i*item_height,(j+1)*item_width,(i+1)*item_height))
			box_list.append(box)
	image_list = [image.crop(box) for box in box_list]
	return image_list
			 
def save_images(image_list):
	index = 1
	for image in image_list:
		#image.show()
		image.save(str(index) + '.png','PNG')
		index += 1

if __name__ == '__main__':
	file_path = "dog.jpg"
	image = Image.open(file_path)
	image = fill_image(image)
	image_list = cut_image(image)
	save_images(image_list)	
