
 #     if end_point == final_endpoint: return net, end_points

#demo1
a = 10
b = 13
if a == 10:print('b:',b), print('a:',a)

#demo2
a = 5
b = 6
if a == 3:print('b:',b), print('a:',a)

#demo3
if a == 10:
    print(b)
print(a)

#demo4
a = 5
b = 6
if a == 3:b = 100, print('a:',a)
#if a == 3:b = 100, b = 10000#SyntaxError: can't assign to literal

#demo5:return tuple
a = 3
b = 4
def func():
    #if a == 3: return a,b
    if a == 3: return 99,100
c = func()
print(type(c))
print((c))








