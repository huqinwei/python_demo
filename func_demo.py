

#严格的说，变量名不具有类型属性，他只是个引用，连id都变了,id是对象的id，不是引用(point)的id
#这个“优化”看来只支持普通变量，list就不是了
a = 5
b = 5
print('a:',a,id(a),type(a))
print('b:',b,id(b),type(b))
a = 'hello'
print(a,id(a),type(a))
print(b,id(b),type(b))


a = [1,2,3]
b = [1,2,3]
print('a:',a,id(a),type(a))
print('b:',b,id(b),type(b))
a = 'hello'
print(a,id(a),type(a))
print(b,id(b),type(b))






###########################################################
#可更改(mutable)与不可更改(immutable)对象

a = 'hello'
b = 'lowa'
c = 'hello'
d = 'lja'
e = 'hello'
print(id(a),id(c),id(e))# str本身是一个“常量”
# 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
a = 5
b = 6
c = 5
d = 8
e = 5
print(id(a),id(c),id(e))# 这也就说通了，为什么a=5和b=5会指到同一个位置，每个手写数字本身就是一个“常量”

#唯一不解的是，你一个脚本语言，不是一句一句的执行吗？怎么还能提前优化的？???????
# 或许不是提前优化，是执行到c=5的时候，找之前的“缓存”，或者说immutable对象，找到了，就指向同一个。c=6也不是改变原来的5的值为6，而是直接改了c的指向。
c = 6
print(id(a),id(c),id(e))

#果然是这样的，即便是让c“指针”指向a，再“改”c的值，其实a还是不变的。
a = 5
c = a
c = 6
print(a)
print(c)
print(id(a),id(c))
#不过局限性也暴露了，不能通过其他“指针”修改原来的值吗？list之类的是可以，但那是mutable，所以这就是immutable和mutable对象的区别？！！！！！
#怪不得传“引用”改不成，要用return赋值呢，其实问题就在这。
def funcA(a):
    a = 5
    return a
a = 6
b = funcA(a)
print('after call func, a is:',a,id(a))
print('after call func, b is:',b,id(b))

def funcB(a):
    a[0] = 3
    return a
a = [333]
b = funcB(a)
print('after call func, a is:',a,id(a))
print('after call func, b is:',b,id(b))

#python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。

def changeme(mylist):
    mylist.append([1,2,3,4])
    return
mylist=[10,20,30]
print(mylist,"\t",id(mylist))
changeme(mylist)
print(mylist,"\t",id(mylist))




# 参数
# 以下是调用函数时可使用的正式参数类型：
#
# 必需参数
def printme(str):
    print(str)
    return
# printme()#missing 1required positional argument

# 关键字参数
def printme(str):
    print(str)
    return
printme(str='hello')

def printinfo(name,age):
    print('name:',name)
    print('age:',age)
    return
printinfo('hu',30)
printinfo(age = 32,name='hu')

# 默认参数
def printinfo(name,age=38):
    print('name:',name)
    print('age:',age)
    return
printinfo('hu')
printinfo('hu',88)

#当然，语法上也避免了这种歧义，这样输入三个到底怎么算，意义不明。
# def func(a,b,c=3,d):#SyntaxError: non-default argument follows default argument
#     return a+b+d


# 不定长参数
# 你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。基本语法如下：
#
# def functionname([formal_args,] *var_args_tuple ):
#    "函数_文档字符串"
#    function_suite
#    return [expression]
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。

def printinfo(arg1,*vartuple):
    print('output')
    print(arg1)
    print(vartuple)
def printinfo2(arg1,*vartuple):
    print('output2:')
    print(arg1)
    for val in vartuple:
        print(val)
printinfo(100)
printinfo(70,60,50)
printinfo2(100)
printinfo2(70,60,50,40,(30,20))



# 还有一种就是参数带两个星号 **基本语法如下：
#
# def functionname([formal_args,] **var_args_dict ):
#    "函数_文档字符串"
#    function_suite
#    return [expression]
# 加了两个星号 ** 的参数会以字典的形式导入。

def printinfo(arg1, **vardict):
    print('output:')
    print(arg1)
    print(vardict)
printinfo(1,a=2,b=3)#字典的必要输入形式
# printinfo(1,2,3)#TypeError: printinfo() takes 1 positional argument but 3 were given

# 声明函数时，参数中星号 * 可以单独出现，例如:
#
# def f(a,b,*,c):
#     return a+b+c
# 如果单独出现星号 * 后的参数必须用关键字传入。

def func(a,b,*,c):#这个比较特殊啊，说他是默认值的参数吧， 也不是
    return a+b+c
# func(1,2,3)#TypeError: func() takes 2 positional arguments but 3 were given
print(func(1,2,c=3))




# 匿名函数
#lambda区别于普通def的地方，没有多余的代码块，就一个表达式！！还有一些命名空间的区别，还有和inline的区别，暂且不表
sum = lambda arg1,arg2:arg1+arg2
print(sum(10,20))


# return语句
def return_none():
    return
print(return_none())



# 变量作用域
# Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。
#
# 变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是：
#
# L （Local） 局部作用域
# E （Enclosing） 闭包函数外的函数中
# G （Global） 全局作用域
# B （Built-in） 内建作用域
# 以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。

x = int(2.9)#B
g_count = 0#G
def outer():
    o_count = 1#E          这个好像不是固定的，可以多层吧，总之是最近的那个？
    def inner():
        i_count = 2#L

#Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问，如下代码：

if True:
    msg = 'im groot'
print(msg)

def test():
    msg2 = 'im batman'
# print(msg2)#NameError: name 'msg2' is not defined

total = 0
def sum(arg1,arg2):
    total = arg1+arg2
    print('in func:',total)
    return total
sum(10,20)
print('out:',total)
total = sum(10,20)
print('out:',total)



# global 和 nonlocal关键字
# 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
#原来这个操作也不是不可以有
#其实就是让内部直接用global了

num = 1

def fun1():
    global num
    print('inner,before change:',id(num),num)
    num = 123
    print('inner,after:',id(num),num)
fun1()
print('outter:',id(num),num)

#对照组，不改变外部
num=1
def fun2(num):
    print('inner,before change:',id(num),num)
    num = 123
    print('inner,after:',id(num),num)
fun2(num)
print('outter:',id(num),num)



#如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了

def outer():
    num = 10
    def inner():
        nonlocal num
        num = 100
        print('inner:',num)
    inner()
    print('outer:',num)
outer()
#对照组，不改变外部
def outer2():
    num = 10
    def inner():
        num = 100
        print('inner:',num)
    inner()
    print('outer:',num)
outer2()



a = 10
def test():
    a = a + 1#这两个一个报错，一个虽然没报错，执行也不正常
    # a += 1
    print(a)
def test2(a):#对照组
    a = a + 1
    # a += 1
    print(a)
# test()
test2(4)




