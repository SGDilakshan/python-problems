# Create a base class Animal with a method sound() and create derived classes Dog and Cat with their own sound()

class Animal:
    def sound(self):
        print("Animal is sounding")

class Dog(Animal):
    def sound(self):
        print("Dog is barking")

class Cat(Animal):
    def sound(self):
        print("Cat is meowing")

# Creating instances
animal = Animal()
dog = Dog()
cat = Cat()

# Calling their respective sounds
animal.sound()
dog.sound()
cat.sound()
