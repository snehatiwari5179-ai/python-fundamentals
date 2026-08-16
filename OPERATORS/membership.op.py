# 1. Substring matching & case-sensitivity boundaries
log_entry = "Critical_Error: Data pipeline lookup failed on node_04."
print("---phase 1: string parsing stream---") # parsing =action of scanning & breaking down sent. to find ur word.
print("Is 'Data' present:", "Data" in log_entry)
print("Is lowercase 'data' present?:", "data" in log_entry)

# 2. Sequence Lookups (Lists)
authorized_roles = ["admin", "developer", "guest"]
current_user = "developer"

print("\n---2. Sequence List Verification---")
# Using 'in' to route authorization workflows
if current_user in authorized_roles:
    print(f"Access granted for user role: {current_user}")
else:
    print("Access Denied.")

# Using 'not in' to verify absences
print("Is 'manager' absent from roles?:", "manager" not in authorized_roles)

# 3. Mapping retrievals (dictionaries)
server_config = {
    "port": 8080,
    "enviroment": "production",
    "ssl_enabled": True
}
print("\n--- 3. Dict. boundary scanning---")
# Default membership scanning targets KEYS only
print("Is 'enviroment' a configuration key?:", "enviroment" in server_config) 
print("Is 'production' a configuration key?:", "production" in server_config) 

# Explicitly targeting the mapped values pool using the .values() method
print("Is 'production' present in values pool?:", "production" in server_config.values())