
# Python3 数据结构

l1 = list((1,2,3))
print(l1)
l1.append(4)
print(l1)
#l1[len(l1)] = [5]#out of range
l1[len(l1):] = [5]
print(l1)
l1.insert(0,0)

print(l1)
l1.insert(len(l1),6)
print(l1)
l1.insert(len(l1)-1,5.5)
print(l1)

#del l1是整个对象删除，del l1[:]等同于clear
# del(l1)

del l1[:]
# l1.clear()
print(l1)


a = [66.25, 333,333,1,1234.5]
print('count element:',a.count(333), a.count(66.25),a.count('x'))
a.insert(2,-1)
a.append(333)
print(a)
print(a.index(333))
print(a.index(-1))
print('remove() return:',a.remove(333))#removes only one 333
print(a)
print('reverse() return:',a.reverse())
print(a)
print('sort() return:',a.sort())
print(a)

#将列表当做堆栈使用
stack = [3,4,5]
stack.append(6)
stack.append(7)
print('stack:',stack)
print('stack pop:',stack.pop())
print('stack:',stack)
print('stack pop:',stack.pop())
print('stack:',stack)
print('stack pop:',stack.pop())
print('stack:',stack)
print('stack pop:',stack.pop())
print('stack:',stack)
print('stack pop:',stack.pop())
print('stack:',stack)

#将列表当作队列使用
from collections import deque
queue = deque(['Eric','John','Michael','Jackson'])
queue.append('Terry')
queue.append('Clark')
print(queue)
print('pop:',queue.popleft())
print(queue)
print('pop:',queue.popleft())
print(queue)




# 列表推导式
# 列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列。
#
# 每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。如果希望表达式推导出一个元组，就必须使用括号。
#
# 这里我们将列表中每个数值乘三，获得一个新的列表：

vec = [2,4,6]
print([3*x for x in vec])
print([3*x for x in vec if x > 3])
print([3*x for x in vec if x < 2])
print([[x,x**2]for x in vec])



freshfruit = ['            banana', '           apple         ', 'pear          ']
print([weapon.strip() for weapon in freshfruit])


vec1 = [2,4,6]
vec2 = [4,3,-9]
print([x*y for x in vec1 for y in vec2])#这其实是双层循环，不是并列循环，x取一个值，y遍历一遍
print([x+y for x in vec1 for y in vec2])
print([vec1[i] * vec2[i] for i in range(len(vec1))])#这个倒是同步遍历了，其实也不安全，前提是等长。
print([str(round(355/113, i)) for i in range(1,6)])




#嵌套列表解析
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
print(matrix)
# matrix.reshape(4,3)#AttributeError: 'list' object has no attribute 'reshape'
# print('reshape:',matrix)

matrix2 = [[row[i] for row in matrix] for i in range(4)]
print(matrix2)
#外层循环是i，所以一个固定的i，对应所有的row，攒起来，就是每列第一个，组合成了第一行，每列第二个，组成了第二行。
for row in matrix:
    print(row)

#土法子，先定义好，然后修改值
matrix3 = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],]
for i in range(len(matrix[0])):
    j = 0
    for row in matrix:
        print(row[i])
        matrix3[i][j] = row[i]
        j += 1
print(matrix3)

#这是一次组合好一个[]，然后append进去
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

#这种更直观
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)


#del删元素的话，是用下标，而remove是用值
a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a)
del a[0]
print(a)
del a[-2:-1]
print(a)
del a[:]
print(a)
del a
# print(a)#这个报错好像是这样的，他后边有东西要执行，尤其有打印print('hello')要执行，就报错，如果什么都没有，就不报错了
b = 4#一个定义b的语句隔开，再来个打印就不报错了，神奇
print('hello')

t = 12345,54321,'helloheloo'
print(t)
print(t[0])
u = t,(1,2,3,4,5)#nested
print(u)



# 集合
# 集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
#
# 可以用大括号({})创建集合。注意：如果要创建一个空集合，你必须用 set() 而不是 {} ；后者创建一个空的字典，下一节我们会介绍这个数据结构。
#警告，大括号两种用途，默认给了字典！！!!!!!!!!!!!


