# symmetric_difference()
website_users={20,30,40,50}
mobile_users={30,40,70,80}
unique_users=website_users.symmetric_difference(mobile_users)
print(unique_users)  # removes common elements

# symmetric_difference_update()
website_users={20,30,40,50,60}
mobile_users={30,40,70,80}
website_users.symmetric_difference_update(mobile_users)
print(website_users)  # modified the original set

# original sets after symmetric_difference()
branch_a={200,300,400,500}
branch_b={500,600,700,800}
diff_customers=branch_a.symmetric_difference(branch_b)
print("branch A:",branch_a)
print("branch B:",branch_b)
print("Diff Customers:",diff_customers)   # except 500 (common) every elements printed from both groups.