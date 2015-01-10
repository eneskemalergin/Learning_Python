## L3 - P6 - Q3

iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print ("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
