# copy using copy()
student={
    "name":"Sweety",
    "age":22
}
student_copy=student.copy()
print(student_copy)

# copy using dict()
student_copy2=dict(student)
print(student_copy2)

# assignment (=) - not a Copy
student_same=student
student_same["age"]=23
print("original:",student)
print("assigned:",student_same) 

# real copy test
employee={
    "id":101,
    "name":"Rahul",
    "salary":50000
}
employee_copy=employee.copy()
employee_copy["salary"]=70000
print("Original:",employee)
print("Copy:",employee_copy)