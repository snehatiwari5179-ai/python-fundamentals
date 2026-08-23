# BASIC None
x = None
print(x)

print("===============================")

# Checking None
x = None
if x is None:
    print("No Value")

print("===============================")

# Value exists
x = 10
if x is None:
    print("NoValue")
else:
    print("Value exists")

print("===============================")

# None vs Empty String
x = None
y = ""
print(x)
print(y)

print("===============================")

# None vs Zero
x = None
y = 0
print(x)
print(y)

print("===============================")

# Func. returning None
def hello():
    print("hello")

result=hello() # prints "Hello" but returns nothing → None.
print(result)

print("===============================")