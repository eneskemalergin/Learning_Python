# Storing lists within lists

''' We can embed the lists inside another lists. '''

movies = [
    "The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
        ["Graham Chapman",
            ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
# We put 2 more lists inside the outter list and at the end we have 3 closing square bracktes

# To get the value in inner lists:
print(movies[4][1][3])

# But what happens if we want to use loops to print items
for each_item in movies:
    print(each_item)
# This function output this:
'''
The Holy Grail
1975
Terry Jones & Terry Gilliam
91
['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]
'''
# it is not quite right, How we can solve this problem?

for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            print(nested_item)
    else:
        print(each_item)
# The code above will improve a little but not enough

for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            if isinstance(nested_item, list):
                for deeper_item in nested_item:
                    print(deeper_item)
            else:
                print(nested_item)
    else:
        print(each_item)
# Know It is true.

# There is another way, more useful and applicable way

# We can create a function to handle this problem in less code
def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)

print_lol(movies)
