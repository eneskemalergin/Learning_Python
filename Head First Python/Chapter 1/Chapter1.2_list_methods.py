## List Methods

# Creats list called cast
cast = ["Cheese", "Palin", "Jones", "Idle"]
print(cast) # Show the list

# len() function shows the number of elements in the list
print(len(cast))

# Prints the second element in the list
print(cast[1])

# append() function takes a new element and add it to list / It can only take one element
cast.append("Gilliam")
print(cast)

# It deletes the last element on the list and returns the list
cast.pop()

# extend() function add the collection of elements to en of the list
cast.extend(["Gilliam", "Chapman"])
print(cast)

# It removes a specific element 
cast.remove("Chapman")
print(cast)

# It adds an element in the specified location
cast.insert(0,"Chapman")


