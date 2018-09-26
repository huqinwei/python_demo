squares = [n**2 for n in range(10)]

print(squares)
l = []
l2 = []
for n in range(10):
	l.append(n**2)
for s in squares:
	l2.append(s)
print('l:',l)
print('l2:',l2)

planets=['earth','jupit','venus','mars567','aa2345','bb234567','cc234','dd','ee']


short_planets = [planet for planet in planets if len(planet) < 6]
#short_planets = ['#'+ planet for planet in planets if len(planet) < 6]#practice:just an operation

print(planets)
print(short_planets)














