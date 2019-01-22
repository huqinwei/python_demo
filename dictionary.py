import copy

dict = {'input':50,'output':100,1:1000}
print(type(dict))
print(dict)
#print(dict[0])
print(dict['input'])
print(dict[1])
dict['ha'] = 5000
print(dict)
#dict.remove('ha')
#dict['dict2':{'hello':12345}]
dict['dict2'] = {'hello':12345}
print(dict)

dict2 = {'a':1,'b':2,'c':{'d':4}}
print(dict2)
dict3 = copy.deepcopy(dict2)
print(dict2['c']['d'])
dict2['c']['d'] = 100
print(dict2)
print(dict3)
