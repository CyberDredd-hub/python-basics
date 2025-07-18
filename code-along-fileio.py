import os
'''file_path = "data.csv"

print(file_path)

f = open("data.csv")
f.close()

file = open(file_path, "r")#open in read mmode
file = open(file_path, "w")#open in write mode
file = open(file_path, "a")#open in append mode
file = open(file_path, "r+")#open in read/write mode'''

# write function will create a new file or overwite an existing one
file = open("example.txt", "w")
file.write("hello, world!\n")
file.write("This is line two!\n")
file.close()

#open a file with the with keyword
with open ("example-with.txt", "w") as file:
    file.write("we wrote this file using the 'with' keyword!\n")
    file.write("This is line two!")
    file.write("This is line 3!")

#read function to read contents of a file
with open("example-with.txt", "r") as file:
    contents = file.read()
    print(contents)

#use for loop to read lines from a file
with open("example-with.txt", "r") as file:
    for line in file:
        print(line.strip())

#append to a file using with
with open("example-with.txt", "a") as file:
    file.write("This is an appended line!\n")


#delete a file
if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("file deleted")
else:
    print("the file does not exist")

