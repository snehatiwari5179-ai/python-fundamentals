# 1. CLASS + OBJECT + __init__() + self

class Person :                              # class → blueprint


     country = "India"                 # class variable → shared

     def __init__(self,name,age):   # __init__ → runs when object is created
          
          self.name = name          # self → current object
          self.age = age             # instance attributes

     def introduce(self):          # method → function inside class
          print("My name is",self.name)
          print("My age is", self.age)
     def greet(self):                    # method
          print("Hello,I am",self.name)

# Object → actual thing created from class
person1 = Person("Sneha",22)
person2 = Person("Abhishek",24)

# Accessing attributes
print(person1.name)
print(person1.age)
print(person2.name)
print(person2.age)

print("=============================================")

# Accessing class variable
print(person1.country)         # country → class variable
print(person2.country)

print("=============================================")

# Calling methods
person1.greet()                     # call method
person2.greet()

person1.introduce()

print("=============================================")

# 2. CHANGING AN ATTRIBUTE
person1.name = "Yash"
print(person1.name)

print("=============================================")

# 3. ADDING A NEW ATTRIBUTE
person1.city = "Kolkata"
print(person1.city)

print("=============================================")

# 4. DELETING AN ATTRIBUTE
del person1.city

# 5. INHERITANCE
class Student(Person):        # Student → child
                              # Person → parent

     def study(self):         # Student's own method
          print(self.name,"is studying")

student1 = Student("Sweety",22)

student1.greet()               # inherited method
student1.introduce()           # inherited method
student1.study()              # Student's own method

print("=============================================")

# 6. SUPER()
class Student2 (Person):       # child class

     def __init__(self,name,age,course):
          super().__init__(name,age)    # super() → call parent's __init__()
          self.course = course          # child's own attribute

     def study(self):
          print(self.name,"is studying",self.course)

student2 = Student2("Sweety Tiwari",22,"Data Analysis")

print(student2.name)        # inherited attribute
print(student2.age)         # inherited attribute
print(student2.course)      # child's attribute

student2.study()

print("=============================================")

# 7. METHOD OVERRIDING
class Coder (Person):         # Coder inherits Person

     def introduce(self):     # overriding → own version
          print("I am a Coder.")
          print("My name is",self.name)

coder1 = Coder("Sneha",22)

coder1.introduce()        # Coder's version runs

print("=============================================")

# POLYMORPHISM
class Dog :
     def sound(self):
          print("Bark")
class Cat :
     def sound(self):
          print("Meow")  # Same method name → different behavior
dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

print("=============================================")


# 9. POLYMORPHISM WITH INHERITANCE
class Animal :
     def sound(self):
          print("animal sound")

class DogAnimal(Animal):
     def sound(self):                   # overriding
          print("barkkk")

class CatAnimal(Animal):
     def sound(self):                   # overriding
          print("meowww")

dog = DogAnimal()
cat = CatAnimal()

dog.sound()
cat.sound()       # Same method call → different behavior

print("=============================================")

# 10. ENCAPSULATION
class BankAcc :

     def __init__(self,balance):       # receives starting balance

          self.__balance = balance      # store balance privately

     def show_balance(self):         # method to show balance
          print(self.__balance)      # print private balance

     def deposit(self,amount):      # method to add money

          if amount > 0:            # # check if amount is positive
               self.__balance += amount      # add money to pvt balance

account = BankAcc(1000)  # create object with 1000 balance

account.show_balance()

account.deposit(500)       # deposit 500
account.show_balance()

print("=============================================")

# 11. ABSTRACTION
from abc import ABC, abstractmethod     # import abstraction tools

class Animal2(ABC):      # abstract class

     @abstractmethod      # abstract method
     def sound(self):
          pass                 # child must implement this

class Dog2(Animal2):
     def sound(self):
          print("Bark")

class Cat2(Animal2):
     def sound(self):
          print("Meow")

dog2 = Dog2()
cat2 = Cat2()

dog2.sound()
cat2.sound()

print("=============================================")

# 12. POLYMORPHISM + ABSTRACTION TOGETHER
animals = [Dog2(),Cat2()]        # list of different objects

for animal in animals:
     animal.sound() # same method call, different behavior

print("=============================================")