# Joining Two Tuples
local_servers= ("Server-Asia-1", "Server-Asia-2")
global_servers= ("Server-US-1","Server-EU-1")

# Combine both tuples using the '+' operator
all_servers= local_servers + global_servers

print("1. Joined Tuple:",all_servers)

# Multiplying a Tuple
default_status= ("ACTIVE",)

# repeat the status 3 times using the '*' operator
status_list_tuple= default_status * 3
print("2. Multiplied Tuple:",status_list_tuple)
