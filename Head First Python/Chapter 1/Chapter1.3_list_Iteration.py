# List Iteration

# We can mix the data types in the list it is OK!
movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]

movies.insert(1,1975) # Inserts int 1975 to index 1
movies.insert(3,1979) # Inserts int 1979 to index 3
movies.append(1983) # Inserts int 1983 at the end

# OR

movies = ["The Holy Grail", 1975,
            "The Life of Brian", 1979,
            "The Meaning of Life", 1983]
# The second one is better for small lists

# If we want to print the each item in the list we can use either
# Printing one by one:

print(movies[0])
print(movies[1])
print(movies[2])
print(movies[3])
print(movies[4])

# OR better and faster for bigger lists:
# Iterating each item in the list and print it.
# This is for loop syntax
for i in movies:
    print(i)

# Also we have the while loop syntax

count = 0
while count < len(movies):
    print(movies[count])
    count += 1 # count = count +1

