# basic 
def my_decorator(function):
    def wrapper():
        print("before func")
        function()
        print("after func")
    return wrapper   # gives the wrapped function back
@my_decorator  # The special thing is @, not the name my_decorator.
def greet():
    print("hello")
greet()

# example 2
def log_pipeline(function):
    def wrapper():
        print("pipeline started")
        function()
        print("pipeline finished")
    return wrapper

@log_pipeline
def load_data():
    print("loading....")

load_data()

print("__________________________________")

# multiple decorators calls
# two decorators example
def first(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper
def second(function):  # bottom decorator is applied first.
    def wrapper():
        print("before2")
        function()
        print("after2")
    return wrapper

@first
@second
def greet():
    [print("hello")]
greet()

print("____________________________________")

# arguments in decorated func.
def my_decorator(func):
    def wrapper(name):
        print("before")
        func(name)
        print("after")
    return wrapper

@my_decorator
def greet(name):
    print("hello",name)
greet("Sweety")

print("____________________________________")

# *ARGS AND **KWARGS IN DECORATORS
# with *args
def my_decorator(func):
    def wrapper(*args):
        print("before")
        func(*args)
        print("after")
    return wrapper
@my_decorator
def add(a,b):
    print(a+b)
add(5,3)

# with **kwargs
def my_decorator(func):
    def wrapper(**kwargs):
        print("before2")
        func(**kwargs)
        print("after2")
    return wrapper
@my_decorator
def greet(name):
    print("hello",name)
greet(name="Sneha")

print("____________________________________")

# decorator with an argument
def repeat(times):
    def decorator(func):
        def wrapper():
            for i in range(times):
                func()
        return wrapper
    return decorator
@repeat(3)  # The 3 belongs to the decorator
def greet():
    print("hello")
greet()

print("____________________________________")

# Preserving Function Metadata

  # Python has a built-in module called functools. We take wraps from it so we can use:

from functools import wraps
def decorator(function):
    @wraps(function)
    def wrapper():  # creates the new function around the original.

        function()  #  runs the original function.
    return wrapper

@decorator
def load_data():  # applies the decorator to load_data.
    """Loads customer data."""
    print("Loading data")

load_data() # actually runs wrapper(), wrapper runs original load_data()

print(load_data.__name__)  # asks for function's name
print(load_data.__doc__)   #  asks for function's description.