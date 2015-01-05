def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splinter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.splint(splitter)
    return(mins + '.' + secs)
