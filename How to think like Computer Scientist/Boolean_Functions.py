''' Boolean Functions '''

def isDivisible(x, y):
    if x % y == 0:
        result = True
    else:
        result = False

    return result

print(isDivisible(10, 5))

''' Basically it gives yes or no answer... '''

def isDivisible(x, y):
    if x % y == 0:
        result = True
    else:
        result = False

    return result

if isDivisible(10, 5):
    print("That works")
else:
    print("Those values are no good")
