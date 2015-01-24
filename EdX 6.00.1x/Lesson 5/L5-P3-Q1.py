## L5 - P3 - Q1

''' The function recurPower(base, exp) from Problem 2 computed baseexp
by decomposing the problem into one recursive case and one base case:

Write a procedure recurPowerNew which recursively computes exponentials using this idea.
'''
def recurPowerNew(base, exp):
    if exp <= 0:
        return 1
    elif exp % 2 == 1:
        return base * recurPowerNew(base, exp - 1)
    else:
        return recurPowerNew(base*base, exp/2)
