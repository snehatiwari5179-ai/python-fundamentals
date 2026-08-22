# BASIC try....except
try:
    print(10/0)          # TRY: risky operation
except:
    print("An error occurred")         # EXCEPT: handle error

print("================================")

#  ZeroDivisionError
try:
    result = 10 / 0       # TRY: division by zero
except ZeroDivisionError:
    print("Cannot divide by zero")      # HANDLE: zero division

print("================================")

# ValueError
try:
    number =  int("hello")      # TRY: convert text to int
except ValueError:
    print("Invalid value")       # HANDLE: invalid value

print("================================")

# TypeError
try:
    result = "10" + 5       # TRY: incompatible types
except TypeError:
    print("Wrong data type")        # HANDLE: TypeError

print("================================")

# FileNotFoundError
try:
    file=open("abc.py")         # TRY: open missing file
except FileNotFoundError:
    print("File not Found")      # HANDLE: missing file

print("================================")

# Multiple except
try:
    number = int(input("Enter Number:"))      # TRY: convert input
    result = 100/number                         # TRY: divide
    print("result:",result)                     # SHOW: result
except ValueError:
    print("Enter numbers only")             # HANDLE: invalid input
except ZeroDivisionError:
    print("Number cannot be zero")      # HANDLE: zero

print("================================")

#  as e — ERROR INFORMATION
try:
    number = int("abc")     # TRY: invalid conversion
except ValueError as e:     # The e is just a variable name
    print("Error:",e)         # SHOW: actual error
    
print("================================")

# else --- no ERROR
try:
    number = int("100")     # TRY: valid conversion
except ValueError:
    print("Coversion failed")       # ERROR: if conversion fails
else:
    print("Conversion successful")       # SUCCESS: no error

print("================================")

# finally ---- always RUN
try:
    print(10/2)     # TRY: successful division
except ZeroDivisionError:
    print("Cannot divide by zero")  # ERROR: if division fails
finally:
    print("This always runs")       # ALWAYS: executes

print("================================")

#  Exception as e
try:
    result = 10/0
except Exception as e:   # Exception - Catches general/normal exception
    print("Error:",e)        # SHOW: error information

print("================================")

#  PRACTICAL USER INPUT
try:
    age=int(input("enter your age:"))   # INPUT: convert to integer
    print("Your age is:",age)            # SHOW: valid age
except ValueError:
    print("Plz enter a valid number")    # HANDLE: invalid input

print("================================")

#  PRACTICAL CALCULATOR
try:
    a = int(input("Enter first number"))      # INPUT: first number
    b = int(input("Enter second number"))     # INPUT: second number
    result = a/b                            # CALCULATE: division
    print("Answer:",result)          # SHOW: answer
except ValueError:
    print("plz enter numbers only")     # HANDLE: bad input
except ZeroDivisionError:
    print("second number cannot be zero")     # HANDLE: zero
finally:
    print("calculation finished")       # ALWAYS: finish

print("================================")