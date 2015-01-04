# Imports "os" from the standart library

# operating system...
import os

# it shows your current directory
os.getcwd()

# It changes the current directory to a directory which has our file that we want to examine
os.chdir("C:\\Users\\Pc-41\\Desktop\\Python Examples\\Head First Python\\Chapter 3")


file = open('sketch.txt') # This command opens the txt file now it is ready to be read
file.close() # this function closes it.

# Let's have fun with our file using Python
data = open('sketch.txt')
# name_of_variable.readline() reads the line and print
print(data.readline(), end = '')
# Same statement again reads the line after the first one, in this case is second line.
print(data.readline(), end = '')


# use the seek() method to return to the start of the file. and yes, you can use tell with Python's files, too
data.seek()

# Following code prints all the line in the file
for each_line in data:
    print(each_line, end = '')

data.close()
