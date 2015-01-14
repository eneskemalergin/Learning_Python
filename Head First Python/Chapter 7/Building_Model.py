## Building a model

''' Your web server needs to store a single copy of your data, which in this case is
Coach Kelly’s timing values (which start out in his text files). '''


'''When your webapp starts, the data in the text files needs to be converted
to AthleteList object instances, stored within a dictionary (indexed by
athlete name), and then saved as a pickle file. Let’s put this functionality in a
new function called put_to_store().
'''

'''
While your webapp runs, the data in the pickle needs to be available to your
webapp as a dictionary. Let’s put this functionality in another new function
called get_from_store().
'''

import pickle

import AthleteList

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return(AthleteList(templ.pop(0),templ.pop(0),templ))
    except IOError as ioerr:
        print('File error: ' + str (ioerr))
        return(None)

def put_to_store(files_list):

    all_athletes = {}
    for each_file in files_list:
        # Takes each file , turn it into an AthleteList object instance, and add the athlete's
        # data to the dictionary
        ath = get_coach_data(each_file)
        # Each athlete's name is used as the "key" in the dictionary.
        # The "value" is the AthleteList object instance
        all_athletes[ath.name] = ath

    try:
        with open('athletes.pickle', 'wb') as athf:
            #Save the entire dictionary of AthleteList to a pickle
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        # And don't forget a try/except to protect your file I/O code
        print("File error (put_and_store):" + str(ioerr))

    return(all_athletes)

def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            # Simply read the entire picke into the dictionary. What could be easier?
            all_athletes = pickle.load(athf)

    except IOError as ioerr:
        # Again... don't forget your try/except
        print("File error (get_from_store):" + str(ioerr))

    return(all_athletes)
