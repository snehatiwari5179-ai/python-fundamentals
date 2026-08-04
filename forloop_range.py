# range (stop)
for i in range(5):
    print(i)  # prints numbers from 0 to 4 as stop value 5 is not included

# repeat a task
for i in range(3):
    print("Hello")  # prints Hello 3 times

# data eng. example
for record in range(10):
    print(f"Processing record {record}")  # simulating processing of 10 records

print("__________________________________________________")

# range (start, stop)
for record in range(101, 106):
    print("processing record:", record)  # prints numbers from 101 to 105
print("____________________________________________________")
# range (start, stop, step)
for record in range(1,101,10):
    print("processing record:", record)  # prints numbers from 1 to 100 with a step of 10
