from classes import *

person = Person("Максим", 21) # Создание объекта класса Person
print(person.getName()) # Вывод имени
person.setName("Павел") # Изменение имени
person.printInfo() # Вывод полной информации
print()

student = Student("Карванен", 22, "KMD21") # Создание объекта класса Student
student.printInfo() 
print(student.getStudentID()) # Вывод studentID
print()

shapes = [Rectangle(4, 5), Circle(3)] # Создание списка геометрических фигур
for shape in shapes: # Итерация по списку фигур
    print(f"Area: {shape.calculateArea():.4f}") # Для каждой фигуры выводим площадь с округлением до 4 знаков
print()

account = Account() # Создание счета
account.deposit(100) # Вносим 100
account.withdraw(50) # Снимаем 50 
print("Баланс: ", account.getBalance()) # Выводим текущий баланс
account.withdraw(100) # Попытка снять больше, чем есть на счету