# basic example
fruits=["Apple","Banana","Mango","Grapes"]
for fruit in fruits:
    if fruit == "Mango":
        break
    print(fruit)

# medium example
numbers=[10,20,30,40,50]
for number in numbers:
    if number == 30:
        break
    print(number)

# data eng. example
files=["sales.csv","inventory.csv","customers.csv","orders.csv"]
for file in files:
    if file == "customers.csv":
        print("Corrupted file found")
        break
    print(file)