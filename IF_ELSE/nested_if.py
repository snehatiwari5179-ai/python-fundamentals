# basic nested if
age=22
has_degree=True
if age >=18:
    if has_degree:
        print("Eligible for interview")

# outer condition false
age=16
has_degree=True
if age >=18:
    if has_degree:
        print("Eligible") # no output since outer condition is false

# nested if with else
age=20
has_id=False
if age >=18:
    if has_id:
        print("Entry allowed")
    else:
        print("Entry denied, ID required")

# data eng. example
employee={
    "active": True,
    "salary": 70000
}
if employee["active"]:
    if employee["salary"]> 60000:
        print("Eligible for bonus")