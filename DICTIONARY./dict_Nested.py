# create Nested Dict.
students={
    "student1":{
        "name":"Sneha",
        "age":21
    },
    "student2":{
        "name":"Raj",
        "age":26
    }
}
print(students)

# Access Nested Values
print(students["student1"]["name"])
print(students["student2"]["age"])

# Modify Nested Values
students["student1"]["age"]=22
print(students)

# Add New Item
students["student1"]["city"]="Kolkata"
print(students)

# Data Eng Example
employee={
    "emp_id":101,
    "personal_info":{
        "name":"Sneha",
        "age":22
    },
    "job_info":{
        "dapartment":"Data Engineering",
        "salary":75000
    }
}
print(employee["personal_info"]["name"])
print(employee["job_info"]["salary"])