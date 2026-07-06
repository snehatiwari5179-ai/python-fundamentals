print(10>5) #prints True since 10 is greater than 5
print(50<2)
print("apple"=="banana") #prints False since apple is not equal to banana
print(bool("HELLO")) #prints True since non-empty strings are considered True
print(bool("")) #prints False since empty strings are considered False
print(bool(0)) #prints False since 0 is considered False
print(bool(15)) #prints True since non-zero numbers are considered True
x="Sneha"
y=20
print(bool(y))
print(bool(["apple","banana", "cherry"])) #prints True since non-empty lists are considered True

print ("_______________________________________")

def myFUNCTION():
    return True
print(myFUNCTION()) #prints True since the function returns True

print ("_______________________________________")

def myFUNCTION():
    return True
if myFUNCTION():
    print("YES!") #prints YES! since the function returns True
else:
    print("NO!") #this line will not be executed since the function returns True

print ("_______________________________________")

x=200 
print(isinstance(x, str)) #prints False since x is an integer, not a string

print ("_______________________________________")

text="elephant"
print(len(text)) #prints the length of the string, which is 8
print(bool(text)) #prints True since non-empty strings are considered True
