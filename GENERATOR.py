# Generator = function that produces values one at a time.
# BASIC
def numbers():  # creates a generator function
    yield 10     # gives 10 and pauses
    yield 15     # continues and gives 20
    yield 20      # continues and gives 30
gen = numbers()   # creates the generator object

print(next(gen))
print(next(gen))
print(next(gen))

print("______________________________________")

# generator expression
# The parentheses + for, automatically create a generator, so no use of yield.

squares=(x*x for x in range(6))  # creates squares one at a time
print(next(squares))  # gets first square - 0
print(next(squares))  # gets next square - 1
print(next(squares))  # gets next square - 4

print("______________________________________")

# LARGE_DATA generator
def large_data(n):
    for i in range(n):
        yield i
data=large_data(1000000)
print(next(data))  # value is 0
print(next(data))  # value is 1
print(next(data))  # value is 2

print("______________________________________")

# FIBONACCI example
def fibonacci():   # creates Fibonacci generator
    a,b=0,1        # starts with 0 and 1
    while True:     # keeps generating numbers
        yield a     # gives current a, then pauses
        a,b=b,a+b   # moves to the next Fibonacci values
fib=fibonacci()      # creates the generator
print(next(fib))     
print(next(fib))
print(next(fib))    # next() is a built-in Python function
print(next(fib))
print(next(fib))
print(next(fib))