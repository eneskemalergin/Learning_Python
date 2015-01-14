# AthleteList class


class AthleteList(list):

    def __init__(self, a_name, a_dob = None, a_times = []):
        list.__init__([]) # This called the list data structure...
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times) # Changed

    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])
