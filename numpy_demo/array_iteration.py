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


print('===================================================')
print('A:\n',A)
print('===================================================')

for row in A:
	print('row iteration:',row)
for column in A:		#just a name,not real column
	print('fake column iteration:',column)
for real_column in A.T:
	print('column iteration:',real_column)
print('flatten:',A.flatten())
print('a.flat:',A.flat)
print('type of flat:',type(A.flat))
for item in A.flat:
	print('flat iteration:',item)










