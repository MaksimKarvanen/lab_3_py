from abc import ABC, abstractmethod
import math

#-------------------------------A-------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def printInfo(self):
        print(f"Имя: {self.name}, Возраст: {self.age}")


#-------------------------------B-------------------------------
class Student(Person):
    def __init__(self, name, age, studentID):
        super().__init__(name, age)
        self.studentID = studentID

    def getStudentID(self):
        return self.studentID
    
    def printInfo(self):
        super().printInfo()
        print(f"Student ID: {self.studentID}")


#-------------------------------C-------------------------------
class Shape(ABC):
    @abstractmethod
    def calculateArea(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculateArea(self):
        return self.width * self.height
    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculateArea(self):
        return math.pi * self.radius ** 2
        
        
#-------------------------------D-------------------------------
class Account:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Ошибка вывода")

    def getBalance(self):
        return self.__balance