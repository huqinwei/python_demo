class C(object):

    global_value = 0
    
    @staticmethod
    def static_method(str='anonymous'):
        print('hello ',str)
    def object_method(self):
        print('hello object')


c = C()
C.static_method('huqw')
#C.object_method()
c.static_method()
c.object_method()
