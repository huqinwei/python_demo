def f(n):
	return n * 2
x = 12.5

print(type(f))
print(type(x))



print(f)
print(x)


def call(fn,arg):
	return fn(arg)
def squared_call(fn,arg):
	return fn(fn(arg))

print(
	call(f,1),
	squared_call(f,1),
	sep='\n'
)




