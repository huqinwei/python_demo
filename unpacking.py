

nums = [
    ('one', 1, 'I'),
    ('two', 2, 'II'),
    ('three', 3, 'III'),
    ('four', 4, 'IV'),
]

for word, integer, roman_numeral in nums:
    print(integer, word, roman_numeral, sep=' = ', end='; ')

for tup in nums:
	word = tup[0]
	integer = tup[1]
	roman_numeral = tup[2]
	print(integer,word,roman_numeral,sep=' = ',end = ';')



