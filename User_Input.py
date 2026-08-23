# Basic USER INPUT
name = input()      # there is no message telling you what to enter
print(name)         # program pauses until user enters something.

print("========================")

# using PROMPT
name = input("Enter your Name--")   # msg shown what to enter
print(f"hello ! {name}")

print("========================")

# multiple inputs
name = input("Name:")
age = input("age:")     # input() always returns a str.
print(name)
print(age)

print("========================")

# INTEGER Input
age = int(input("AGE:"))    # int() → converts str. to int.
print(age + 1)           # arithmetic → adds 1

print("========================")

# FLOAT / DECIMAL INPUT
price = float(input("Price:"))  # float() → converts to decimal
print(price*2)  # multiplies by 2

print("========================")

# VALIDATE INPUT
while True:
    try:
        num = float(input("enter no.:"))   # gets user input, convert to decimal
        break                            # stops loop when input is valid
    except ValueError:
        print("Wrong Input,try again.")  # shows error message.
        
print("========================")