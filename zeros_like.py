import numpy as np

c = (2,3)
d = 2,3
print(type(c))
print(type(d))

def input_value(a,b=0):
	print("\na type:",type(a))
	print("b type:",type(b))

input_value(c,3)
#input_value(d)#error

input_value(2,3)
input_value((2,3))

