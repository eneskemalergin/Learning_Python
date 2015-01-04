# Programs Produce Data
#======================

man = []
other = []
try:
    data = open('sketch.txt')
    for i in data:
        try:
            (role, line_spoken) = i.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!')

print(man)
print(other)

# The code above unite the lines for man in man list, other man's lines in other list

# Another great feature is writing on data
# Syntax is:
# out = open("data.out","w")
# print("Norwegian Blues stun easily.", file=out) // How you write thing in the file

# Now we will create some txt files using Python fileI/O
'''
try:
    man_file = open('man_data.txt', 'w')
    other_file = open('other_data.txt', 'w')
    print(man, file = man_file)
    print(other, file = other_file)

    man_file.close()
    other_file.close()
except IOError:
    print('File Error')
'''
# after running this code we will have 2 more txt files created by Python. man_data, and other_data

''' It’s a different story when writing data to files: if you need to handle an
IOError before a file is closed, your written data might become corrupted
and there’s no way of telling until after it has happened.
'''

try:
    man_file = open('man_data.txt', 'w')
    other_file = open('other_data.txt', 'w')

    print(man, file=man_file)
    print(other, file=other_file)
except IOError:
    print('File error.')
finally: # we can omit this unwanted situation to be happened with finally suite.
    man_file.close()
    other_file.close()
# No matter what, the code in the finally suite always runs.
''' If no runtime errors occur, any code in the finally suite executes. Equally,
if an IOError occurs, the except suite executes and then the finally
suite runs.'''

# If you use with you don't have to close the files that you have opened.
try:
    with open(‘man_data.txt', ‘w') as man_file:
        print(man, file=man_file)
    with open(‘other_data.txt', ‘w') as other_file:
        print(other, file=other_file)
except IOError as err:
    print(‘File error: ' + str(err))
          
with open('man_data.txt', 'w') as man_file, open('other_data.txt’, 'w’) as other_file:
    print(man, file=man_file)
    print(other, file=other_file)


with open('man_data.txt') as mdf:
    print(mdf.readline())
