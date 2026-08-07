# basic example
def greet(): # def used for creating func. ; greet is the name of the function ; () means this func. dosen't need any info for now.

    print("Hello Sneha !")
    
greet()

# medium example
def welcome():
    print("Welcome to the world of Python !")
welcome()
welcome() # calling the function 

print("____________________________")

# python Arguments

def greet(name): # name is the argument of the function greet
    print("hello",name)
greet("Sneha") # calling the function greet and passing the value of name as Sneha

# medium example
def square(num):
    print(num*num) 
square(5) # calling the function square and passing the value of num as 5

print("____________________________")

# number of arguments
# example
def student_info(name,age):
    print("name:",name)
    print("age:",age)
student_info("Sneha",20) # calling the function student_info and passing the values of name and age

# default parameter value
# example 1
def greet(name="Sweety"):
    print("hello",name)
greet() # calling the function greet without passing any value for name, so it will take the default value "Sweety"

# example 2
def read_data(file_name,file_type="CSV"):
    print("reading:",file_name)
    print("file type:",file_type)
read_data("sales.csv") # value given for file_name and default value will be taken for file_type
read_data("users.json","JSON") # values given for both parameters.

# keyword arguments
# example 1
def student(name,age):
    print(name,age)
student(age=22,name="Sneha") # parameter name given while calling. 

# example 2
def product(name,price,quantity):
    print("product:",name)
    print("price:",price)
    print("quantity:",quantity)
product(price=100,quantity=5,name="Laptop")

# positional arguments
def student(name,age,course):
    print(name)
    print(age)
    print(course)
student("Sneha",20,"Python") # values are passed in the same order as the parameters are defined in the function.

# mixing positional & keyword 

def product(name,price,quantity):
    print(name)
    print(price)
    print(quantity)
product("Laptop",price=50000,quantity=2) # first value is positional and the rest are keyword arguments.

# passing diff. data types as arguments
# string example
def show(data):
    print(data)
show("Prince")

# integer example
def show(data):
    print(data)
show(22)

# List example
def show(data):
    print(data)
show(["Python","SQL","Git"])

# dictionary example
def show(data):
    print(data)
show({"name":"Maan Singh Khurrana","age":30})

# return values
# example 1
def add(a,b):
    return a+b
result=add(5,5) # calling the function add and storing the return value in result
print(result)

# example 2
def square(num):
    return num*num
answer=square(5) # calling the function square and storing the return value in answer
print(answer)

# data eng. example
def get_file_name():
    return "sales.csv"
file_name=get_file_name()
print(file_name)

# returning diff. DB
# string return
def get_name():
    return "Sneha"
print(get_name())

# List return
def get_skills():
    return["Python","SQL","Git"]
print(get_skills())

# Dict. return
def get_student():
    return{
        "name":"Sneha",
        "course":"BCA"
    }
print(get_student())

# positional-only
def student(name,age,/):  # parameters before / can only receive values by position.
    print(name)
    print(age)
student("sneha",22)

# keyword-only
def student(*,name,age):
    print(name)
    print(age)
student(name="sneha",age=22)

# combining both P & K
def student(name,/,age,*,course):
    print(name)
    print(age)
    print(course)
student("Sweety",22,course="BCA")