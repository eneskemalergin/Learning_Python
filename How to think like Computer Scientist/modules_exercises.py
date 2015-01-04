# Exercises #

# 1. Use a for statement to print 10 random numbers.
import random 
for i in range(10):
    i = random.random()
    print i

# 2. Repeat the above exercise but this time print 10 random numbers between 25 and 35.
import random
for i in range(10):
    i = random.randrange(25,36)
    print i

# 3. The Pythagorean Theorem tells us that the length of the hypotenuse
#       of a right triangle is related to the lengths of the other two sides.
#       Look through the math module and see if you can find a function that
#       will compute this relationship for you. Once you find it, write a short
#       program to try it out.
import math
result = math.hypot(3,4)
print result

'''
import math

side1 = 3
side2 = 4
hypotenuse = math.hypot(side1,side2)
print(hypotenuse)
'''
