import os

# READ

with open("data.txt","r") as file:      # with → manages file automatically
     content = file.read()         # read file
     print(content)

print("------------------------")

# CREATE + WRITE

with open("data.txt","w") as file:      # w → overwrite
     file.write("Sneha\n")     # write() → write data, \n → new line
     file.write("Laadoo\n")

print("------------------------")

#  APPEND

with open("data.txt","a") as file:      # a → append
     file.write("Puchu")                # adds data at the end

print("------------------------")

# READ LINE BY LINE

with open("data.txt","r") as file:      # r → read
     for line in file:              # loop → each line
          print(line.strip())           # strip() → remove \n/ whitespace

print("------------------------")

# CHECK IF FILE EXISTS

if os.path.exists("data.txt"):
     print("File Exists")

print("------------------------")

# DELETE FILE

# os.remove(data.txt)         # remove() → delete file
