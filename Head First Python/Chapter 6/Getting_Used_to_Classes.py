Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Getting_Used_to_Classes
>>> class Athlete:
	def __init__(self, a name, a_dob = None, a_times = []):
		
SyntaxError: invalid syntax
>>> class Athlete:
	def __init__(self, a_name, a_dob = None, a_times = []):
		self.name = a_name
		self.dob = a_dob
		self.times = a_times

		
>>> sarah = Athlete('Sarah Sweeney', '2002-6-17', ['2:58', '2.58', '1.56'])
>>> james = Athlete('James Jones')
>>> type(sarah)
<class '__main__.Athlete'>
>>> type(james)
<class '__main__.Athlete'>
>>> sarah
<__main__.Athlete object at 0x0000000004004F60>
>>> james
<__main__.Athlete object at 0x0000000004070B38>
>>> sarah.name
'Sarah Sweeney'
>>> james.name
'James Jones'
>>> sarah.dob
'2002-6-17'
>>> james.dob
>>> sarah.times
['2:58', '2.58', '1.56']
>>> james.times # we did not initialize it yet
[]
>>> 
