# creating a SET
employee_ids= {101,102,103,104}
print(employee_ids)

# Duplicate values are removed
customer_ids= {101,102,103,101,104}
print(customer_ids)

# Length of a SET
customer_ids={101,102,103,104,102,106,105,108}
print(len(customer_ids))

# check data type
customer_ids={101,102,103}
print(type(customer_ids))

# SET with diff data types
sample_data={101,"python",True,95.5}
print(sample_data)

# Empty SET
empty_set=set()
print(type(empty_set))
print(empty_set)

# data eng example
raw_customer_ids=[101,102,103,101,104,105,102,106,107]
unique_customer_ids=set(raw_customer_ids)
print("raw records:", len(raw_customer_ids))
print("unique customers:",len(unique_customer_ids))
print("unique ids:", unique_customer_ids)

