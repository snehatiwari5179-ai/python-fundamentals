import calculator
print(calculator.add(5,3))

print("____________________________")

# use a module
import mymodule  # imports mymodule.py
mymodule.greet("Sneha")  # uses greet() 
print(mymodule.person1["age"])  # gets & prints the age from person1

print("____________________________")

# rename/alias a module
import mymodule as MX # gives shorter name to mymodule
print(MX.person1["age"]) # uses MX to access person1

print("____________________________")

# import from module
from mymodule import person1 # imports only person1 directly
print(person1["age"])   # uses person1 directly

print("____________________________")

# built-in module
import platform      # Imports Python's built-in platform module
print(platform.system())  # Prints the operating system name

print("____________________________")

# dir()
print(dir(platform))  # shows the names available inside platform.

print("example 2---------------")

print(dir(mymodule))  # shows the names available inside mymodule which you created.