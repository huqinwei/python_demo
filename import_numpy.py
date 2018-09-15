import numpy
print("numpy is a", type(numpy))
print("it contains names such as..",dir(numpy)[-5:])
print("it contains names such as..",dir(numpy)[-15:])
print("numpy.random is a", type(numpy.random))
print("it contains names such as..",dir(numpy.random)[-5:])
print("it contains names such as..",dir(numpy.random)[-15:])


print(type(numpy.ndarray))
array = numpy.random.randint(low = 1,high = 6,size = 9)
print("type(array):",type(array))
print("array:",array)
