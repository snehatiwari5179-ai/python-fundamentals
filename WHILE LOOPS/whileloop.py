# while loop
# example 1
i=1
while i<=5:
    print(i)
    i += 1  # without this line, the loop will run infinitely because the condition will always be true.

print("___________________________________")

# example 2
number=10
while number <=15:
    print(number)
    number += 1  # incrementing the number to avoid infinite loop  

print("___________________________________")

# data eng. example
record=1            # start checking records from 1
while record <= 5:  # process records until 5
    print(f"Processing record {record}")
    record += 1  # incrementing the record to avoid infinite loop.