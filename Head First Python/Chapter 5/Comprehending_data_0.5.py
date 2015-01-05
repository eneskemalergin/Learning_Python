## Comprehending Data V0.5

# Now we have another problem duplicates
# Coach stated his demand "three fastest timesfor each athlete."

'''
our goal is -> producing the three fastest times for each athlete.
    And, of course, there’s no place for any duplicated times in your
output.

'''
# Let's work on that!

# For Accessing the first three data items from any list, we use list slicing

list_ = [1,2,3,4,5,6,6,7,8,8,9]

list_[0:3]# Will give the first 3 element

# But What about the duplicates
# We have to remove the duplicates, How?

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

# Removing duplicates and showing first 3 elements for James
# Empty List
unique_james = []

for each_t in james: # Iterate over the existing data
    if each_t not in unique_james: # if the data item isn't already in the new list
            unique_james.append(each_t) # append the unique data item to the new list

print(unique_james[0:3])

# Julie
unique_julie = []
for i in julie:
    if i not in unique_julie:
        unique_julie.append(i)

print(unique_julie[0:3])

# Mikey
unique_mikey = []
for i in mikey:
    if i not in unique_mikey:
        unique_mikey.append(i)

print(unique_mikey[0:3])

# Sarah
unique_sarah = []
for i in sarah:
    if i not in unique_sarah:
        unique_sarah.append(i)

print(unique_sarah[0:3])


'''

['2-34', '3:21', '2.34']
['2.59', '2.11', '2:11']
['2:22', '3.01', '3:01']
['2:58', '2.58', '2:39']

'''

# We have done it, but not so fast! This code is not looking good
