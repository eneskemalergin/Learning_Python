## Custom Data Objects V0.1
'''
# The exercise in Chapter 5 was great job, but to be sure which score who's score we should
# follow another approach...

# The coach upgraded the same files that we used before with adding the athlete's name

# Example Data "sarah2.txt" looks like this;
# Sarah Sweeney,2002-6-17,2:58,2.58,2:39,2-25,2-55,2:54,2.18,2:55,2:55,2:22,2-21,2.22

'''
# This version only gets the sarah's records.
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
# the pop(0) removes the first data from the list, then second pop(0) removes another first element
(sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
print(sarah_name + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in sarah])))[0:3])
