## Comprehending Data V0.1

''' Assuming that we have same type of different data of individuals:
    How would we comprehend them?

    Let's try to understand the concept with solving an example;

    
    We have 4 athlete, the coach needs a quick way to know the top three fastest times for each
    athlete

    Also we have 4 .txt file called
    - james.txt
    - julie.txt
    - mikey.txt
    - sarah.txt
    
    
'''

# Opening each files.
# Reading the line of data
# Convert the data to a list

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

# Displaying the list results
print(james)
print(julie)
print(mikey)
print(sarah)

'''
    data.strip().split(',') is a valid expression
    the methods are chained together

'''
# Let's see the result:

'''
    ['2-34', '3:21', '2.34', '2.45', '3.01', '2:01', '2:01', '3:10', '2-22']
    ['2.59', '2.11', '2:11', '2:23', '3-10', '2-23', '3:10', '3.21', '3-21']
    ['2:22', '3.01', '3:01', '3.02', '3:02', '3.02', '3:22', '2.49', '2:38']
    ['2:58', '2.58', '2:39', '2-25', '2-55', '2:54', '2.18', '2:55', '2:55']
We got this as a result
'''

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


# In another .py file we wrote our sanitize function and let's try again










