# -*- coding: cp1252 -*-
# Error Types #
'''
    *Many problems in your program will lead to an error message.
Can You say what is wrong with this code by simply looking at it? No... 
current_time_str = input("What is the current time (in hours 0-23)?")
wait_time_str = input("How many hours do you want to wait")

current_time_int = int(current_time_str)
wait_time_int = int(wait_time_int)

final_time_int = current_time_int + wait_time_int
print(final_time_int)

NameError: name 'wait_time_int' is not defined
'''

#ParseError
'''
Parse errors happen when you make an error in the syntax of your program. 
If you don’t use periods and commas in your writing then you are making
it hard for other readers to figure out what you are trying to say.
Similarly Python has certain grammatical rules that must be followed
or else Python can’t figure out what you are trying to say.
####
Usually ParseErrors can be traced back to missing punctuation characters,
such as parenthesis, quotation marks, or commas. 
####
'''
#TypeError
'''
TypeErrors occur when you you try to combine two objects that are not
compatible. For example you try to add together an integer and a string.
Usually type errors can be isolated to lines that are using mathematical
operators, and usually the line number given by the error message is an
accurate indication of the line.
'''
#NameError
'''
Name errors almost always mean that you have used a variable before it
has a value. Often NameErrors are simply caused by typos in your code.
They can be hard to spot if you don’t have a good eye for catching
spelling mistakes. Other times you may simply mis-remember the name of a
variable or even a function you want to call.
'''
#ValueError
'''
Value errors occur when you pass a parameter to a function and the
function is expecting a certain type, but you pass it a different type. 
'''


















