class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name)
        print("destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1
print(id(pt1),id(pt2),id(pt3))

print('del pt1')
del pt1
print('del pt2')
del pt2
print('del pt3')
del pt3


p8 =Point(3,3)
p9 = p8
p8 = p9
print(id(p8),id(p9))
print('del pt8')
del p8
print('del pt9')
del p9

print('game over')
