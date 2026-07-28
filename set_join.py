# join sets using union()
branch_a={101,102,103}
branch_b={103,104,105}
all_customers=branch_a.union(branch_b)
print("branch A:",branch_a)
print("branch B:",branch_b)
print("All Customers:",all_customers)

# join sets using update()
branch_a={101,102,103}
branch_b={103,104,105}
branch_a.update(branch_b)
print(branch_a)

# original set after union()
employee_team_1={201,202}
employee_team_2={202,203}
merged_team=employee_team_1.union(employee_team_2)
print(employee_team_1)
print(employee_team_2)
print(merged_team)

# original set after update()
employee_team_1={201,202}
employee_team_2={202,203}
employee_team_1.update(employee_team_2)
print(employee_team_1)



