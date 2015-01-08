Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Getting_used_to_inheritance
>>> class NamedList(list):
	def __init__(self, a_name):
		list.__init__([])
		self.name = a_name

		
>>> johnny = NamedList("John Paul Jones")
>>> type(johnny)
<class '__main__.NamedList'>
>>> dir(johnny) # johnny can do everything that list could do
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'name', 'pop', 'remove', 'reverse', 'sort']
>>> # with plus name attribute that we put
>>> johnny.append("Bass Player")
>>> johhny.extend(["Composer", "Arranger", "Musician"])
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    johhny.extend(["Composer", "Arranger", "Musician"])
NameError: name 'johhny' is not defined
>>> johnny.extend(["Composer", "Arranger", "Musician"])
>>> johnny
['Bass Player', 'Composer', 'Arranger', 'Musician']
>>> johnny.name
'John Paul Jones'
>>> for attr in johnny:
	print(johnny.name + " is a " + attr + ".")

	
John Paul Jones is a Bass Player.
John Paul Jones is a Composer.
John Paul Jones is a Arranger.
John Paul Jones is a Musician.
>>> 
