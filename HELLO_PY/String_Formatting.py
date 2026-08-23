# BASIC f-string
name = "Ranveer Vaghela"        # VALUE: name
age = 27                        # VALUE: age
print(f"My name is {name} and I am {age}.")  # F-STRING: insert values

print("===============================")

#  EXPRESSION
price = 100     # VALUE: price
quantity = 3    # VALUE: quantity
print(f"Total:{price * quantity}")    # EXPRESSION: 

print("===============================")

#  DECIMAL FORMATTING
price = 99.5678                          # FLOAT: price
print(f"price:{price:.2f}")              # FORMAT: 2 decimals

print("===============================")

# PERCENTAGE
score = 0.6666                          # DECIMAL: percentage value
print(f"score:{score:.2%}")             # FORMAT: percentage

print("===============================")

# THOUSANDS SEPARATOR
sales =  15000000                      # INTEGER: large number
print(f"Sales:{sales:,}")              # FORMAT: comma separator
print(f"Sales:{sales:_}")              # FORMAT: underscore separator

print("===============================")

# WIDTH
name = "Maahir"       
print(f"{name:10}")    # Width = reserved space for the value 

print("===============================")

# ALIGNMENT
name = "Shahid"
print(f"{name:<15}")       # ALIGN: left
print(f"{name:^18}")       # ALIGN: center
print(f"{name:>20}")       # ALIGN: right

print("===============================")

# FILL CHARACTER
name = "Amar"
print(f"{name:*<8}")     # * + left
print(f"{name:*>12}")    # * + right
print(f"{name:*^10}")    # * + center

print("===============================")

# SIGN
number = 25
print(f"{number:+}")        # show +
print(f"{number:}")       # normal display

print("===============================")

# NUMBER FORMATS
number = 25
print(f"{number:d}")     # integer/decimal format
print(f"{number:b}")     # FORMAT: binary
print(f"{number:o}")     # FORMAT: octal
print(f"{number:x}")     # FORMAT: hexadecimal

print("===============================")
