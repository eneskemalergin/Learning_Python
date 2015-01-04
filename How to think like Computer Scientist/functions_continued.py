# Functions Continued... #

# Functions are famous with returning values...
print abs(5)

# These two statements are returning same value: 5
# They are taking 1 parameter

print abs(-5)

'''
Some functions take more than one argument.
    For example the math module contains a function called pow
    which takes two arguments, the base and the exponent.
'''
import math
print(math.pow(2, 3))

print(math.pow(7, 4))

# Continue with built-in functions shall we?

# max returns the maximum value in the defined numbers...
print(max(7, 11))
print(max(4, 1, 17, 2, 12))
print(max(3 * 11, 5 ** 3, 512 - 9, 1024 ** 0))

# The following function returns the x times x, another words square of x
def square(x):
    y = x * x
    return y

toSquare = 10
result = square(toSquare)
print("The result of ", toSquare, " squared is ", result)

# def addEm adds the parameters
def addEm(x, y, z):
    return x + y + z
    print('the answer is', x + y + z)

# another implementatio of square
def badsquare(x):
    y = x ** power
    return y

power = 2
result = badsquare(10)
print(result)
