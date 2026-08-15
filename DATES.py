import datetime     # Imports Python's datetime module
# current data & time
x=datetime.datetime.now() # Gets the current date and time
print(x)  # x is just a variable name we chose
# date parts
print(x.year)           # Gets and prints the year
print(x.month)          # Gets and prints the month
print(x.day)            # Gets and prints the day
print(x.strftime("%A"))      # Gets and prints the full weekday name

print("_____________________________________")

# create a date
my_date=datetime.datetime(2004,6,16) # Creates the date 16 June 2004
print(my_date)

print("_____________________________________")

# create date + time
my_datetime=datetime.datetime(2000,5,8,6,50)
print(my_datetime)

print("_____________________________________")

# strftime formatting
print(my_date.strftime("%d-%m-%Y"))  # Formats date as 16-06-2004
print(my_datetime.strftime("%d,%B,%Y"))  # Formats date as 8,May,2000
print(my_date.strftime("%A,%d,%B,%Y"))  # Formats date with weekday.