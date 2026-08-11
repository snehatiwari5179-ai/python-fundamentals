# Lambda basic
#  a small anonymous function written in one line.

add=lambda a,b: a+b
print(add(20,30))

# Lambda + sorted()
employees=[
    ("ranveer",30000),
    ("raghbir", 25000),
    ("maahir",40000)
]
result=sorted(employees,key=lambda x: x[1])
print(result)

# lambda + filter()
numbers=[10,15,20,25,30]
result=filter(lambda x: x%2==0,numbers)
print(list(result)) # Because filter() and map() return a filter/map object, not a normal list, to get actual values as a list we have to write like this.

# Lambda + map()
numbers=[10,20,30]
result=map(lambda x:x*2,numbers )
print(list(result))
# example 2
num=[300,400,500]
result=map(lambda x:x+10,num)
print(list(result))
# example 3
names=["sw","rk"]
result=map(lambda x:x.upper(),names)
print(list(result))