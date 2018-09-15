class people:
    name = ''
    age = 0
    __weight = 0

    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s said: i'm %d old!"%(self.name,self.age))

class student(people):
    def __init__(self,n,a,w,g):
#        super(student,self).__init__(n,a,w)
        people.__init__(self,n,a,w)
#        people.__init__(self,n,a,w)
        self.grade = g

    def speak(self):
        print("%s said: i'm %d old! grade %d"%(self.name,self.age,self.grade))


s = student('kent',10,60,3)
s.speak()
