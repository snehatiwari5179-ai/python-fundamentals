# difference()
registered_users={100,200,300,400,500}
active_users={300,400}
inactive_users=registered_users.difference(active_users)
print(inactive_users)  # returns elements present in first set & not in second set

# difference_update()
registered_users={100,200,300,400,500,700}
active_users={100,200}
registered_users.difference_update(active_users)
print(registered_users)  # modified the original set

# difference is one-way
set_a={1,2,3,4}
set_b={3,4,5,6}
print(set_a.difference(set_b))  #  set_a dataset is kept
print(set_b.difference(set_a))  #  set_b dataset is kept

