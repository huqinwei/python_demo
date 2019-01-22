import math
class Circle:
    def __init__(self,radius):
        self.radius=radius

    @property
    def area(self):
        return math.pi * self.radius**2
    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(10)
print(c.area)
#print(c.area())#float object is not callable
print(c.perimeter())
print(c.perimeter)
