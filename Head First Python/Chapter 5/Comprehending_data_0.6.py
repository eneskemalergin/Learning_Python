## Comprehending Data V0.6


# set(), creates an empty set that does not allow duplicates

distances = {10.6, 11, 8, 10.6, "two", 7}
distances_no_dupplicate = set(distances)

'''

To extract the data you need, replace
all of that list iteration code in your
current program with four calls to
sorted(set(...))[0:3].

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

with open('james.txt') as jaf:
    data = jaf.readline()
james = data.strip().split(',')
with open('julie.txt') as juf:
    data = juf.readline()
julie = data.strip().split(',')
with open('mikey.txt') as mif:
    data = mif.readline()
mikey = data.strip().split(',')
with open('sarah.txt') as saf:
    data = saf.readline()
sarah = data.strip().split(',')

print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])


'''
['2.01', '2.22', '2.34']
['2.11', '2.23', '2.59']
['2.22', '2.38', '2.49']
['2.18', '2.25', '2.39']

Better Result
'''
