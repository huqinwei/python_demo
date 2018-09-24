#demo1
a = 6
print(id(a))


def f():
    print(a)
    print(id(a))


f()
print(id(a))
print('finally:', a)
#demo2
a=6
print(id(a))
def f():
    print(a)
    a = 2#wrong position
    print(id(a))
f()
print(id(a))
print('finally:',a)



#demo3

a = 6
print(id(a))


def f():
    a = 2  # right position!!!!!!!!
    print(a)
    print(id(a))


f()
print(id(a))
print('finally:', a)

#demo4
a=6
print(id(a))
def f():
    print(a)
    global a#wrong position
    print(id(a))
f()
print(id(a))
print('finally:',a)
