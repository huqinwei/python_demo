planets = ['1earth','2moon','3venus']

#print(planets[0])
#print(planets[1])
print(planets[-1])
print(planets[-2])
print(planets[-3])
print(planets[2:2])
print(planets[2:3])
print(planets[1:-1])#no other way to access 3venus?
print(planets[1:])#except for this
print(planets[-1:])#and this

print('planets[1][1]',planets[1][1])
print('planets[1][2]',planets[1][2])



x = 12
# x is a real number, so its imaginary part is 0.
print(x.imag)
# Here's how to make a complex number, in case you've ever been curious:
j=5#it doesn't make difference
c = 12 + 3j#this j is just a 'symbol'
c2 = 12 + 3*j#this j is a variable
c3 = complex(12,3)
c4 = complex(1)
c5 = complex("1")
c6 = complex("1+2j")
#c7 = complex("1 + 2j")
print(c)
print(c2)
print(c3)
print(c4)
print(c5)
print(c6)
#print(c7)
#print(c.subs(1))
print(type(c))
print(c.imag)
#help(complex.imag)



print('x\'s mem size',x.bit_length)
print(x.bit_length())#property, not function

people=['hu','qin','wei']
print(type(people))
print(len(people))
print(people.index('hu'))
people.append('hu')
print(people)
print(people.index('hu'))
