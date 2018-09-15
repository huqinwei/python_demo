def least_difference(a,b,c):
	"""
		this is
		my functions's
		document!
	"""

	diff1=abs(a-b)
	diff2=abs(b-c)
	diff3=abs(a-c)
	return min(diff1,diff2,diff3)

def least_difference2(a,b,c):
	diff1=abs(a-b)
	diff2=abs(b-c)
	diff3=abs(a-c)
	return diff1,diff2,diff3

def least_difference3(a,b,c):
	diff1=abs(a-b)
	diff2=abs(b-c)
	diff3=abs(a-c)
	min(diff1,diff2,diff3)

a = print(least_difference(100,1000,10000))
b,c,d = least_difference2(100,1000,10000)
print(a)
print(b)
print(c)
print(d)

print(
	least_difference3(1,10,100),
	least_difference3(1,10,10),
	least_difference3(5,6,7),
)

print()
print()
least_difference(1,10,100)

#help(least_difference)



#print(print())

