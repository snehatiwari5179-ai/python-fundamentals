# Two separate lists of regional branch locations
north=["Delhi","Chandigarh"]
south=["Bengaluru","Chennai"]
# Using '+' operator
all_branches = north + south
print(all_branches)
# Using a For Loop with append()
list_a = ["Delhi","Chandigarh"]
list_b = ["Bengaluru","Chennai"]
for city in list_b:
    list_a.append(city)
print(list_a)
# Using the extend() Method
team_1=["Delhi","Chandigarh"]
team_2=["Bengaluru","Chennai"]
team_1.extend(team_2)
print(team_1)