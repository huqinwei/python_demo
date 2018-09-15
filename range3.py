for i in range(10):
	print(i)

for i in range(10,[2]):
	print(i)


print("------------------")

li = [lambda:x for x in range(10)]
#del x
print(li[0]())

a = 3
b = [a]
b.append(4)
print(b)







