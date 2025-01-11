class Student:
    def __init__(self,name,companyName):
        self.name = name
        self.companyName = companyName

    def joinClass(self):
        print(f"{self.name} Join the class")
    def completeAssigments(self):
        print(f"{self.name} complete the assigments")

bala = Student("Bala","Amazon")
print(" my name is : ",bala.name)
bala.joinClass()
bala.completeAssigments()

hetu = Student("Hetu","Google")
print(" my name is : ",hetu.name)
hetu.joinClass()
hetu.completeAssigments()