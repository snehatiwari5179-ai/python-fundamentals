message="""hello sneha, 
welcome to python programming,
learn python and become a pythonista."""
print(message)
print("-------------------------")

word="python"
print(word[0]) #prints the first letter of the word
print(word[1]) #prints the second letter of the word
print(word[2]) #prints the third letter of the word
print("-------------------------")

for letter in "aeroplane":
    print(letter) #prints each letter of the word in a new line
print("-------------------------")

text="hello world"
print(len(text)) #prints the length of the string , space is also counted as a character.
print("-------------------------")

text="life is beautiful"
print("beautiful" in text) #prints True if the word is present in the string else prints False
text="life is beautiful"
print("amazing" in text)

print("-------------------------")

text="she is beautiful"
print("ugly" not in text) #prints True if the word is not present in the string else prints False

print("-------------------------")

text="Sneha is a Data-Engineer"
if "doctor" in text:
    print("Yes, 'doctor' is present in the string.")
else:
    print("No, 'doctor' is not present in the string.") 

    print("-------------------------")

text="Doreamon"
print(text[2:5]) #prints the letters from index 2 to 4  
text="Nobita"
print(text[:5]) #prints the letters from index 0 to 4 
text="Shizuka"
print(text[2:]) #prints the letters from index 2 to the end of the string
text="Gian"
print(text[-3:-1]) #n=-1,a=-2,i=-3,g=-4

print("-------------------------")

txt="hello data engineer"
text=txt.upper()
print(text) #prints the string in uppercase letters

print("-------------------------")

text="HELLO DATA ENGINEER"
text=text.lower()
print(text) #prints the string in lowercase letters

print("-------------------------")

txt="  Python Coding  "
text=txt.strip()
print(text) #prints the string without any leading and trailing spaces

print("-------------------------")

txt="I Love Web Development"
print(txt.replace("Web Development", "Data Engineering"))

print("-------------------------")

txt="Raj,Sharma"
print(txt.split(",")) #splits the string into a list where each word is a list item 

print("-------------------------")

first_name="Sneha"
last_name="Tiwari"
full_name= first_name + last_name
print(full_name) #prints the full name by concatenating first name and last name
first_name="Sneha"
last_name="Tiwari"
full_name= first_name + " " + last_name
print(full_name) #prints the full name by concatenating first name and last name with a space in between
age=22
txt="My age is " + str(age)
print(txt) #prints the age by converting the integer into a string

print("-------------------------")

name="kriti sanon"
age=30
message=f"My name is {name} and I am {age} years old."
print(message) #prints the message by using f-string formatting

print("-------------------------")

price=500
tax=50
receipt= f"Your total bill is Rs. {price+tax}"
print(receipt) #prints the total bill by calculating the sum of price and tax using f-string formatting

print("-------------------------")

number=3.14159
f_number=f"{number:.3f}"
print(f_number) #prints the number rounded to 3 decimal places using f-string formatting

print("-------------------------")

parts="keyboard\nmouse\nmonitor"
print(parts) #prints the string with each part on a new line using the newline character \n
feedback= " The client mentioned,\"the product is excelent\"during the review."
print(feedback) #prints the string with double quotes using the escape character \"
cityinfo="it\'s one of the most oldest operating ports in Salt Lake."
print(cityinfo) #prints the string with single quotes using the escape character \'"
file_path="C:\\Users\\Sneha\\Documents\\Python\\Projects"
print(file_path) #prints the string with backslashes using the escape character \\

print("-------------------------")

phone="123-456-7890"
is_indian=phone.startswith("91") #checks if the string starts with "91"
print(is_indian) #prints False since the string does not start with "91"
file_name="data.txt"
is_data=file_name.endswith(".txt") #checks if the string ends with ".txt"
print(is_data) #prints True since the string ends with ".txt"
age="22"
is_adult=age.isdigit() #checks if the string contains only digits
print(is_adult) #prints True since the string contains only digits
log_msg="database connection failed" 
position=log_msg.find("connection") #finds the position of the substring "connection" in the string
print(position) #prints 9 since the substring "connection" starts at index 9
txt="Hello my Name is SNEHA"
x=txt.casefold()
print(x) #prints the string in lowercase letters using the casefold() method