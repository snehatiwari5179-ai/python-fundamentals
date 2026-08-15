# access using []
student={
    "name":"Sneha",
    "age":22,
    "course":"BCA"
}
print(student["name"])

# access using get()
print(student.get("age"))

# missing key with get()
print(student.get("city"))  # returns NONE as key dosen't exists

# print ALL Keys
print(student.keys())  # returns all keys

# print ALL Values
print(student.values())  # returns all values

# print ALL Items
print(student.items())  # returns key-value pairs.