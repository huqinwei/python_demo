def mod_5(x):
	return x%5

print(
	'Which number is biggest?',
	max(100,51,14),
	'Which number is the biggest modulo 5?',
	max(100,51,14,key=mod_5),
	'Which number is the smallest modulo 5?',
	min(100,51,14,key=mod_5),
	sep='\n',
)
