i=1
while i <=3:
    print(i)
    i += 1
else:
    print("Loop Finished")  # prints "Loop Finished" after the loop ends normally

# example 2
i=1
while i<=5:
    if i ==3:
        break
    print(i)
    i += 1
else:
    print("Loop Finished") # does not print "Loop Finished" because break stopped the loop early.