dict1 = {}
print(type(dict1))

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(type(basket))
print(basket)
print('orange' in basket)
print('lalsjalksdja' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a-b)
print(b-a)
print(a|b)
print(a&b)
print(a^b)

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)




#dictionary
tel = {'jack':4008003333, 'sparow':'8008208820'}
print(tel)
# print(tel[0])#key error
print(tel['jack'])
tel['chowyunfat'] = 1300000
print(tel)
l1 = list(tel.keys())
print(l1)
print(sorted(l1))
l2 = list(tel.values())
print(l2)

print('jack' in tel)
print(tel['jack'] != None)
# print(tel['jackaaa'])#KeyError: 'jackaaa'
print(tel.get('jack'))
print(tel.get('jackaaa'))
print(tel.get('jackaaa')!=None)#这是另一种查看in的方式


#构造#@
#这个用[]还是()好像无所谓，可能是list和tuple都只是载体，他内部拆解了，要求可迭代，至少长2
d1 = dict([('a',444),('aasd',5324),('ny',343)])
d2 = dict((('a',444),('aasd',5324),('ny',343)))
# d3 = dict(('a',444),('aasd',5324),('ny',343))#expected at most 1 arguments,got 3
# d3 = dict(('a',444))#ValueError: dictionary update sequence element #0 has length 1; 2 is required
print('d1:',d1)
print('d2:',d2)
# print('d3:',d3)

d4 = {x:x**2 for x in range(4)}
d5 = {x:x**2 for x in (4,2,11)}
print(d4)
print('d5:',d5)





# 遍历技巧

# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来：
knights = {'gallahad':'the pure', 'robin':'the brave'}
for k,v in knights.items():
    print(k,v)
for k in knights:
    print(k)
for v in knights.values():
    print(v)

for i,v in enumerate(['tic','tac','toe']):
    print(i,v)
#用zip打包多个容器可以同时遍历,不限于2个,1个，3个，都支持
questions = ['name','quest','favorite color']
answers = ['lancelot','the holy grail', 'blue']
tips = ['tip1','tip2','tip3']
for q,in zip(questions):
    print('what is your {0}? '.format(q))
for q,a,t in zip(questions,answers,tips):
    print('what is your {0}? It is {1}.the tips is {2}'.format(q,a,t))

for i in range(1,10,2):
    print(i)
for i in reversed(range(1,10,2)):
    print(i)
print(range(1,10,2))
print(reversed(range(1,10,2)))

#sorted是一个技巧，不同于sort，sort直接改了原值，sorted是返回右值
basket = ['apple','orange','apple','pear','orange','banana']
print(basket)
for f in (set(basket)):
    print(f)
for f in sorted(set(basket)):
    print('sorted:',f)
basket_set = set(basket)

print('before sorted:',basket_set)
for f in sorted(basket_set):
    print('sorted:',f)
print('after sorted:',basket_set)




#悲剧的set不可以指定元素del，甚至都不能指定元素访问，只能查询啊？
a = set('abracadabra')
print('set a is:',a)
# print(a[0])
# del a[0]
print(a.remove('r'))# remove()	移除指定元素
print(a)
print(a.pop())# pop()	随机移除元素
print(a)
a.add('i')# add()	为集合添加元素
print(a)


# 集合内置方法完整列表
# clear()	移除集合中的所有元素
# copy()	拷贝一个集合
# difference()	返回多个集合的差集
# difference_update()	移除集合中的元素，该元素在指定的集合也存在。
# discard()	删除集合中指定的元素
# intersection()	返回集合的交集
# intersection_update()	删除集合中的元素，该元素在指定的集合中不存在。
# isdisjoint()	判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
# issubset()	判断指定集合是否为该方法参数集合的子集。
# issuperset()	判断该方法的参数集合是否为指定集合的子集
# symmetric_difference()	返回两个集合中不重复的元素集合。
# symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
# union()	返回两个集合的并集
# update()	给集合添加元素


#dict是可以直接删的，可能和访问机制有关系，list和dict都有下标访问，set没有，不支持del
tel = {'jack':4008003333, 'sparow':'8008208820'}
print(tel)
print(tel['jack'])
del tel['jack']
print(tel)





