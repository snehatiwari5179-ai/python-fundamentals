# match statement
#example 1

day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")

# example 2
fruit="cherry"
match fruit:
    case "apple":
        print("This is an apple")
    case "banana":
        print("This is a banana")
    case _:  # works like else.
        print("Unknown fruit")

# example 3
file_type="csv"
match file_type:
    case "csv":
        print("Read CSV")
    case "json":
        print("Read JSON")
    case _:
        print("Unknown file type")