class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("total employee %d"%Employee.empCount)

    def displayEmployee(self):
        print("Name:",self.name,",Salary:",self.salary)

liuyang = Employee('shabi',250)
liuxiaofei = Employee('weak',200)

liuyang.displayEmployee()
Employee.displayEmployee(liuyang)

Employee.displayCount(liuyang)
liuyang.displayCount()
print("direct access:",Employee.empCount)

Employee.new_static = 20
Employee.new_static = 30

print("object access new static:",liuyang.new_static)
liuyang.new_static = 5
print("object modify new static:",liuyang.new_static)
print("class access new static:",Employee.new_static)
print("object has attr:",hasattr(liuyang,'new_static'))
print("object get attr:",getattr(liuyang,'new_static'))

liuxiaofei.fake_static2 = 10
print("object add new local(is not static):",liuxiaofei.fake_static2)
liuxiaofei.fake_static2 = 5
print("object modify static:",liuxiaofei.fake_static2)

print("object has attr:",hasattr(liuyang,'fake_static2'))
#print("object access object's fake_static2:",liuyang.fake_static2)
#print("class access object's fake_static2:",Employee.fake_static2)












