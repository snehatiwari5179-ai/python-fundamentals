# basic example
for i in range(8):
    for j in range(4):
        print(i, j)

# medium example
colors=["white","blue"]
cars=["bmw","audi"]
for color in colors:
    for car in cars:
        print(color,cars)

# data eng. example
files=["sales.csv", "inventory.csv", "customers.csv"]
for file in files:
    print("processing:",file)
    for record in range(3):
        print("record:",record)