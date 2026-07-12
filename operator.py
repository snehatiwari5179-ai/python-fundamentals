x=5
y=2
print(x+y) #add
a=3
b=3
print(a*b) #multiply
r=10
s=5
print(r/s) #divide
total_chocolate=10
children=3
reminder=total_chocolate%children
print(reminder) #modulus
base_no=6
power=2
print(base_no**power) #exponentiation
number1=8
number2=3
print(number1//number2) #floor division,cuts off the decimal part and returns the integer value.

print("________________________________________")

record_count=5
print("starting count:",record_count)
record_count +=10  #same as record_count=record_count+10
print("Batch 1 arrived. Total count:",record_count)
record_count -=3  #same as record_count=record_count-3
print("After removing corrupted rows. Total count:",record_count)
server_cost=100
print("Initial server cost:",server_cost)
server_cost *=2  #same as server_cost=server_cost*2
print("Cost after doubling:",server_cost)
server_cost /=4 #same as server_cost=server_cost/4
print("Final cost per department:",server_cost)
leftover_tokens=11
leftover_tokens %=3  # 3 goes into 11 three times with a remainder of 2
print("variable updated with remainder only:",leftover_tokens)
total_packages=5
total_packages //=3  #floor division operator discards the remainder and returns only the integer value.
print("Variable updated with whole number only:",total_packages)
x=4
x **=3
print("x after exponentiation:",x)

print("________________________________________")

#setting up data
marks=65
#python evaluates 'marks>=60' first and then assigns the result to 'result'
status="pass" if marks>=60 else "fail"
print("Student status:",status)
age=14
can_vote="yes" if age>=18 else "no"
print('can age 14 vote?',can_vote)

#testing 3 possible outcomes on a single line using nested ternary operator.
student_marks=85
grade="A" if student_marks >=90 else ("B" if student_marks >=50 else "F")
print("Student grade:",grade)

#test with a failing score
student_marks=35
grade="A" if student_marks >=90 else ("B" if student_marks >=50 else "F")
print("Student grade:",grade)

#using elif
score=45
if score >=80:
    grade_ladder="A"
elif score >=40:
    grade_ladder="B"
else:
    grade_ladder="F"
print("Ladder result:",grade_ladder)

#standard numrical comparison operators
a=15
b=25
print("is a equal to b?:", a == b)
print("is a not equal to b?:", a !=b)
print("is a less than b?:", a<b)
print("is b greater than or equal to 25?:", b>=25)

#float and integer comparison
print("does integer 10 equal float 10.0?:", 10==10.0)

#chaining comparison operators
age=30
is_working_age = 18 < age < 65
print("is age between 18 and 65?:",is_working_age)

# standard logical gate checks
is_authorized=True
has_valid_token= False
has_expired= False
#The 'and' check
print("Can logic (and):", is_authorized and has_valid_token)
#The 'or' check
print("Can logic (or):", is_authorized or has_valid_token)
#The 'not' check
print("Is active session:", not has_expired)

condition1=False
ghost_variable=True
#because condition1 is False, 'and' short-circuits and does not evaluate ghost_variable.
print("short-circuit and result:", condition1 and ghost_variable)

# Testing Mutable Objects 
list_1 = [1,2,3]
list_2 = [1,2,3]
list_3 = list_1 #list_3 points to the same object as list_1
print("---Testing Lists---")
print("Do values match? (list_1 == list_2):", list_1 == list_2)
print("Are they the same memory box? (list_1 is list_2):", list_1 is list_2)
print("Are list_1 and  list_3  identical? (list_1 is list_3):", list_1 is list_3)

#Checking their actual location address in RAM
print("Memory ID of list_1:", id(list_1))
print("Memory ID of list_2:", id(list_2))
print("Memory ID of list_3:", id(list_3))

#Testing the interview Trap: Integer caching
print("\n--- Testing Small Integer Caching (-5 to 256) ---")
x = 100
y = 100
print("Is 100 pointing to the same memory slot?:", x is y )