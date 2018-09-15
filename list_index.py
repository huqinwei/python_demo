planets = ['1earth','2moon','3venus']

#print(planets[0])
#print(planets[1])
print(planets[-1])
print(planets[-2])
print(planets[-3])
print(planets[2:2])
print(planets[1:-1])
print(planets[-1:])



x = 12
# x is a real number, so its imaginary part is 0.
print(x.imag)
# Here's how to make a complex number, in case you've ever been curious:
c = 12 + 3j
print(c)
print(c.imag)



print(x.bit_length)
print(x.bit_length())
#help(x.bit_length)

people=['hu','qin','wei']
print(people.index('hu'))
people.append('hu')
print(people)
print(people.index('hu'))
