### Strings and Lists ###

''' The split method breaks a string into a list of words '''
''' by default, any number of whitespace characters is considered a word boundary '''

song = "The rain in Spain..."
wds = song.split() #It splited by default
print(wds)

''' What if we out a delimeter '''

song = "The rain in Spain..."
wds = song.split('ai') # Now it will split when it see ai
print(wds)

# If you noticed that ai won't be seeing in the result

'''The inverse of the split method is join. You choose a desired separator string,
(often called the glue) and join the list with the glue between each of the elements '''

wds = ["red", "blue", "green"]
glue = ';'
s = glue.join(wds)
print(s)
print(wds)

print("***".join(wds))
print("".join(wds))

## list type conversion function ##

xs = list("Crunchy Frog")
print(xs)
