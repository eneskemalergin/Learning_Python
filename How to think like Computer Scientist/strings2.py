''' Traversal and the for loop by item:  Strings '''

'''Often we start at the beginning, select each character in turn, do something to it,
    and continue until the end. This pattern of processing is called a traversal.
'''

for aname in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
    invitation = "Hi " + aname + ".  Please come to my party on Saturday!"
    print(invitation)
#############################################################################
for avalue in range(10):
    print(avalue)
#----------------------------------------------------------------------------#
# It goes with character by character ...
for achar in "Go Spot Go":
    print(achar)

''' Traversal and the for loop by index:  Strings '''

fruit = "apple"
for idx in range(len(fruit)):
    print(fruit[idx])

''' Traversal and the while loop:  Strings '''

fruit = "apple"

position = 0 # initialization and keep track of the count.
while position < len(fruit):
    print(fruit[position])
    position = position + 1
