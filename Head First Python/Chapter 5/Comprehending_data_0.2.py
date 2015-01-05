## Comprehending Data V0.2

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
sarah =data.strip().split(',')

# We have to use some kind of sorting but how?

# We have two types of sorting mechanism in Python: sort() and sorted()

x = [1,3,5,2,8,10,6]
x

# We have used sort()
x.sort()
x

y = [1,3,5,2,8,10,6]
# We have used sorted()
sorted_y = sorted(y)
y
sorted_y

# We have used sorted because it only shows the sorted version, we don't want to mess with data.
print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))

'''
['2-22', '2-34', '2.34', '2.45', '2:01', '2:01', '3.01', '3:10', '3:21']
['2-23', '2.11', '2.59', '2:11', '2:23', '3-10', '3-21', '3.21', '3:10']
['2.49', '2:22', '2:38', '3.01', '3.02', '3.02', '3:01', '3:02', '3:22']
['2-25', '2-55', '2.18', '2.58', '2:39', '2:54', '2:55', '2:55', '2:58']

Ok! It's more tidy but still some mistakes in it...

'''
#The minute and seconds separators are confusing Python’s sorting technology.

# Python sorts the string as well as numbers
# a dash comes before a period, which itself comes before a colon.
