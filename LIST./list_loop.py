# A simple list of team members in our department
employees = ["Amit","Aman","Ajay"]
# Loop by Item
for name in employees: print("Employee Name:",name)     # "name" is a temporary placeholder variable created by Loop
# Loop by Index Position
for i in range(len(employees)):
    print(f"Position {i} is occupied by : {employees[i]}")
# Using a While Loop
counter=0    # the loop runs while counter is less than 3
while counter < len(employees):
    print(f"Reading index {counter}:{employees[counter]}")
    counter += 1    # moves the counter forward to avoid an infinite loop
# List Comprehension Shortcut
[print("Shorthand ouput:",name)for name in employees]
