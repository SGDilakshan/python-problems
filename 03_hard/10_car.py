# Create a class Car with private attributes make, model, and year. Write getter and setter methods for these attributes.

class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    # Getters
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    # Setters
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year


# Example usage
car = Car("Toyota", "Corolla", 2020)
print(car.get_make(), car.get_model(), car.get_year())

car.set_year(2021)
print("Updated Year:", car.get_year())
