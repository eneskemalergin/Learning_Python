# String Methods #

ss = "Hello, World"
print(ss.upper())

tt = ss.lower()
print(tt)

'''
Method 	    Parameters 	Description
upper 	    none 	Returns a string in all uppercase
lower 	    none 	Returns a string in all lowercase
capitalize  none 	Returns a string with first character capitalized, the rest lower
strip 	    none 	Returns a string with the leading and trailing whitespace removed
lstrip 	    none 	Returns a string with the leading whitespace removed
rstrip 	    none 	Returns a string with the trailing whitespace removed
count 	    item 	Returns the number of occurrences of item
replace     old, new 	Replaces all occurrences of old substring with new
center 	    width 	Returns a string centered in a field of width spaces
ljust 	    width 	Returns a string left justified in a field of width spaces
rjust 	    width 	Returns a string right justified in a field of width spaces
find 	    item 	Returns the leftmost index where the substring item is found
rfind 	    item 	Returns the rightmost index where the substring item is found
index 	    item 	Like find except causes a runtime error if item is not found
rindex 	    item 	Like rfind except causes a runtime error if item is not found
'''
ss = "    Hello, World    "

els = ss.count("l")
print(els)

print("***" + ss.strip() + "***")
print("***" + ss.lstrip() + "***")
print("***" + ss.rstrip() + "***")

news = ss.replace("o", "***")
print(news)

food = "banana bread"
print(food.capitalize())

print("*" + food.center(25) + "*")
print("*" + food.ljust(25) + "*")     # stars added to show bounds
print("*" + food.rjust(25) + "*")

print(food.find("e"))
print(food.find("na"))
print(food.find("b"))

print(food.rfind("e"))
print(food.rfind("na"))
print(food.rfind("b"))

print(food.index("e"))


