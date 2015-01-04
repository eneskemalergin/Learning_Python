''' Conditional Execution '''
# Binary Selection #

x = 15

if x % 2 == 0:
    print(x, "is even")
else:
    print(x, "is odd")

#----------------------------------------------------------------#
'''
Syntax of an if statement :

if BOOLEAN EXPRESSION:
    STATEMENTS_1        # executed if condition evaluates to True
else:
    STATEMENTS_2        # executed if condition evaluates to False

'''

if 4 + 5 == 10:
    print"TRUE"
else:
    print"FALSE"

print"TRUE"

if 4 + 5 == 10:
    print("TRUE")
else:
    print("FALSE")

#----------------------------------------------------------------#
''' We can ommit else clause entirely '''

x = 10
if x < 0:
    print("The negative number ",  x, " is not valid here.")
print("This is always printed")



x = -10
if x < 0:
    print("The negative number ",  x, " is not valid here.")
print("This is always printed")

# This will throw an error because we have used else two times.
'''

x = -10
if x < 0:
    print("The negative number ",  x, " is not valid here.")
else:
    print(x, " is a positive number")
else:
    print("This is always printed")

'''
