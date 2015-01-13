Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> def f(x):
	return x + a

>>> a = 3
>>> f(1)
4
>>> x = 12
>>> def g(x):
	x = x + 1
	def h(y):
		return(x + y)
	return h(6)

>>> g(x)
19
>>> 
