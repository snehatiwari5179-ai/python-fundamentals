# remove()
employee_IDs={101,102,103,104}
employee_IDs.remove(103)
print(employee_IDs)

# discard()
customer_IDs={201,202,203}
customer_IDs.discard(201)
print(customer_IDs)
customer_IDs={201,202,203}
customer_IDs.discard(205)
print(customer_IDs)  # no error if item missing

# pop()
product_IDs={501,502,503,504}
removed_item=product_IDs.pop()  # you dont know which item that gets removed
print("random no. removed:",removed_item)
print(product_IDs)

# clear()
transaction_IDs={1001,1002,1003}
transaction_IDs.clear()   # empties the set
print(transaction_IDs)

# del
sensor_IDs={1,2,3}
del sensor_IDs
#print(sensor_IDs) gives error as it deletes the SET completely.