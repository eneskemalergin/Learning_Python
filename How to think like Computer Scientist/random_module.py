# -*- coding: cp1252 -*-
# The Random Module #

import random

prob = random.random()
print prob
'''
    The random() function returns a floating point
number in the range [0.0, 1.0)
'''

diceThrow = random.randrange(1,7)
print(diceThrow)
'''
    The randrange function generates an integer between its
lower and upper argument, using the same semantics as range
— so the lower bound is included, but the upper bound is excluded.
All the values have an equal probability of occurring

'''
'''
    It is important to note that random number generators are based on a deterministic algorithm
— repeatable and predictable.
So they’re called pseudo-random generators — they are not genuinely random. 
'''
