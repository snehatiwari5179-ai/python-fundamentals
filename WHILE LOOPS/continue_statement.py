i=0
while i<5:
    i +=1
    if i==3: # skips the iteration when i is equal to 3
        continue  # continues to the next iteration of the loop
    print(i)  # prints 1, 2, 4, 5 (skips 3)

# data eng. example
record=0
while record <=5:
    if record == 3: # skips the iteration when record is equal to 3
        record += 1
        continue  
    print("Processing record:", record) 
    record += 1  