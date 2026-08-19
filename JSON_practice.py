import json
# 1. JSON OBJECT → PYTHON DICTIONARY

# outer quotes belong to Python, while inside represents JSON string.

json_data='{"name": "sneha" ,"age": 22}' # JSON object written as text
data=json.loads(json_data) # Converts JSON text into Python data
print(data)  # Prints the Python dictionary
print(type(data))  # Shows that the type is dict

print ("======================================")

# 2. JSON ARRAY → PYTHON LIST
json_data='[10,20,30,40]' # JSON array written as text
data=json.loads(json_data)  # Converts JSON array into Python list
print(data)     # Prints the list
print(type(data))   # Shows that the type is list

print ("======================================")

# 3. JSON STRING → PYTHON STRING
json_data='"Sweety"'  # JSON string written as text
data=json.loads(json_data)  # Converts JSON string into Python string
print(data)
print(type(data))   # Shows that the type is str

print ("======================================")

# 4. JSON NUMBER → PYTHON NUMBER
json_data='25'  # JSON integer written as text
data=json.loads(json_data)  # Converts JSON number into Python integer
print(data)
print(type(data))    # Shows that the type is int

print ("======================================")

# 5. JSON TRUE → PYTHON TRUE
json_data='true'
data=json.loads(json_data)  # Converts JSON true into Python True
print(data) 
print(type(data))   # Shows that the type is bool 

print ("======================================")

# 6. JSON FALSE → PYTHON FALSE
json_data='false'    # JSON boolean
data=json.loads(json_data)  # Converts JSON false into Python False
print(data)
print(type(data))  # Shows that the type is bool

print ("======================================")

# 7. JSON NULL → PYTHON NONE
json_data='null'    # JSON null value
data=json.loads(json_data)  # Converts JSON null into Python None
print(data)
print(type(data))   # Shows that the type is NoneType

print ("======================================")

# 8. PYTHON DICTIONARY → JSON OBJECT
data={      # Creates Python dictionary
    "name":"sneha",
    "age":22
}
json_data=json.dumps(data)  # Converts Python dictionary into JSON
print(json_data)    # Prints JSON

print ("======================================")

# 15. REALISTIC JSON WITH MULTIPLE DATA TYPES
json_data = '''
{
    "name": "Sneha",
    "age": 22,
    "skills": ["Python", "SQL"],
    "student": true,
    "address": null
}
'''                                                # JSON containing different data types

data = json.loads(json_data)                      # Converts the complete JSON into Python

print(data)                                       # Prints the complete Python dictionary

print(data["name"])                               # Gets string value

print(data["age"])                                # Gets integer value

print(data["skills"])                             # Gets list value

print(data["student"])                            # Gets boolean value

print(data["address"])                            # Gets None value