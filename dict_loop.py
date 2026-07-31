# loop through keys
student={
    "name":"Sweety",
    "age":22,
    "course":"BCA"
}
for key in student: # returns all keys only
    print(key) 

# loop using keys()
for key in student.keys():
    print(key)

# loop through values
for value in student.values():  # returns all values only
    print(value)

# loop through keys & values
for key,value in student.items():  # returns both K & V.
    print(key,":",value)