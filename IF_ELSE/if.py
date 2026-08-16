# basic IF statement
age=20
if age>=18:
    print("eligible to vote")

# false condition
age=15
if age>=18:
    print("eligible to vote")

# marks example
marks=85
if marks>=40:
    print("Pass")

# salary example
salary=60000
if salary>50000:
    print("bonus eligible")

# data eng. example
employee={
    "name":"Prince",
    "salary":75000
}
if employee["salary"]>70000:
    print("High Salary Employee")