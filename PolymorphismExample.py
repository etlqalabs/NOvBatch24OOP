
# Polymorphism implemetation ways
# Way 1:  Not allowed in python
class MethodOverloading:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c
    def add(self,a,b,c,d):
        return a+b+c+d

obj = MethodOverloading()
#print(obj.add(1,2,3))  # not allowed
#print(obj.add(1,2,3,4)) # works well

# Way 2 Method overiding ( with inheritance)
# case 1
class Bird:
    def fly(self):
        print("Bird flies")

class Penguinue(Bird):
    def fly(self):
        print("Penguine can't fly")

p = Penguinue()
p.fly()
''''
# case 2:
# case 1
class Bird:
    def fly(self):
        print("Bird flies")

class Penguinue(Bird):
    pass

p = Penguinue()
p.fly()

# case 3:
class Bird:
    def fly(self):
        print("Bird flies")

class Penguinue(Bird):
    def fly(self):
        print("Penguine can't fly")
b = Bird()
b.fly()

'''

# Way 3 Class Overriding ( without inheritance )
class Circle:
    def area(self):
        print("are of circle")

class Rectangle:
    def area(self):
        print("are of Rectangle")

class Triangle:
    def area(self):
        print("are of triangle")

shapes = [Circle(),Rectangle(),Triangle()]
for shape in shapes:
    shape.area()

