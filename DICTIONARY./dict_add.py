# add one item using []
student={"name":"Sneha"}
student["age"]=22
print(student)

# add one item using update()
student.update({"course":"BCA"})
print(student)

# add multiple items 
student.update({
    "city":"Kolkata",
    "year":2,
    "college":"distance"
})
print(student)

# adding to an empty dict.
employee={}
employee["emp_id"]=1001
employee["name"]="Rahul"
print(employee)