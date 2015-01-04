# Length #


''' len functions gives you the lenght of characters '''

fruit = "Banana"
print(len(fruit))

#---------------------------------------------------------------#

''' You can take specific characters from the string. Using indexing '''
fruit = "Banana"
sz = len(fruit)
lastch = fruit[sz-1] # Careful you need to use size - 1 
print(lastch)

#######################################################################

# The Slice Operator #

''' Slicing feature gives you the ability to take specific character group
        using intervals
'''
singers = "Peter, Paul, and Mary"
print(singers[0:5])
print(singers[7:11])
print(singers[17:21])


fruit = "banana"
print(fruit[:3]) # Starts the beginning till the 3rd one
print(fruit[3:]) # Starts from the 3rd onr till end


#######################################################################

# String Comparison #

word = "banana"
if word == "banana":
    print("Yes, we have bananas!")
else:
    print("Yes, we have NO bananas!")


word = "zebra"

if word < "banana":
    print("Your word, " + word + ", comes before banana.")
elif word > "banana":
    print("Your word, " + word + ", comes after banana.")
else:
    print("Yes, we have no bananas!")


print("apple" < "banana")

print("apple" == "Apple")
print("apple" < "Apple")


print(ord("A"))
print(ord("B"))
print(ord("5"))

print(ord("a"))
print("apple" > "Apple")

print(chr(65))
print(chr(66))

print(chr(49))
print(chr(53))

print("The character for 32 is", chr(32), "!!!")
print(ord(" "))



