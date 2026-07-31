# pop()
student={
    "name":"Sneha",
    "age":22,
    "course":"BCA"
}
removed=student.pop("age")
print("Removed:",removed)
print(student)

# popitem()
student={
    "name":"Sneha",
    "age":22,
    "course":"BCA"
}
student.popitem()
print(student)

# del (Delete One Key)
student={
    "name":"Sneha",
    "age":22,
    "course":"BCA"
}
del student["course"]
print(student)

# clear()
student={
    "name":"Sneha",
    "age":22
}
student.clear()
print(student)