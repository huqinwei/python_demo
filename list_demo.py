

a = (1,2,3,4,5)
print(type(a))
a2 = 1,2,3,4,5
print(type(a2))
#a3 = zip(1,2)
#print(type(a3))



b = [1,1,2,3,4,5,100,'a']
print(type(b))
print('b include:')
for i in b:
	print(i)
#	print(b[i])
print('length of b:',len(b))
for i in range(len(b)):
#	print(i)
	print(b[i])

print('before:',b)
b.append('new')
print('append:',b)
b.insert(1,'insert')
print('insert:',b)
b.remove('a')
print('remove a:',b)
print('count 1:',b.count(1))
print('index of 1:',b.index(1))
print('index of 2:',b.index(2))

b2 = [33,11,4,3,55,133,2]
print('b2:',b2)
print('sort:',b2.sort())#stri and int can't sort
print('b2:',b2)
print('sort reverse:',b2.sort(reverse=True))
print('b2:',b2)
print('b2[-1]:',b2[-1])
print('b2[0:3]:',b2[0:3])
print('b2[0:]:',b2[0:])
print('b2[3:0]:',b2[3:0])
print('b2[3:-1]:',b2[3:-1])#embarassing
print('b2[-3:-1]:',b2[-3:-1])
print('b2[:-1]:',b2[:-1])





b3 = ['a','ar','b','c','ai','aa','bb','abcd']
print('b3:',b3)
print('sort:',b3.sort())#stri and int can't sort
print('b3:',b3)
print('sort reverse:',b3.sort(reverse=True))
print('b3:',b3)


c = {1,2,3,4,5}
print(type(c))














