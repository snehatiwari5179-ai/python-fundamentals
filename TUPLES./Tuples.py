# Creating a standard tuple
db_config=("localhost",5432,"postres_db","localhost")
print(db_config)    # Tuples allow duplicates
print("Total Items:",len(db_config))
print("Data Type:", type(db_config))

# Demonstrating Mixed Types
mixed_tuple=("user1",101,True,99.5)   
print(mixed_tuple)

# The Single-Item Tuple Trap
# CORRECT : with a trailing comma
real_tuple=("admin",)
print(real_tuple)

# Creating a Tuple with tuple() Constructor
# Note the double round-brackets
constructed_tuple = tuple(("Production","Staging","Development"))
print(constructed_tuple)