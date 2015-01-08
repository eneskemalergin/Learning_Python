## Custom Data Objects V0.2

''' The version 0.1 is working quite well but imagine that we are doing the same process
for other 3 athletes as well. It will be 12 more lines. It is ok for 3 more but imagine if
you would have 3000 more...
    Then you need another solution...
    '''

# Lists are great but they are not the best data structure for every situation

# In Sarah's data we can group the data into 3 groups. full name, dob, timing data

# There is another built-in data structure of Python step in here: "Dictionaries"

# They are associates data values with keys:

'''
Keys    values
----    ------
Name -> "Sarah Sweeney"
DOB  -> "2002-6-17"
Times-> [2:58,2.58,2:39,2-25,2-55,2:54,2.18,2:55,2:55,2:22,2-21,2.22]

'''
# Let's apply the dictionary principle into our new approach

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return(data.strip().split(','))
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)

sarah = get_coach_data('sarah2.txt')
sarah_data = {}
sarah_data['Name'] = sarah.pop(0)
sarah_data['DOB'] = sarah.pop(0)
sarah_data['Times'] = sarah
print(sarah_data['Name'] + "'s fastest times are: " +
    str(sorted(set([sanitize(t) for t in sarah_data['Times']]))[0:3]))
