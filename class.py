



class animal:
	#name = 'dog'
	live_position = 'land'
	def what_am_i(self):
#		print(name)#error
		return self.__name
	def what_am_i2(self,b):
		return self.__name
#	def animal(stri):
#		self.name = stri
	def __init__(self,string):
		self.__name = string

	__name = 'dog'

cat = animal
print(type(cat))
print(animal.what_am_i(cat))
#print(cat.what_am_i())
print(cat.what_am_i2(cat,'ss'))

hum = animal('human')
print(type(hum))
print(animal.what_am_i(hum))
print(hum.what_am_i())
print(hum.__name)
