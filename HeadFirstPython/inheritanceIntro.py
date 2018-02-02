"""
Python provides inheritance by simply including the name of the parent class in brackets, after the class identifier
declaration.
"""


class NamedList(list):				# This class derives from the list class.
	def __init__(self, a_name):
		list.__init__([])			# Call the constructor of the super-class and pass an empty list as argument.
		self.name = a_name


# Using the derived class:
johnny = NamedList("John Paul Jones")
print("Details for johnny object: ")
print(type(johnny))
print("Functionality provided by the object: ")
print(dir(johnny))					# Prints all the attributes and functions in the class: same as that of class `list`

johnny.append("Bass Player")
johnny.extend(['Composer', "Arranger", "Musician"])

print(johnny.name + " is a : " + str(johnny))