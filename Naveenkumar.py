# # 1. Bank Account Class (with 5 bugs)
# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount > 0:           
#             self.__balance += amount  
#         else:
#             print("Deposit must be positive")

#     def withdraw(self, amount):
#         if amount <= 0:          
#             print("Withdraw amount must be positive")
#         elif amount > self.__balance: 
#             print("Insufficient funds")
#         else:
#             self.__balance -= amount  

#     def get_balance(self):
#         return self.__balance

# account = BankAccount("Arun", 1000)
# account.deposit(500)
# account.withdraw(300)
# print("Balance:", account.get_balance())

# # -------------------------------------------------------------------------------------------

# # 2. Employee and Manager (Inheritance) 
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def display(self):
#         print(f"Employee: {self.name}, Salary: {self.salary}")

# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name , salary)
#         self.department = department

#     def display(self):
#         print(f"Manager: {self.name}, Salary: {self.salary}, Department: {self.department}")

# emp = Employee("Ravi", 50000) 
# mgr = Manager("Kumar", 90000, "IT")

# emp.display()
# mgr.display()

# Employee: Ravi, Salary: 50000
# Manager: Kumar, Salary: 90000, Department: IT
# # -------------------------------------------------------------------------------------------

# # 3. Class and Static Methods (with 5 bugs)
# class Demo:
#     count = 0

#     def __init__(self):
      
#         Demo.count += 1

#     @classmethod
#     def get_instance_count(cls):
       
#         return cls.count

#     @staticmethod
#     def greet():
#         print("Hello from Demo class!")

# d1 = Demo()
# d2 = Demo()

# print("Instances created:", Demo.get_instance_count())

# d1.greet()

# Expected Output:

# Instances created: 2
# Hello from Demo class!

# # -----------------------------------------------------------------------------------------------

# # 4. Operator Overloading 
# # Question:
# # Create a Point class to represent (x, y) coordinates and overload the + operator to add two points.
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
    
#         return Point(self.x + other.x, self.y + other.y)

#     def __str__(self):
#         return f"{self.x}, {self.y}"

# p1 = Point(2, 3)
# p2 = Point(4, 5)
# p3 = Point(1,2)
# p4 = p1 + p2 + p3


# print("Sum of points:", p4)

# # -----------------------------------------------------------------------------------------

# # 5. Encapsulation with Private Attributes 
# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.__grade = grade

#     def get_grade(self):
        
#         return self.__grade

#     def set_grade(self, grade):
#         if 0 <= grade <= 100:  
#             self.__grade = grade
#         else:
#             print("Grade must be between 0 and 100")

# s = Student("Ravi", 80)
# print("Initial grade:", s.get_grade())
# s.set_grade(90)
# print("Updated grade:", s.get_grade())
# s.set_grade(105)  # Invalid

# # Expected Output:

# # Initial grade: 80
# # Updated grade: 90
# # Grade must be between 0 and 100

# # ----------------------------------------------------------------------------------------------

# # 6. Polymorphism – Shapes Area 
# class Shape:
#     def area(self):
#         return 1  

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
       
#         return 3.14 * self.radius ** 2

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
        
#         return self.side ** 2

# shapes = [Circle(5), Square(4)]
# for shape in shapes:
#     print("Area:", shape.area())

# # Expected Output:

# # Area: 78.5
# # Area: 16

# # ---------------------------------------------------------------------------------------------

# # 7. Abstract Class and Method (with 5 bugs)
# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         print("Animal sound")  
#         pass

# class Dog(Animal):
#     def sound(self):
#         return "Bark"

# class Cat(Animal):
#     def sound(self):
#         return "Meow"

# dog = Dog()
# cat = Cat()


# print("Dog:", dog.sound())
# print("Cat:", cat.sound())

# # Dog: Bark
# # Cat: Meow

# # ----------------------------------------------------------------------------------------------

# # 8. Property Decorators (with 5 bugs)
# class Product:
#     def __init__(self, price):
#         self.__price = price  

#     @property
#     def price(self):
#         return self.__price  

#     @price.setter
#     def price(self, value):
#         if value > 0:  
#             self.__price = value
#         else:
#             print("Price cannot be negative")

# p = Product(100)
# print("Initial price:", p.price)
# p.price = 120
# print("Updated price:", p.price)
# p.price = -50  # Invalid

# # Expected Output:

# # Initial price: 100
# # Updated price: 120
# # Price cannot be negative

# # -------------------------------------------------------------------------------------

# # 9. Composition Example (with 5 bugs)
# class Engine:
#     def start(self):
#         print("Engine started")  

# class Car:
#     def __init__(self):
#         self.engine = Engine()
        
#     def drive(self):
#         self.engine.start()
#         print("Car is moving")

# car = Car()
# car.drive()

# Expected Output:

# Engine started
# Car is moving



# # -----------------------------------------------------------------------------------------------
# # 10. Custom Iterator Class (with 5 bugs)
# class Countdown:
#     def __init__(self, start):
#         self.current = start

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current < 1:  
#             raise StopIteration
#         val = self.current
#         self.current -= 1    
#         return val

# for num in Countdown(5):
#     print(num)