Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Get used to dictionaries
>>> cleese = {}
>>> palin = dict()
>>> type(cleese)
<class 'dict'>
>>> type(palin)
<class 'dict'>
>>> cleese['Name'] = "John Cleese"
>>> cleese['Occupations'] = ['actor', 'comedian', 'writer', 'film producer']
>>> palin = {'Name': 'Michael Palin}
	 
SyntaxError: EOL while scanning string literal
>>> palin = {'Name': 'Michael Palin', 'Occupations': ['comedian', 'actor', 'writer', 'tv' ]}
>>> palin['Name']
'Michael Palin'
>>> cleese['Occupations'][-1] # takes the last item in the dictionary
'film producer'
>>> palin['Birthplace'] = "Broomhill, Sheffield, England"
>>> cleese['Birthplace'] = "Weston-super-Mare, North Somerset, England"
>>> palin
{'Occupations': ['comedian', 'actor', 'writer', 'tv'], 'Name': 'Michael Palin', 'Birthplace': 'Broomhill, Sheffield, England'}
>>> cleese
{'Occupations': ['actor', 'comedian', 'writer', 'film producer'], 'Name': 'John Cleese', 'Birthplace': 'Weston-super-Mare, North Somerset, England'}
>>> 
