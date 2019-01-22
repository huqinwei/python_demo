class Test:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def prt(huqinwei):
        print(huqinwei)
        print(huqinwei.__class__)

    def print_x(self):
        print(self.x)
    def print_y(hu):
        print(hu.y)
    def print_default(hu):
        print(hu)


ha = Test(55,66)
ha.prt()
ha.print_x()
ha.print_y()
ha.print_default()
#ha.print_default('fuck')
Test.print_default('fuck')
