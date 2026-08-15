db_config=("localhost",5432,"postgres_db")
print(db_config)
# Changing an Item Value
temp_list= list(db_config) # changing tuple to list
temp_list[1] = 5433
db_config = tuple(temp_list)  # changing list back to tuple
print(db_config)

# Adding an Item using List Workaround
temp_list= list(db_config)
temp_list.append("SSL_enabled")  
db_config= tuple(temp_list)
print(db_config)

# Adding an Item using Tuple Concatenation
new_setting = ("v1.0",)
db_config += new_setting  # add tuple to tuple
print(db_config)

# Removing an Item
temp_list= list(db_config)
temp_list.remove("v1.0")
db_config = tuple(temp_list)
print(db_config)


# Deleting the Entire Tuple
sample_tuple= ("temp1","temp2")
del sample_tuple
print(sample_tuple)   #this will raise an error because the tuple no longer exists
