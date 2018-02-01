"""
The Data recording and processing program with the use of objects. Note that any new functionality that the method needs
should ideally get it's own dedicated method.
"""


# Classes:
class Athlete:
	def __init__(self, arg_name, arg_dob, arg_times):
		"""
		:param argName: 	The name of the athlete
		:param argDOB: 		The Date of birth of the athlete
		:param argTimes:	The list of times for each athlete.
		"""
		self.name = arg_name
		self.dob = arg_dob
		self.times = arg_times

	def top3(self):
		return sorted(set([sanitize(t) for t in self.times]))[0:3]


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

