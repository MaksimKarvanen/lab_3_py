from abc import ABC, abstractmethod # Импорт абстрактного базового класса и декоратора abstractmethod из модуля abc
import math

#-------------------------------A-------------------------------
class Person:
    # Конструктор класса, инициализирует объект с именем и возрастом
    def __init__(self, name, age):
        # Публичные атрибуты объекта
        self.name = name # Имя
        self.age = age # Возраст

    # Метод для получения имени
    def getName(self):
        return self.name # Возвращает текущее значение поля name
    
    # Метод  для установки нового имени
    def setName(self, name):
        self.name = name

    def printInfo(self):
        print(f"Имя: {self.name}, Возраст: {self.age}") # f-строка для форматированного вывода


#-------------------------------B-------------------------------
# Класс Student, наследующий от Person
class Student(Person):
    def __init__(self, name, age, studentID):
        super().__init__(name, age) # Вызов конструктора родительского класса
        self.studentID = studentID # Добавление нового атрибута StudentID

    def getStudentID(self):
        return self.studentID
    
    # Переопределенный метод вывода информации
    def printInfo(self): 
        super().printInfo() # Вызываем метод родительского класса
        print(f"Student ID: {self.studentID}")


#-------------------------------C-------------------------------
class Shape(ABC):
    # Абстрактный метод, который должны реализовать все наследники
    @abstractmethod
    def calculateArea(self):
        pass # Заглушка


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width # Широта
        self.height = height # Высота

    def calculateArea(self):
        return self.width * self.height # Возвращаем площадь
    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius # Радиус

    def calculateArea(self):
        return math.pi * self.radius ** 2 # площадь окружности - pi * R^2
        
        
#-------------------------------D-------------------------------
class Account:
    def __init__(self):
        self.__balance = 0 # Приватное поле баланса (изначально 0)

    # Пополнение
    def deposit(self, amount):
        if amount > 0: # Проверка, что сумма положительна
            self.__balance += amount # Увеличиваем баланс
    
    # Снятие
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Ошибка вывода") # Если снятие превышает лимит

    def getBalance(self):
        return self.__balance