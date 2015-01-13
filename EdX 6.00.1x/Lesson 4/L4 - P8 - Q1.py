## L4 - P8 - Q1

'''
 Write a Python function, fourthPower,
 that takes in one number and returns that value raised to the fourth power.

You should use the square procedure that you defined in Problem 3 of
these lecture exercises
'''

def square(x):
    return(x*x)

def fourthpower(x):
    return (square(square(x)))
