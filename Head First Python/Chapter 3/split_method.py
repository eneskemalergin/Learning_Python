# We now our data now, let's examine our file:

'''
Man: Is this the right room for an argument?
Other Man: I've told you once.
Man: No you haven't!
Other Man: Yes I have.
Man: When?
Other Man: Just now.
Man: No you didn't!
Other Man: Yes I did!
Man: You didn't!
Other Man: I'm telling you, I did!
Man: You did not!
Other Man: Oh I'm sorry, is this a five minute argument, or the full half hour?
Man: Ah! (taking out his wallet and paying) Just the five minutes.
Other Man: Just the five minutes. Thank you.
Other Man: Anyway, I did.
Man: You most certainly did not!
Other Man: Now let's get one thing quite clear: I most definitely told you!
Man: Oh no you didn't!
Other Man: Oh yes I did!
Man: Oh no you didn't!
Other Man: Oh yes I did!
Man: Oh look, this isn't an argument!
(pause)
Other Man: Yes it is!
Man: No it isn't!
(pause)
Man: It's just contradiction!
Other Man: No it isn't!
Man: It IS!
Other Man: It is NOT!
Man: You just contradicted me!
Other Man: No I didn't!
Man: You DID!
Other Man: No no no!
Man: You did just then!
Other Man: Nonsense!
Man: (exasperated) Oh, this is futile!!
(pause)
Other Man: No it isn't!
Man: Yes it is!

'''
# We realized that for every line it has : followed by a space character, then the line of the man or other man

# We can extract parts of the line as required
# The split() method can help here.

'''
data = open('sketch.txt')
for i in data:
    (role, line_spoken) = i.split(':')
    print(role, end = '')
    print(' said: ', end = '')
    print(line_spoken, end = '')
'''
# We got an error in line 54 
'''
Traceback (most recent call last):
  File "C:/Users/Pc-41/Desktop/Python Examples/Head First Python/Chapter 3/split_method.py", line 54, in <module>
    (role, line_spoken) = i.split(':')
ValueError: too many values to unpack (expected 2)

'''
# It appears that there is something wrong with our data (ValueError)
'''
# Other Man: Now let's get one thing quite clear: I most definitely told you!
 In here we got 2 colon in one line that causes an error.
'''

# Split function has anoter attribute which limits the split number
# name.split(':', 1) // Limit our splitting :)

# Let's take the same code but changing this part
'''
data = open('sketch.txt')
for i in data:
    (role, line_spoken) = i.split(':', 1) # Put here , 1
    print(role, end = '')
    print(' said: ', end = '')
    print(line_spoken, end = '')
'''
# But there is again another error occured
# in line 79
# It caused because there are some line only contains (pause), and no colon :

# Now we have to add and extra logic to avoid tons of code for each specific line
# Using find() method

each_line = "I tell you, there's no such thing as a flying circus."
each_line.find(':')
# Gives result -1 means not found

each_line = "I tell you: there's no such thing as a flying circus."
each_line.find(':')
# Gives result 10 that means its in the 10th place


# Let's implement that logic:

data = open('sketch.txt')
for i in data:
    if not i.find(':') == -1: # If result of finding process is not equal -1, do the following!
        (role, line_spoken) = i.split(':', 1) # Put here , 1
        print(role, end = '')
        print(' said: ', end = '')
        print(line_spoken, end = '')
# Now It is working
