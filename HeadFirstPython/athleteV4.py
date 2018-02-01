"""
The Data recording and processing program with the use of objects. Note that any new functionality that the method needs
should ideally get it's own dedicated method.
"""


# Classes:
class Athlete:
	def __init__(self, arg_name, arg_dob=None, arg_times=[]):
		"""
		:param arg_name: 	The name of the athlete
		:param arg_dob: 	The Date of birth of the athlete
		:param arg_times:	The list of times for each athlete.
		"""
		self.name = arg_name
		self.dob = arg_dob
		self.times = arg_times
	"""
	We're storing the entire list of times, instead of just the top 3 since we might need to extend the functionality of 
	the program in the future, and in such cases the flexible design of a function helps a lot.
	"""

	def top3(self):
		return sorted(set([sanitize(t) for t in self.times]))[0:3]

	"""
	We're adding two new methods : add_time(), which adds a single time to the record and add_times() which adds multiple
	"""

	def add_time(self, t):
		self.times.append(t)

	def add_times(self, t):
		self.times.extend(t)


# Static Methods:
def sanitize(time_string):
	"""
	:param time_string: Input time string, which may have mins and seconds separated by either ':', '-' or '.'
	:return:            Uniformly formatted time string with mins and secs separated by '.'
	"""
	if "-" in time_string:
		splitter = "-"
	elif ":" in time_string:
		splitter = ":"
	else:
		return time_string
	(mins, secs) = time_string.split(splitter)
	return mins + "." + secs


def data_grepper(file):
	try:
		with open(file) as data:
			line = data.readline().strip().split(',')
			athlete = Athlete(line.pop(0), line.pop(0), line)
			return athlete
	except IOError as err:
		print("File Error : " + str(err))


def printObj(ath):
	print(ath.name + ", born on " + ath.dob + ", has the top 3 times of : " + str(ath.top3()))


james = data_grepper('athleteTraining/james2.txt')  # Contains reference to an object holding all the related data.
julie = data_grepper('athleteTraining/julie2.txt')
mikey = data_grepper('athleteTraining/mikey2.txt')
sarah = data_grepper('athleteTraining/sarah2.txt')

printObj(james)
printObj(julie)
printObj(mikey)
printObj(sarah)

# Testing code for new functionality:
vera = Athlete('Vera Vi', '1991-01-02')
vera.add_time('1.31')
printObj(vera)
vera.add_times(['2.22', "1-21", '2:22'])
printObj(vera)
