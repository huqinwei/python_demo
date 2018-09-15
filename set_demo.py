char_list = 'hello world!hahahaheheheoooooo'
print(char_list)
s = set(char_list)
print(s)

s2 = s.copy()

s3 = s
s.add('q')
s2.remove('e')
s2.discard('e')
print('s2:',s2)
print('s3:',s3)

dif = s2.difference(s3)
print('s2.dif:',dif)#important!!!!!!!!!!!!!!!!!!
dif = s3.difference(s2)
print('s3.dif:',dif)

'''
s3.clear()
print(s3)
print(s)
print(s2)
'''
