#A list of database engine names used in data systems
db_engines=["PostgreSQL", "MySQL", "MongoDB","Redis","Cassandra","Snowflake"]
print("First database in list [0]:", db_engines[0])
print("Last database in list [-1]:", db_engines[-1])
print("Second-to-last database[-2]:",db_engines[-2])
print("------------------------------------------------------------------------")
#Range Slicing(positive ranges)
sub_list = db_engines[1:4]
print("slice of [1:4]:", sub_list)
print("------------------------------------------------------------------------")
#Slicing Shortcuts (Omitted Bounds)
print("Slice from start to [:3]:", db_engines[:3])
print("Slice from index 3 to end [3:]:",db_engines[3:])
print("------------------------------------------------------------------------")
#Negative Range Slicing
print("Negative slice [-4:-1]:", db_engines[-4:-1])
print("------------------------------------------------------------------------")
#Membership Verification
if "Snowflake" in db_engines:
    print("Successful")
else:
    print("Unsuccessful")
print("------------------------------------------------------------------------")