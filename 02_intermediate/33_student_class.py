# Create a class to represent a Student with attributes like name, age, and grades.

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grades}"

# Create student objects
student1 = Student("Dilakshan", 24, "A")
student2 = Student("Abirami", 22, "A+")

# Display student info
print(student1.info())
print(student2.info())
