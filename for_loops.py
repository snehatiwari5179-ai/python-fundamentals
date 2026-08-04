# basic for loop through a list
fruits=["Apple","Banana","Mango"]
for fruit in fruits:
    print(fruit)

# using conditional statements in a for loop
numbers=[1,2,3,4,5]
for number in numbers:
    if number % 2 == 0: # checks if the number is even;means remainder is 0
        print(number, "is even")
    else:
        print(number, "is odd")

# string iteration
name="Python"
for letter in name:
    print(letter)

column_name="customer_id"
for letter in column_name:
    print(letter)

# data engineering example
files=["data1.csv","data2.csv","data3.csv"]
for file in files:
    print("Processing file:", file)
    # Here you can add code to read and process each file