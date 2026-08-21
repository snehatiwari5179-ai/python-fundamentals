import re   # import RegEx module

# re.search() 
text= " I love python and python is easy"
result= re.search("python",text)   # Find first Python
print(result)

print("========================================")

# re.findall()
result= re.findall("python",text)    # Find all Python
print(result)

print("========================================")

# re.split()
text="dairy milk/kitkat/kinderjoy"
result= re.split("/",text)   # Split at /
print(result)

print("========================================")

# re.sub()
text=" I Love Lotus "
result= re.sub("Lotus","Roses",text)    # Replace Lotus
print(result)

print("========================================")

# [] character SET
text="cat bat mat"
result= re.findall(r"[cbh]at",text)  # c OR b OR h
# r"..." → raw string
print(result)

print("========================================")

# ^ --- beginning
text="Excel is easy"
result= re.search(r"^Learning",text)
print(result)  # as text dosen't start with "Learning", output is None

print("========================================")

# $ --- end
text = "I love python"
result= re.search(r"python$",text)   # Must end with python
print(result) 

print("========================================")

# . --- any single character
text= " cat cut mat"
result= re.findall(r"c.t",text)  # c + any character + t
print(result)

print("========================================")

# | --- OR
text= "I like blue and white"
result= re.findall(r"blue|white",text) # blue or white
print(result)

print("========================================")

# \d --- digit
text="My age is 22"
result= re.findall(r"\d",text)    # Find individual digits
print(result)

print("========================================")

# \w --- word character
text= "Sneha_08"
result= re.findall(r"\w",text)
print(result)

print("========================================")

# \s --- whitespace
text= "Hello World"
result= re.findall(r"\s",text)           # Find spaces
print(result)

print("========================================")

# \D --- not digit
text="A205"
result= re.findall(r"\D",text)      # Find non-digits, A
print(result)

print("========================================")

# \W --- not word character
text= "ABC@2000"
result= re.findall(r"\W",text)      # Find non-word characters, @
# A word character includes letters, digits, and _ .
print(result)

print("========================================")

# \S --- not whitespace
text= "Hello World"
result= re.findall(r"\S",text)      # Find non-space characters
print(result)

print("========================================")

# + --- 1 OR MORE
text= "My phone is 98765432"
result= re.findall(r"\d+",text)     # Whole number
print(result)

print("========================================")

# * --- ZERO OR MORE
text= "coooool"
result= re.findall(r"o*",text)
print(result)     #  commas = Python list separators

print("========================================")

# ? --- ZERO OR ONE
text= "color colour"
result= re.findall(r"colou?r",text)      # u is optional, both versions are allowed
print(result)

print("========================================")

# {n} --- exactly n times
text= "year:2026"
result= re.findall(r"\d{3}",text)       # Exactly 3 digits
print(result)

print("========================================")

# {n,m} --- n TO m times
text= "numbers: 12 123 1234 12345"
result= re.findall(r"\d{2,4}",text)     # minimum = 2, maximum = 4
print(result)

print("========================================")

# character ranges
text= "hello ABC 123"
lowercase= re.findall(r"[a-z]",text)  # lowercase letters from text
uppercase= re.findall(r"[A-Z]",text)  # uppercase letters from text
digits= re.findall(r"[0-9]",text)     # digits from text

print(lowercase)
print(uppercase)
print(digits)

print("========================================")

# [^0-9] --- not digit
text= "ABC123"
result= re.findall(r"[^0-9]",text)      # Anything except digits
print(result)

print("========================================")

# match object + group()
text= "my ph no is 98765432"
result= re.search(r"\d+",text)       # Find first number
if result:          # Check if match exists
    print("matched:",result.group())      # Get matched text

print("========================================")

# practical --- find number
text= "the product costs 2500 rupees"
result= re.findall(r"\d+",text)     # Extract number
print(result)

print("========================================")

# practical --- find order id
text= "order id: ORD-2458"
result= re.findall(r"ORD-\d+",text)
print(result)

print("========================================")
