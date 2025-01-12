class Vehicle:
#parameterized constructor
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"{self.brand} {self.model} started")
        #print(self.brand,self.model," started")
    def stop_engine(self):
        print(f"{self.brand} {self.model} stopped")

class Car(Vehicle):
    def __init__(self,brand,model,fuel_type):
        super().__init__(brand,model)
        self.fuel_type = fuel_type

    def honk(self):
        print(f"{self.model} {self.brand} is honking: beep beep")

    def start_engine(self):
        print(f"{self.brand} {self.model} started with {self.fuel_type}")

class ElecticCar(Vehicle):
    def __init__(self,brand,model,battery_capacity):
        super().__init__(brand,model)
        self.battery_capacity = battery_capacity
    def charge(self):
        print(f"{self.model} {self.brand} is charging")

# Object creation of difference class

# create an object of the Vehcile class ( Parent class )

vehicle = Vehicle("Toyota","Camry")
vehicle.start_engine()

# Create an object of the Car class ( child class ) and see we can use the existing mrthods from Parent ( Vehcicle class )

car = Car("Honda","Honda civic","Petrol")
car.start_engine()

electricCar = ElecticCar("Tesla","ModelS",100)
electricCar.start_engine()









