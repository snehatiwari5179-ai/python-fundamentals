# intersection()
web_users={101,102,103,104}
mobile_users={103,104,105,106}
common_users=web_users.intersection(mobile_users)
print(web_users)  # original never changes
print(common_users)  # prints items both have in common

# intersection_update()
web_users={101,102,103,104}
mobile_users={103,104,105,106}
web_users.intersection_update(mobile_users)
print(web_users)  # 101 & 102 erased from web_users bcoz mobile_users dosen't have

# original sets after intersection()
crm_customers={1001,1002,1003}
app_customers={1002,1003,1004}
common_customers=crm_customers.intersection(app_customers)
print("CRM:",crm_customers)
print("App:",app_customers)
print("Common:",common_customers)

