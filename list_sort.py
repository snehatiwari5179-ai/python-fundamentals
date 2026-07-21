# Default Ascending sort
prices=[40,10,50,20]
prices.sort()
print(prices)
# Descending Reverse Sort
prices.sort(reverse=True)
print(prices)
# Custom Function Sorting
# Sort no. based on how close they r to the no. 25
def check_closeness(number):
    return abs(number - 25)
scores=[100,22,50,28]
scores.sort(key = check_closeness)
print(scores)
# Case Insensitive Sorting
fruits = ["cherry","banana","apple"]
fruits.sort(key = str.lower)
print(fruits)
# Pure Reversing ( The reverse() method )
items=["First","Second","Third"]
items.reverse()
print(items)
