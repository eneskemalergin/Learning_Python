#Inputting:

''' There are two main types of getting onput from the user:
        1-) input()
        2-) raw_input()

        input() takes whatever type that user puts, but carefull
                user should put the value in right syntax otherwise
                input() function throws an error
            For instance:
                >>> m = input("Enter:")
                >>> Enter: 1
                # than no problem it takes as an integer
                >>> m = input("Enter:")
                >>> Enter: String
                # There is a problem it wont understand that
                You should solve this problem with changing String to
                "String" with quotation marks around.
        raw_input() takes whatever type that user puts and returns to
                    string. So if you wnat to use this to take value from user
                    try to remember to use convertions
'''

n = input("Please enter your name: ")
print "Hello", n
n = raw_input("Please enter your name: ")
print "Hello", n
        
