#set is hash?
#set like heap mem


a_set = set(['a','b','d','g','f','z','h'])
b_set = set(['a','b','u','g'])

print(type(a_set))
print(a_set)
a_set.add('a')
print(a_set)
a_set.add('u')
print(a_set)


a_set.remove('a')
print(a_set)
#a_set.remove('a')#this will be error,can not remove same element twice
a_set.discard('a')

print(a_set.difference(b_set))

a_set.clear()
print(a_set)
