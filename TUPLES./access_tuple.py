server_info= ("192.168.1.1",8080,"HTTPS","Active","Production")
# standard indexing
first_item = server_info[0]
print(first_item)

# Negative Indexing
last_item = server_info[-1]
second_last = server_info[-2]
print(last_item)
print(second_last)

# Range of Indexes (Slicing)
port_proto= server_info[1:3]
print(port_proto)

# Range shortcuts
from_beginning= server_info[:3]
to_end = server_info[2:]
print(from_beginning)
print(to_end)

# Negative Range Slicing
middle_range= server_info[-4:-1]
print(middle_range)

# Check if Item exists
if "Active" in server_info:
    print("Verification Success")