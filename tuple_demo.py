

tup1 = ('google','huqinwei','baidu')
print(tup1)
print(type(tup1))
print(tup1[0])#访问和数组一样，但是不能赋值
print(tup1[1])
print(tup1[-1])
# tup1[1] = 'alimama'#TypeError: 'tuple' object does not support item assignment
# print(tup1)\

real_tup = (50,)
fake_tup = (50)#这种不能成为元组
print(type(real_tup))
print(type(fake_tup))

#拼接操作同list
tup2 = ('yahoo','gmail','youtube')
tup3 = tup1 + tup2
print('tup3:',tup3)



l1 = ['a','b','c']
l2 = ['d','h','j']
l3 = l1 + l2
print(l3)




#这句有什么问题，能使后边的代码都不执行
# del tup3
# del(tup3)
# print(tup3)
##这句就没问题
# del tup1s
# print(tup1)
#同是拼接而成，，l3也可以
# del l3
# print(l3)
# del l1
# print(l1)
# del之后不能print，找不到这个变量，不特定于元祖，都一样吧



print((tup3))
print([tup3])
print(len(tup3))

tup4 = tup3 * 3
print(tup4)

print('a' in tup4)
print('huqinwei' in tup4)
for val in tup4:
    print(val,end=',')
print('\ncut:',tup4[-2:])

tup5 = ('bbbbb','bbba','bbbc')
print((tup5))
print(max(tup5))
print(min(tup5))
tup6 = (444, 2232,44534,412)
print(max(tup6))
print(min(tup6))

tup7 = tuple(l3)
print(l3)
print(tup7)

