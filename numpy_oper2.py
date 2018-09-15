import numpy as np

A = np.arange(2,14).reshape((3,4))
print(np.argmin(A))
print(A.argmin())
print(A.argmax())



#print(A.average())
print(np.average(A))
print(np.median(A))
print(np.cumsum(A))

print(A)
print(A[2][2])
print(A[2,2])


print(A[2][:])
print('A[2:]',A[2:])
print('A[0:]',A[0:])
print('A[0,1:2] ',A[0,1:2])
print('A[0:,1:2] ',A[0:,1:2])

for row in A:
	print('row ',row)
for column in A:		#just a name,not real column
	print(column)
for real_column in A.T:
	print('column ',real_column)
print(A.flatten())
print(A.flat)
print(type(A.flat))
for item in A.flat:
	print('item:',item)










