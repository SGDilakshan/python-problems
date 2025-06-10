# Create a class to represent a Car with attributes like make, model, and year.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"This car is a {self.year} {self.make} {self.model}."

# Create car objects
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2018)

# Display car info
print(car1.display_info())
print(car2.display_info())
