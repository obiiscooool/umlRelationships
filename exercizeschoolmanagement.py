from os import name


class Person:
    def __init__(self, name, age, type):
        self.name = name
        self.__age = age
        self.type = type
        if type == "student":
            self.student = Student(self.name,self.__age)
        else:
            self.teacher = Teacher(self.name,self.__age)

    def get_age(self):
        return self.__age
    
class Student(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def study(self):
        return (f"{self.name} is studying.")
    
class Teacher(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def teach(self):
        return (f"{self.name} is teaching.")
person1 = Person("Abz", 30, "Teacher")
print(person1.name)
print(person1.get_age())
print(person1.teacher.teach())
#__age is better than age because it is 
#private and cannot be accessed directly from outside the class.