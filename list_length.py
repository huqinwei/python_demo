a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]
e = [1,2,3][1:-1]
f = [1, 2, 3][1:1]
g = [1, 2, 3][1:2]
h = [1, 2, 3][1:3]
d2 = [1, 2, 3,4][1:]
d3 = [1, 2, 3,4][1]#there is no so-called '2-dim' list like this,just a child of array
d4 = [[1,2,3,4],[1]]#this is real 2-dim list
print(type(b[1]))
print('length c:',len(c))
print(d,' and length is ',len(d))#child list of [1,2,3],is[2,3]
print('d3:',d3)#child list of [1,2,3],is[2,3]
print('d4:',d4)#child list of [1,2,3],is[2,3]
print('d4[1][0]:',d4[1][0])
#print('d4[1][0]:',d4[1][1])#out of range,there is no default filled value
#print(d.shape)
print(len(e))
print('f length:',len(f))
print(len(g))
print(len(h))


print(len(d2))



