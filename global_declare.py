
'''
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
'''
#demo4
'''
a=6
print(id(a))
def f():
    print(a)
    print(id(a))
    global a#wrong position
    print(a)
    print(id(a))
f()
print(id(a))
print('finally:',a)
'''
#demo5
#assign before global declare
'''
a = 6
print('id:',id(a))
def f():
    a = 3
    print('in function f() ',a)
    print('id:',id(a))
    global a
    a = 5#another a
    print(a)
    print('id:',id(a))#another a
f()
print('after f():',a)
print(id(a))

'''
#demo5.2
a = 6
print('value is ',a, ' id is ',id(a))
a = 5
print('value is ',a, ' id is ',id(a))
a = 4
print('value is ',a, ' id is ',id(a))
a += 3
print('value is ',a, ' id is ',id(a))



#demo6
#just assign in local
'''
a = 6
print('id:',id(a))
def f():
    a = 3
    print('in function f() ',a)
    print('id:',id(a))
    #global a
    a = 5#another a
    print(a)
    print('id:',id(a))#another a
f()
print('after f():',a)
print(id(a))
'''