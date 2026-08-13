num=[10,20,30] # normal list
my_iterator=iter(num)  # creates iterator from list
print(next(my_iterator))  # gets first value - 10
print(next(my_iterator))  
print(next(my_iterator))

print("__________________________________________")

class MyNumbers:   # creates our own type called MyNumbers

    def __iter__(self):   # tells Python how this object should start iterating
        self.a = 1       # creates a stored value called a and starts it at 1
        return self      # gives the same object back as the iterator

    def __next__(self):    # tells Python what to give when we ask for the next value
        x = self.a        # takes the current value of a and stores it in x
        self.a += 1        # increases a by 1
        return x       # gives the current value back


myclass = MyNumbers()    # creates an object from MyNumbers

myiter = iter(myclass)   # starts the iterator; Python runs __iter__()

print(next(myiter))        # asks for next value → 1
print(next(myiter))         # asks for next value → 2
print(next(myiter))        # asks for next value → 3
print(next(myiter))          # asks for next value → 4
print(next(myiter))          # asks for next value → 5