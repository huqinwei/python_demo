
#Python赋值运算符

a = 21
b = 10
c = 0

c = a + b
print('c:',c)
c += a
print('c:',c)
c *= a
print('c:',c)
c /= a#float
# c //= a#int
print('c:',c)

c = 2
c %= a
print(c)
c **= a
print(c)

#Python位运算符
a = 60#00111100
b = 13#00001101
print(a&b)#00001100
print(a|b)#00111101=64-1-2
print(a^b)#00110001
print(~a) #11000011#(~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。

print(a<<1)
print(a<<2)
print(a>>1)

#Python逻辑运算符
#and和==还是有点小区别的，and不一定是==啊
# 	x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回 20。
# or	x or y	布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。
# not	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False
a = 10
b = 20
c = 0
print('a and b:',(a and b))
print('a and c:',(a and c))
print('a or b:',a or b)
print('c or b:',c or b)
print('not a:',not a)
print('not c:',not c)

#不过一般and 和or都用在条件控制了，没取值。

if a and b:
    print('a and b is true')
else:
    print('a and b is not true')

if a and c:
    print('a and c is true')
else:
    print('a and c is not true')


# Python成员运算符


a = 10
b = 20
c = 4
list = [1,2,3,4,5]
if a in list:
    print('a in list')
else:
    print('a not in list')

if b not in list:
    print('b not in list')
else:
    print('b in')
if c in list:
    print('c in list')

# Python身份运算符
# is	is 是判断两个标识符是不是引用自一个对象	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
# is not	is not 是判断两个标识符是不是引用自不同对象	x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。

aa = 20
cc = 33##看来和顺序也无关，这个cc并不能避免bb成为aa的别名
bb = 20
if aa is bb:
    print('aa is bb')
else:
    print('aa is not bb')

if id(aa) == id(bb):#分开声明的，居然id都一样？成了别名？这种“优化”的意义是？
    print('aa_id equals to bb_id')
    print(id(aa))
    print(id(bb))

bb = 30#原来这个优化也没那么死板，发生改变的时候再分开。
if aa is bb:
    print('aa is bb')
else:
    print('aa is not bb')

if id(aa) == id(bb):
    print('aa_id equals to bb_id')
print(id(aa))
print(id(bb))

aaa = [1,2,3]
bbb = aaa
ccc = aaa[:]
print(bbb is aaa)
print(bbb == aaa)
print(ccc is aaa)#深层拷贝，ccc和aaa不是is的关系
print(ccc == aaa)







