# Inheritance (Is-a)
class Animal:
    def __init__(self, name: str):
        self.name = name
        pass

class Cat(Animal):
    def meow(self):
        return f"{self.name} meows"
    
my_cat = Cat("candy")

print(my_cat.meow())

# Composition (Strong Has-a)

class Book:
    def __init__(self, name: str):
        self.name = name

class Library():
    def __init__(self):
        self.Books = [Book("Hunger games"), Book("Diary of a wimpy kid")]

Library_of_Mandaue = Library()

for book in Library_of_Mandaue.Books:
    print(f"Library has {book.name}")

# Aggregation (Weak Has-a)

class Teacher:
    def __init__(self, name: str):
        self.name = name

class Department:
    def __init__(self, name: str, teachers: list):
        self.name = name
        self.teachers = teachers

teacher1 = Teacher("Mr. Smith")
teacher2 = Teacher("Mrs. Davis")

Math_Department = Department("Math", [teacher1, teacher2])

for teacher in Math_Department.teachers:
    print(f"Department has {teacher.name}")

# Association (Knows-a)

class Doctor:
    def __init__(self, name: str):
        self.name = name

class Patient:
    def __init__(self, name: str):
        self.name = name

doctor_1 = Doctor("Dr. John")
patient_1 = Patient("Alice")

print(f"Patient {patient_1.name} sees Doctor {doctor_1.name}")

# Dependency (Uses-a)

class Printer:
    def print_file(self, file_name: str):
        print(f"Printing {file_name}")

class Document:
    def print_document(self, printer: Printer):
        printer.print_file("MyDocument.pdf")

my_printer = Printer()
my_document = Document()

my_document.print_document(my_printer)

# Realization/Implementation (Implements)

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

my_circle = Circle()
my_circle.draw()