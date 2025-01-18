# Abstrcation is hiding the complexity of the system from the end user
# Java - achieved using interface and abstrct classes
# Python - acheived using abstract class
from abc import abstractmethod, ABC
class Vehicle(ABC):
    def __init__(self,numberofTyres):
        self.numberofTyres = numberofTyres

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stops(self):
        pass

class Car(Vehicle):
    def __init__(self):
        super().__init__(4)
    def start(self):
        print("Car starts...")

class MarutiSuzuki(Car):
    def stops(self):
        print("Maruti suzuki stops..")

class Bike(Vehicle):
    def __init__(self):
        super().__init__(2)

    def start(self):
        print("Bike starts...")

class Bullet(Bike):
    def stops(self):
        print("Bullet stops ...")
c = MarutiSuzuki()
c.start()
c.stops()
b = Bullet()
b.start()
b.stops()