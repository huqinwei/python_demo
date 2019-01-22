#classic
#class A:
#new
class A(object):
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
