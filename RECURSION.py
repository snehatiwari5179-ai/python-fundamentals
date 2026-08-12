# Recursion is when a function calls itself.
# BASIC 
def count(n): # func. named count
    if n==0: # check whether n has reached 0
        return # stop func.
    print(n)  # print current no.
    count(n-1) # call same func. but with 1 less
count(3) # start process with 3.


# fibonacci
def fibonacci(n):
    if n<=1:  # checks if n is 1 or smaller
        return n    # if yes, give n back and stop
    return fibonacci(n-1)+fibonacci(n-2)  # fibonacci(4) = 3, fibonacci(3) = 2, so 3+2 
print(fibonacci(5))

# recursion with LIST
def sum_list(num):
    if len(num)==0:    # checks whether the list has 0 items
        return 0       # if empty, stop and give back 0
    return num[0]+sum_list(num[1:])   # first item + function on the remaining items
print(sum_list([1,2,3,4]))

# recursion LIMIT
import sys
print(sys.getrecursionlimit)