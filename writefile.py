import os
#from traceback import print_tb

# Open the file in write mode (this will create the file if it doesn't exist)
with open('test.txt', 'w') as file:
    # Write content to the file
    file.write("Hello, this is a quick test file.\n")
    file.write("This is the second line of the file.")

current_directory = os.getcwd()

print("Current Working Directory:", current_directory)

keyfile = open('test.txt')

print(keyfile)

print(keyfile.read())
print(keyfile.read())

print(keyfile.seek(0))

content = keyfile.read()

print(content)

keyfile.close()  # use the close function to make sure the file does not stay open after use

keyfile = open('test.txt')

print(keyfile.readlines())

keyfile.seek(0)

bylines = keyfile.readlines()

print(bylines)

for line in bylines:
    print(line.split()[0])

keyfile = open('test.txt', 'w+')

# print(keyfile.read()) this prints out an empty string because w+ deletes all the text in the file
keyfile.write('MY NEW TEXT')

print(keyfile.seek(0))

print(keyfile.read())

keyfile.close()

keyfile = open('oops.txt', 'a+')  #this makes files without writable permissions

keyfile.write('First line in A+ opening')

keyfile.close()

newfile = open('oops.txt')

print(newfile.read())
newfile.close()

keyfile = open('oops.txt', 'a+')
keyfile.write('Added second line because I used A+ mode')

keyfile.seek(0)

print(keyfile.read())

keyfile.write('\nThis is the real new line, on the next line')

keyfile.seek(0)

print(keyfile.read())

keyfile.seek(0)

print(keyfile.read())
keyfile.close()

with open('oops.txt', 'r') as filename:
    variable = filename.readlines()

print(variable)
