# add one item using add()
employee_IDs={101,102,103}
employee_IDs.add(104)
print(employee_IDs)

# duplicate value using add()
employee_IDs={101,102,103}
employee_IDs.add(102)
print(employee_IDs)  # duplicate ignored

# add multiple items using update()
employee_IDs={101,102,103}
new_employee_IDs={104,105,106}
employee_IDs.update(new_employee_IDs)
print(employee_IDs)

# update() with a List
customer_IDs={1001,1002}
new_customers=[1003,1004,1002]
customer_IDs.update(new_customers)
print(customer_IDs)

# update() with a Tuple
product_IDs={501,502}
new_products={503,504,502}
product_IDs.update(new_products)
print(product_IDs)


