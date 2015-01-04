''' Conditional Continued '''
# Nested Conditionals#

'''One conditional can also be nested within another. 

if x < y:
    print("x is less than y")
else:
    if x > y:
        print("x is greater than y")
    else:
        print("x and y must be equal")

'''
x = 10
y = 10

if x < y:
    print("x is less than y")
else:
    if x > y:
        print("x is greater than y")
    else:
        print("x and y must be equal")


x = -10
if x < 0:
    print("The negative number ",  x, " is not valid here.")
else:
    if x > 0:
        print(x, " is a positive number")
    else:
        print(x," is 0")


# Chained Conditionals #

'''
Python also provide more than one condition for one fact.
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x and y must be equal")

elif is an abbreviation of else if
there is no limit of the number of elif statements
'''
x = 10
y = 10

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x and y must be equal")
    
