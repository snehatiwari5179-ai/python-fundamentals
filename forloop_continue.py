# basic example
fruits=["Apple","Banana","Mango","Grapes"]
for fruit in fruits:
    if fruit=="Mango": # skips mango and continues with the next iteration of the loop
        continue
    print(fruit)

# medium example
numbers=[1,2,3,4,5]
for number in numbers:
    if number % 2 == 0:
        continue
    print(number)

# data eng. example
files=["sales.csv","inventory.csv","customers.csv","orders.csv"]
for file in files:
    if file == "customers.csv":
        print("skipping...")
        continue
    print(file)