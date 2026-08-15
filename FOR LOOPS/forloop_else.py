# basic example
for i in range(5):
    print(i)
else:
    print("Loop Finished")

# example with break
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop Finished") # not printed because loop was broken

# data eng. example
files=["sales.csv", "inventory.csv", "customers.csv"]
for file in files:
    print("processing:",file)
else:
    print("All files processed successfully")