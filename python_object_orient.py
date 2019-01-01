# import heapq
#
#
# l = [5,222,33,124,54,1,3]
# print(l)
# heapq.heapify(l)
# print(l)
#
#
# l2 = []
# for i in range(len(l)):
#     heapq.heappush(l2,l[i])
#     print(l2)



class Human:
    age = 55#既可以在类里定义age，也可以在init里再定义age，其实是同一个
    def __init__(self,age = 100):
        self.age = age
    def how_old_r_you(self):
        return "I'm "+str(self.age)+" 's old"
    def public_func():
        print('hahaha')
class Human2:
    def __init__(self,age = 100):
        self.age = age#既可以在类里定义age，也可以在init里再定义age，其实是同一个
    def how_old_r_you(self):
        return "I'm "+str(self.age)+" 's old"

print(Human().how_old_r_you())
print(Human().age)

print(Human2().how_old_r_you())
print(Human2().age)


xiaoming = Human()
print(xiaoming.how_old_r_you())
xiaogang = Human(88)
print(xiaogang.how_old_r_you())
print(xiaogang.age)

#没有静态函数一说？直接用类访问也不行？
# Human().public_func()#TypeError: public_func() takes 0 positional arguments but 1 was given
#是不是只有有了Human()这个形式，就已经是实例了？只是我没赋值给xiaoming
Human.public_func()#这样就对了！
# Human.how_old_r_you()#TypeError: how_old_r_you() missing 1 required positional argument: 'self'
Human.how_old_r_you(xiaogang)#self的来源，显式的传对象给函数，或者隐式的用对象调用成员函数


print(Human)
print(xiaogang.__class__)
print(xiaogang)

##继承

class people:
    name = ''
    age = 0
    #private
    _fake_private = 9999
    __weight = 0#这个私有只是逻辑上的私有，可能是认为规定外部访问不访问下划线开头的？私有是双下划线，不是单下划线，是具有语法意义的
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s say: i'm %d old"%(self.name,self.age))

class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w)
        self.grade = g
    def speak(self):
        print("%s say: i'm %d old, i'm grade %d"%(self.name,self.age,self.grade))


hu = people('hu',32,72)
hu.speak()
# print(hu.__weight)
print(hu._fake_private)

liao = student('liao',32,88,3)
liao.speak()
print(liao.grade)
print(liao.age)
# print(liao.__weight)

#多继承


class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("I'm %s, I'm a speaker,my topic is %s"%(self.name,self.topic))


# class sample(speaker,student):
class sample(student,speaker,):
    a = ''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)
    #一方面，出现冲突的选继承池前排的，另一方面，没冲突的全都要
    # 重写的话直接覆盖了
    def speak(self):
        print('I\'m an American Idiot!!')
test = sample('hujintao',66,76,100,'helloworld')
print(test.a)
print(test.age)
# print(test.__weight)
print(test.grade)
print(test.topic)
test.speak()
super(sample,test).speak()


#类的私有方法
class Site():
    def __init__(self,name,url):
        self.name = name
        self.__url = url
    def who(self):
        print('name : ',self.name)
        print('url : ',self.__url)
    def __foo(self):
        print('private func')
    def foo(self):
        print('public func')
        # self.__foo(self)#wrong,this is 2 arguments
        self.__foo()
        # __foo(self)#wrong,this is not the func i want,it's undefined
x = Site('Hu','www.goooooodu.twcn')
x.who()
x.foo()
# x.__foo()
x.__init__('liao','www.250.com')#双下划线的成员不能外部访问，但是init这种却可以
x.who()
x.foo()
# x.__del__()#双下划线的成员不能外部访问，但是del这种却可以
# x.who()
print(x)
# 这些都要自定义吧？继承object不报错，但是也没达到预期!!!~!感觉len(x)和x.__len__()是等价的,这里很多是操作符！
# __init__ : 构造函数，在生成对象时调用
# __del__ : 析构函数，释放对象时使用
# __repr__ : 打印，转换
# __setitem__ : 按照索引赋值
# __getitem__: 按照索引获取值
# __len__: 获得长度
# __cmp__: 比较运算
# __call__: 函数调用
# __add__: 加运算
# __sub__: 减运算
# __mul__: 乘运算
# __truediv__: 除运算
# __mod__: 求余运算
# __pow__: 乘方
# print(x.__repr__)
# print(x.__setitem__(0,'aa'))AttributeError: 'Site' object has no attribute '__setitem__'
# print(x.__getitem__(0))
# print(len(x))
# print(x.__len__)#TypeError: object of type 'Site' has no len()
# print(x.__len__())#TypeError: object of type 'Site' has no len()
# print(x.who)

class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'Vector (%d,%d)'%(self.a,self.b)
    def __add__(self,other):
        return Vector(self.a+other.a,self.b+other.b)
vec1 = Vector(1,4)
vec2 = Vector(3,7)
vec3 = vec1 + vec2
print(vec3)#原来对象的表达式就是__str__()的返回值，就是print要输出的东西
#不过类型不算str,那应该是print或者是赋值符号什么的自动去找__str__()函数了,不然的话，打印的是这个object的地址
print(type(vec3))
vec4 = vec3
print(vec4)
print(type(vec4))
print(vec3.a)
print(vec3.b)





#Python中新式类 经典类的区别（即类是否继承object）
# C 为A的子类， D为BC的子类 ，A中有save方法，C对其进行了重写
#
# 在经典类中 调用D的save方法 搜索按深度优先 路径B-A-C， 执行的为A中save 显然不合理
# 在新式类的 调用D的save方法 搜索按广度优先 路径B-C-A， 执行的为C中save
#经典类
class A:
#新式类
# class A(object):
    def __init__(self):
        print('this is A')
    def save(self):
        print('come from A')
class B(A):
    def __init__(self):
        print('this is B')
class C(A):
    def __init__(self):
        print('this is C')
    def save(self):
        print('come from C')
class D(B,C):
    def __init__(self):
        print('this is D')
class E(C,B):
    def __init__(self):
        print('this is E')

d1 = D()
d1.save()
e1 = E()
e1.save()
##经典类结果为'come from A,但是实际是from C，说明python3默认新式类？
#实测，python2确实会这样
#classic
# this is D
# come from A
# this is E
# come from C
# new
# this is D
# come from C
# this is E
# come from C







