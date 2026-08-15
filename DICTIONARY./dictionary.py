# create a Dictionary
student={
    "name":"sneha",
    "age":"22",
    "course":"BCA"
    }
print(student)

# Dict. with diff. data types
employee={
    "id":101,
    "name": "rahul",
    "salary":"40000",
    "is_active": True
}
print(employee)

# duplicate keys
student={
    "name":"Sneha",
    "name":"Sweety"  
}
print(student) # second key overwrites the first as duplicate keys not allowed, so only "Sweety" printed 

# duplicate values
grades={
    "Amit":"A",
    "Priya":"B",
    "Rahul":"B"
}
print(grades)  # duplicate values are valid
