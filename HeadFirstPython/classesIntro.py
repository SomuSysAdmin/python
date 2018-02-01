"""
The functions in classes are called methods, the data members are called attributes, and the objects created from the
classes are called instances. The classes are defined with the `class` keyword.

The constructors are defined with the `__init__()` keyword. Note that unlike C++ or Java, Python doesn't have the
concept of causing a constructor call (via object creation) through the `new` keyword. Python automatically creates the
object and then if `__init__()` method exists, initializes the construction specific to the provided instructions.

The `self` keyword

Thus, a class with a constructor for athletes will look like:
"""


class Monty:                      	# Classes generally have an identifier that starts with a capital letter.

	def __init__(self, value=0):		# The constructor doesn't have the same name as the class.
		self.thing = value				# Code for the class.

	def how_big(self):
		return len(self.thing)


# Object creation and instantiation:
a = Monty("Holy Grail")		# This is called a factory function and the constructor call is
							# --> Monty().__init__(a. "Holy Grail")
b = Monty("Life of Brian")	# --> Monty().__init__(b, 'The life of Brian")
"""
The factory function's call auto-assigns the value of the referencing variable to the `self` parameter of the `__init__`
function. Thus, the actual value of the object, i.e., the reference to the object in the memory is passed via `self`. 
This is critical due to the fact that the python needs the first argument of every method in the class to be `self` to 
understand which object caused a function call. By the very nature, the methods are shared among objects, while the 
attributes each get a copy assigned to the specific object. Thus the use of `self` identifies which copy of the data 
should be edited for each function call. 
"""
print("Length of 'Holy Grail' : " + str(a.how_big()))
print("Length of 'The life of Brian' :  " + str(b.how_big()))

class Athlete:
	def __init__(self, a_name, a_dob=None, a_times=[]):		# Default values passed as parameters
		self.name = a_name
		self.dob = a_dob
		self.times = a_times

	def value_dump(self):
		print(self.name)
		print(self.times)

# Main code


sarah = Athlete('Sarah Sweeney', '2002-6-17', ['2:58', '2.58', '1.56'])
james = Athlete('James Jones')		# Object created with the default values

print("\nTypes of Sarah and James objects:")
print(type(sarah))		# Both belong to <class '__main__.Athlete'>
print(type(james))

print("\nPrinting object references for Sarah and James:")
print(sarah)			# Output is memory locations where these objects are stored.
print(james)

print("\nPrinting Attribute Values:")
print("Values in Sarah: ")
sarah.value_dump()
print(sarah.dob)
print("Values in James: ")
james.value_dump()
print(james.dob)

