# Handling Exceptions

''' Python interpreter displays a traceback followed by an error message, if there is something
    wrong with your code

   The traceback is Python’s way of telling you that something unexpected has
occurred during runtime. In the Python world, runtime errors are called
exceptions.


    Python let’s you catch exceptions as they occur, which
gives you with a chance to possibly recover from the error and, critically, not
crash.


    Rather than adding extra code and logic to guard against bad things
happening, Python’s exception handling mechanism lets the error occur,
spots that it has happened, and then gives you an opportunity to recover.


    try:
        # some code may be cause a runtime error
    except:
        # your error-recovery code

    This syntax allows you to survive from the unexpected crashes.
'''

# Let's go back and examine our sketch file's data problem
# We were trying to print all the lines with for loop but we had 2 different errors
# and they have caused all program, after the typo, crashed.

data = open('sketch.txt')
for each_line in data:
    try:
        (role, line_spoken) = each_line.split(':', 1)
        print(role, end='')
        print(' said: ', end='')
        print(line_spoken, end='')
    except:
        pass
data.close()

# The result looks corrent but there is 2 lines missing actually. The try and except functionality
# ignored those which are causing the problem.

# Both approaches work at the same way, but which one is better?
# Extra Code |OR| Exception Handler

'''
Extra Code:
###########
By making sure runtime errors never happen, I keep
my code safe from tracebacks.
Complexity never hurt anyone.
I just don’t get it. You’re more than happy for your
code to explode in your face…then you decide it’s
probably a good idea to put out the fire?!?
But the bad things still happen to you. They never
happen with me, because I don’t let them.
Well…that depends. If you’re smart enough—and,
believe me, I am—you can think up all the possible
runtime problems and code around them.
Hard work never hurt anyone.
Of course all my code is needed! How else can you
code around all the runtime errors that are going to
happen?
Um, uh…most of them, I guess.
Look: just cut it out. OK?

Exception Handler:
##################
At the cost of added complexity….
I’ll be sure to remind you of that the next time
you’re debugging a complex piece of code at 4
o’clock in the morning.
Yes. I concentrate on getting my work done first and
foremost. If bad things happen, I’m ready for them.
Until something else happens that you weren’t
expecting. Then you’re toast.
Sounds like a whole heap of extra work to me.
You did hear me earlier about debugging at 4 AM,
right? Sometimes I think you actually enjoy writing
code that you don’t need…
Yeah…how many?
You don’t know, do you? You’ve no idea what will
happen when an unknown or unexpected runtime
error occurs, do you?
'''
'''
====================================================================
'''
# One way of checking if ther eis file or not!
import os
if os.path.exists('sketch.txt'):
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except ValueError: # Making our exceptions more specific
            pass
    data.close()
else:
    print('The data file is missin!')

# Another way
try:
    data = open('sketch.txt')

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except ValueError: # Making our exceptions more specific
            pass
    data.close()
except IOError: # Making our exceptions more specific
    print('The data file is missing!')
