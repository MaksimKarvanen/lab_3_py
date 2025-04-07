from classes import *

person = Person("Максим", 21)
print(person.getName())
person.setName("Павел")
person.printInfo()
print()

student = Student("Карванен", 22, "KMD21")
student.printInfo()
print(student.getStudentID())
print()

shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print(f"Area: {shape.calculateArea():.2f}")
print()

account = Account()
account.deposit(100)
account.withdraw(50)
print("Баланс: ", account.getBalance())
account.withdraw(100)