# Access SET Items using for Loop
employee_IDs={101,102,103,104}
for employee in employee_IDs:
    print(employee)

# Membership checking using in
customer_IDs={1001,1002,1003,1004}
print(1003 in customer_IDs)
print(1010 in customer_IDs)  # checks if given value present or not

# membership checking using not in
product_IDs={501,502,503}
print(504 not in product_IDs)
print(501 not in product_IDs)

# Data Eng. Example
existing_customer_IDs={101,102,103,104,105,106}
new_customer=105
if new_customer in existing_customer_IDs:
    print("Customer already exists.")
else:
    print("New customer.Add to database.")
    