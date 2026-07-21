# A List of daily business transaction amounts in dollars
transactions=[12,55,20,80,45]
# The traditional Loop Way
high_values=[]
for amount in transactions:
    if amount>30:
        high_values.append(amount)
print(high_values)
# The List Comprehension Way
high_values_shortcut=[amount for amount in transactions if amount > 30]
print(high_values)