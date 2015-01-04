                ### Files ###
## Working with Data Files ##
''' In real life data reside in files, we have to learn how to manage files using python '''
''' In Python, we must open files before we can use them and close them when we are done with them. '''

''' Method Name 	Use 	                Explanation
    open 	        open(filename,'r') 	Open a file called filename and use it for reading. This will return a reference to a file object.
    open 	        open(filename,'w') 	Open a file called filename and use it for writing. This will also return a reference to a file object.
    close 	        filevariable.close() 	File use is complete.
'''
## Finding a File on your Disk ##

''' Opening a file requires that you, as a programmer,
    and Python agree about the location of the file on your disk.
    '''
#The way that files are located on disk is by their path

'''For example on a Mac if you save the file hello.txt in your home directory the path
    to that file is /Users/yourname/hello.txt On a Windows machine the path looks a bit
    different but the same principles are in use. For example on windows the path might be
    C:\Users\yourname\My Documents\hello.txt '''

''' You can access files in folders, also called directories,
    under your home directory by adding a slash and the name of the folder.
    For example, if you had a file called hello.py in a folder called CS150
    that was inside a folder called PyCharmProjects under your home directory,
    then the full name for hello.py stored in the CS150 folder would be
    /Users/yourname/PyCharmProjects/CS150/hello.py
'''

''' If your file and your Python program are in the same directory you can simply use the
    filename. open('myfile.txt', 'r') '''

''' If your file and your Python program are in different directories then you
    should use the path to the file open('/Users/joebob01/myfile.txt', 'r'). '''


## Reading a File ##
''' suppose we have a text file called qbdata.txt that contains a data with following format:
First Name, Last Name, Position, Team, Completions, Attempts, Yards, TDs, Ints, Comp%, Rating '''

fileref = open("qbdata.txt", "r")
fileref.close()





''' we can close it by using the close method. After the file is closed any
    further attempts to use fileref will result in an error.'''
## Iterating over lines in a File ##

''' We will now use this file as input in a program that will do some data processing.
    In the program, we will read each line of the file and print it with some additional text.
    Because text files are sequences of lines of text, we can use the for loop to iterate
    through each line of the file. '''

''' To process all of our quarterback data, we will use a for loop to iterate over the
    lines of the file. Using the split method,
    we can break each line into a list containing all the fields of interest about the quarterback.
'''

qbfile = open("qbdata.txt", "r")

for aline in qbfile:
    values = aline.split()
    print('QB ', values[0], values[1], 'had a rating of ', values[10] )

qbfile.close()

## Alternative File Reading Methods ##

'''
Method Name 	Use 	                Explanation
write 	        filevar.write(astring) 	Add astring to the end of the file. filevar must refer to a file that has been opened for writing.
read(n) 	filevar.read() 	        Reads and returns a string of n characters, or the entire file as a single string if n is not provided.
readline(n) 	filevar.readline() 	Returns the next line of the file with all text up to and including the newline character. If n is provided as a parameter than only n characters will be returned if the line is longer than n.
readlines(n) 	filevar.readlines() 	Returns a list of strings, each representing a single line of the file. If n is not provided then all lines of the file are returned. If n is provided then n characters are read but n is rounded up so that an entire line is returned.

'''
#Now let’s look at another method of reading our file using a while loop. 
infile = open("qbdata.txt", "r")
line = infile.readline()
while line:
    values = line.split()
    print('QB ', values[0], values[1], 'had a rating of ', values[10] )
    line = infile.readline()

infile.close()

## Writing Text Files ##
# 'w' flag instead of the 'r' flag

infile = open("qbdata.txt", "r")
aline = infile.readline()
while aline:
    items = aline.split()
    dataline = items[1] + ',' + items[0]
    print(dataline)
    aline = infile.readline()

infile.close()
'''  the next step is to add the necessary pieces to produce an
    output file and write the data lines to it.
    To start, we need to open a new output file by adding another call to the open function,
    outfile = open("qbnames.txt",'w')
    using the 'w' flag. 
'''
infile = open("qbdata.txt", "r")
outfile = open("qbnames.txt", "w")

aline = infile.readline()
while aline:
    items = aline.split()
    dataline = items[1] + ',' + items[0]
    outfile.write(dataline + '\n')
    aline = infile.readline()

infile.close()
outfile.close()


