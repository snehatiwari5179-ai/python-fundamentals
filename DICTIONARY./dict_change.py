# change a value using []
student={
    "name":"Sneha",
    "age":21,
    "course":"BCA"
}
student["age"]=22
print(student)

# change a value using update()
student.update({"course":"MCA"})
print(student)

# add a new key using update()
student.update({"city":"kolkata"})
print(student)

# update multiple keys
student.update({
    "age":24,
    "course":"Data Eng.",
    "college": "Distance BCA"
})
print(student)
