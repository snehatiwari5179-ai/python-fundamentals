# Basic Loop
employee_IDs={101,102,103,104}
for employee in employee_IDs:
  print(employee)

# print customer IDs
customer_IDs={1001,1002,1003,1004}
for customer in customer_IDs:
   print("customer ID:",customer)

# membership check inside loop
product_IDs={501,502,503,504}
for product in product_IDs:
   if product==503:
      print("product found:",product)

# Data Eng. Example
order_IDs={5001,5002,5003}
for order in order_IDs:
   print(f"Processing Order ID:{order}")

customer_IDs={101,102,103,-1,104}
for customer in customer_IDs:
   if customer>0:
      print("valid customer:",customer)
   else:
      print("Invalid Customer:",customer)