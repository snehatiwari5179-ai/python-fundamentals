# Server regions tuple
regions = ("Asia-South","US-East","EU-Central")
# Direct For Loop
print("1.Direct For Loop")
for region in regions:
    print(region)

# Loop by Index Nos.
print("2.For Loop with range() and len()")
for i in range(len(regions)):
    print(f"Index {i} contains:{regions[i]}")

# While Loop
print("3.While Loop")
index = 0
while index < len(regions):
    print(f"Position{index}:{regions[index]}")
    index +=1                                       # Move to the next index
