#try finally
#demo1
# def f():
#     try:
#         print('try print 1')
#         return 1
#     finally:
#         print('finally!!!')
#         return 0
# print('f()\'s return is :', f())

#demo2
# def f():
#     try:
#         print('try print')
#         return 1
#     finally:
#         print(0)
# print('ret:',f())

# demo3
# def f():
#     try:
#         print('try')
#         return 1
#     except:
#         return 2
#     else:
#         print('else')
#         return 3
#
#     finally:
#         print(0)
# print('ret:', f())


# demo3.2 try without return
# def f():
#     try:
#         print('try')
#     except:
#         return 2
#     else:#this will be execute
#         print('else')
#         return 3
#
#     finally:
#         print(0)
# print('ret:', f())



#demo other
def test_finally_return1():
    try:
        print(1)
        return 1
    finally:
        print(0)
        return 0
print('test1 return:',test_finally_return1())

def test_finally_return2():
    try:
        print(1)
        return 1
    finally:
        print(0)
print('test2 return:',test_finally_return2())

def test_else_finally_return3():
    try:
        print(1)
        return 1
    except:
        return 2
    else:
        print(3)
        return 3
    finally:
        print(0)
print('test3 return:',test_else_finally_return3())

def test_else_finally_return4():
    try:
        print(1)
        return 1
    except:
        return 2
    else:
        print(3)
        return 3
    finally:
        print(0)
        return 0
print('test4 return:',test_else_finally_return4())

def test_else_finally_return5():
    try:
        print(1)
    except:
        return 2
    else:
        print(3)
    finally:
        print(0)
        return 0
print('test5 return:',test_else_finally_return5())


def test_else_return6():
    try:
        print(1)
        return 1
    except:
        return 2
    else:
        print(3)
        return 3


print('test6 return:', test_else_return6())


def test_else_return7():
    try:
        print(1)
    except:
        return 2
    else:
        print(3)
        return 3


print('test7 return:', test_else_return7())


#summary:finally is the boss,write return in finally!!!!!!!!!!!!!!!!











