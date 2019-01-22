a = [1,2,3]
b = [4,5,6]
c = [7,8,9,10]
print(type(zip(a,b)))
list1 = list(zip(a,b))
print(list1)

for i,j in zip(a,b):
	print(i,j)

list2 = list(zip(a,a,b,a))
print(list2)


list3 = list(zip(a,c))
print(list3)

list4 = list(zip(c,a))
print(list4)



list5= list(a.zip(c))

