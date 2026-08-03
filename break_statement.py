# break statement
# example 1
i=1
while i<=10:
    print(i)
    if i==5: # stops at 5
        break  # breaks the loop when i is equal to 5
    i += 1

# data eng. example
record=1            # start checking records from 1
while record <=1000: # search until 1000
    if record == 250: # stops at record 250
        print("customer found")
        break  # breaks the loop when record is equal to 250
    record += 1

while True:  # keep asking for password until correct one is entered
    password = input("Enter password: ")

    if password == "python123":  # loop goes back to enter password if the password is incorrect
        print("Correct!")
        break