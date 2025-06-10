# Write a program that uses a Person class to keep track of a person’s name, age, and address.

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_info(self):
        return f"{self.name} is {self.age} years old and lives in {self.address}."

# Create Person objects
person1 = Person("Dilakshan", 24, "Jaffna")
person2 = Person("John", 23, "Sri Lanka")
person3 = Person("Pavithira", 21, "Japan")

# Display info
print(person1.display_info())
print(person2.display_info())
print(person3.display_info())
