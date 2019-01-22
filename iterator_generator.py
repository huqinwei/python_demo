

l1 = [1,2,3,4,5,6,7,8,9]
l2 = list((2,2,2,2,3))
print(l2)
it = iter(l1)
print(it)
print(next(it))
print(next(it))
print(next(it))
# print('next(l1):',next(l1))#TypeError: 'list' object is not an iterator
print(it)
#感觉迭代器像是个队列，next就像popleft
for x in it:
    print(x,end = ' ')


import sys
l1 = [1,2,3,4,5,66]
it = iter(l1)
while True:
    try:
        print((next(it)))
    except StopIteration:
        # sys.exit()
        print('im not exit yet?')#原来即使弹出exception，这样也是不能结束的！！！
        break#we need a break


#创建一个迭代器

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        raise StopIteration
myclass = MyNumbers()
print(myclass)
# print(id(myclass))
myiter = iter(myclass)
print(myiter)
# print(id(myiter))
print('next(myiter):',next(myiter))
print('next(myiter):',next(myiter))
#其实这是一样的！只是用了一个新变量名方便区分!!当然这个情况只针对这个简陋的自定义迭代器，针对list是无效的！！！
print('next(myclass):',next(myclass))
print('next(myclass):',next(myclass))
print('next(myclass):',next(myclass))
#关于什么时候报错，感觉逻辑也挺奇葩，明明这也算一次迭代，但是就是不报错，而且提取出来的元素，只到20就停了，前边5次，现在20次，应该是25
'''
for i in range(20):
    # print('for-loop:')#但是你放开这句，就能报错。。。。！
    next(myiter)
    print(next(myiter))
   '''
# 好像和中间的next(myclass)有关，但是区别在哪？
# 甚至还和前边是不是打印id有关，应该是玄学报错？！
# 只是不显示，但是程序确实停了！

#生成器
'''
def fibonacci(n):
    a,b,counter = 0,1,0
    while True:
        if(counter > n):
            return
        #只要yield的变量，就是迭代器要返回的，不限制,哪怕是个常量，格式也自由#但不是一次return这么多个值，一次只return一个，这就很乱了
        yield 'a is ' + str(a)
        yield [b]
        yield a,b
        yield 100

        a,b=b,a+b

        counter += 1


f = fibonacci(5)
print(f)

while True:
    try:
        print(next(f),end='-----')
    except StopIteration:
        sys.exit()
'''
# 感觉generator的逻辑像是，里边要设定无限循环，你每次用next调用它， 内部就会自动无限向下执行,执行到一个yield为止。
def failed_generator(n):
    a,b,counter = 0,1,0
    if(counter > n):
        return
    #这个没有循环的generator，因为有四个yield，所以能执行四次，然后代码到底，结束。
    yield 'a is ' + str(a)
    yield [b]
    yield a,b
    yield 100

    a,b=b,a+b

    counter += 1

g = failed_generator(10)
print(g)

while True:
    try:
        print(next(g),end='++++')
    except StopIteration:
        sys.exit()









