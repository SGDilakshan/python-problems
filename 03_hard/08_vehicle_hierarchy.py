# Implement a class hierarchy to represent different types of vehicles (Car, Bike) with their own attributes and methods.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        return super().display_info() + f", Number of doors: {self.num_doors}"

    def start(self):
        return "Car started."

class Bike(Vehicle):
    def __init__(self, make, model, year, bike_type):
        super().__init__(make, model, year)
        self.bike_type = bike_type

    def display_info(self):
        return super().display_info() + f", Bike type: {self.bike_type}"

    def kick_start(self):
        return "Bike kick-started."

# Example usage
car = Car("Toyota", "Camry", 2020, 4)
bike = Bike("Honda", "CBR500R", 2021, "Sports")

print(car.display_info())
print(car.start())

print(bike.display_info())
print(bike.kick_start())
