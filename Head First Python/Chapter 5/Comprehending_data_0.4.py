## Comprehending Data V0.4

# We got what we want but it is not enough

''' As things stand, your code creates four lists to hold the data as read
from the data files. Then your code creates another four lists to hold
the sanitized data. And, of course, you’re iterating all over the
place...

'''

# We will use list comprehension to make it les painful

# write when transforming one list into another.

'''
To do for comprehending lists
1 Create a new list to hold the transformed data.
2 Iterate each data item in the original list.
3 With each iteration, perform the transformation.
4 Append the transformed data to the new list.


clean_mikey = []
for each_t in mikey:
    clean_mikey.append(sanitize(each_t))

or

clean_mikey = [sanitize(each_t) for each_t in mikey]

# The both does the same think
'''

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

with open('james.txt') as jaf: data = jaf.readline()
james = data.strip().split(',')
with open('julie.txt') as juf: data = juf.readline()
julie = data.strip().split(',')
with open('mikey.txt') as mif: data = mif.readline()
mikey = data.strip().split(',')
with open('sarah.txt') as saf: data = saf.readline()
sarah = data.strip().split(',')

print(sorted([sanitize(t) for t in james]))
print(sorted([sanitize(t) for t in julie]))
print(sorted([sanitize(t) for t in mikey]))
print(sorted([sanitize(t) for t in sarah]))

# This prints the same result but we avoided to spend both unnecessary memory and time

