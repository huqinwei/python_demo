
#with open('3lines','w') as file:
	#file.write('first line\nsecond line\nfinal line\n')	

with open('3lines','r') as file:
	#print(file.read())
	#print(file.read())
	print(file.readlines())
	#print(file.read())
	#print(type(file.readline()))
	#print(file.readline())
with open('3lines','r') as file:
	#print(file.read())
	#print(file.read())
	print(file.readlines())
	#print(file.read())
	#print(type(file.readline()))

with open('3lines','a') as file:
	file.write('fourth line\n')
