#types of datatypes 

a="sweety"
print(type(a))
b=10
print(type(b))
c=10.5
print(type(c))
d= 2+3j
print(type(d))
x=["apple","banana","cherry","mango","grapes"]
print(type(x))
e=("apple","banana","cherry","mango")
print(type(e))
f=range(6)
print(type(f))
print(f)
#convert to list to display the content of x:
print(list(f))
my_dict={
    "name":["sneha tiwari","sweety"],
    "topic":"python",
    "status":"learning"
}
print(my_dict["name"])
print(type(my_dict))

#no fixed order, duplicates not allowed in set
my_set={"kolkata","bombay","kolkata","delhi","chennai","delhi"}
print(my_set)
print(type(my_set))

is_it_raining=True
is_it_sunny=False
print(type(is_it_raining))
print(is_it_raining)

k=None # captital N is used to define None
print(type(k))
print(k)

 #bytes datatype
msg="hello" #normal string
print(msg) 
packed=msg.encode('utf-8') #turned into bytes
print(packed)
unpacked=packed.decode('utf-8') #turned back into string
print(unpacked)

money=99.99
wihout_decimal=int(money) #converted to integer
print(wihout_decimal)
money=2000
with_decimal=float(money) #converted to float
print(with_decimal)
print("-------------------------")
import random #asks python to take out its random toolbox and use it
dice_roll=random.randint(1,6) #random number between 1 and 6
print(dice_roll)
print("-------------------------")
a=int(2.0)
b=int(3)
print(a+b)
print("----------------------")
c=float(2)
d=float(3.3)
print(c+d)
print("----------------------")
e=str(2)
f=str(3.3)
print(e+f) # concatenation of strings