# local scope
def my_func():
    x=10
    print(x)
my_func()

# enclosing scope
def outer(): 
    x=20 # belongs to outer()
    def inner(): # inside outer()
        print(x) # dosen't have its own x, so py looks outside inner().
    inner()
outer()

# global scope
x=30  # created outside func.
def my_func():
    print(x) # dosen't have its own x, sp py looks outside func. & finds global x
my_func()

# local+global same name
x=50
def my_func():
    x=20
    print("inside:",x)
my_func()  # runs whole func.
print("outside:",x) # just prints the global

# global keyword
x=10
def change():
    global x  # we want the original global variable to become 20.
    x=25  
change()
print(x)

# nonlocal keyword
def outer():
    x=15
    def inner():
        nonlocal x      # says: use the x from outer()
        x=50       # changes that outer x
    inner()
    print(x)
outer()

