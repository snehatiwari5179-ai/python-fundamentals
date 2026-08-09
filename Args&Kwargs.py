# With *args, one function handles any number of values.

# example 1

def fruit(*args): # args is just a name. You can give it another name.
    print(args)
fruit("apple","mango","banana")

# example 2
def fruits(*args):
    print(args[0]) # first item
    print(args[1]) # second item
fruits("apple","mango","cherry")

# example 3
def load_files(*files):
    for file in files:       # The for loop takes one item at a time from files.
        print("loading:",file)
load_files("sales.csv","customers.csv","orders.csv")

# using *args with regular 
# example 1
def student(name,*skills): #*args must come after the regular parameter.
    print(name)
    print(skills) 
student("sneha","Python","SQL","Git")   

# example 2
def student(name,*skills):
    print("Student:",name)
    for skill in skills:
        print("Skill:",skill)
student("Sweety","Python","SQL","Git")

# With **kwargs one function handles any number of keyword arguments.

# example 1
def student(**kwargs): #  kwargs is just a variable name; it can be changed.
    print(kwargs)
student(name="Kiran",age=37,city="Kolkata")

# example 2
def student(**kwargs):
    print(kwargs["name"])
    print(kwargs["city"])
student(name="Amar",age=40,city="Kolkata")

# Using **kwargs with Regular Arguments
def student(name,**details):
    print(name)
    print(details)
student("Sneha",age=22,city="Kolkata",course="BCA")

# Combining *args and **kwargs
def student(*args,**kwargs): # python seperates them.
    print("positional:",args)
    print("keyword:",kwargs)
student("Raj","BCA",age=26,city="Delhi")

# Unpacking Arguments
# The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.

# *unpacking
def add(a,b,c):
    print(a+b+c)
numbers=(10,20,30)
add(*numbers)

# **unpacking
def student(name,age,course):
    print(name,age,course)
details = {
    "name":"Sneha",
    "age":22,
    "course":"BCA"
}
student(**details)

