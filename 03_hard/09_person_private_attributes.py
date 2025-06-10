# Create a class Person with private attributes and define methods to get and set the values of those attributes.

class Person:
    def __init__(self, name, age):
        self.__name = name      # Private attribute
        self.__age = age        # Private attribute

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        self.__age = age

# Example usage
person = Person("Sivanathan", 24)

print("Name:", person.get_name())
print("Age:", person.get_age())

# Updating values
person.set_name("Dilakshan")
person.set_age(25)

print("Updated Name:", person.get_name())
print("Updated Age:", person.get_age())
