# create a frozenset
country_codes= frozenset({"IN","US","UK","CA"})
print(country_codes)

# remove duplicate automatically
numbers=frozenset([1,2,3,4,4,5])
print(numbers)

# membership check
allowed_roles=({"admin","manager","employee"})
print("admin" in allowed_roles)
print("guest" in allowed_roles)

# loop through a frozenset
departments=frozenset({"HR","IT","Sales"})
for department in departments:
    print(department)

# union()
set_1=frozenset({1,2,3})
set_2=frozenset({3,4,5})
print(set_1.union(set_2))

#numbers = frozenset([10, 20, 30])
#print(numbers)

# Now try all these one by one and observe ERROR msg.
#numbers.add(40)
#numbers.remove(20)
#numbers.clear()
#numbers.update([50])  