"""
The Data recording and processing program with the use of a derived class of `list` data structure.
"""


# Classes:
class Athlete(list):
	def __init__(self, arg_name, arg_dob=None, arg_times=[]):
		"""
		:param arg_name: 	The name of the athlete
		:param arg_dob: 	The Date of birth of the athlete
		:param arg_times:	The list of times for each athlete.
		"""
		list.__init__([])
		self.name = arg_name
		self.dob = arg_dob
		self.extend(arg_times)

	def top3(self):
		return sorted(set([sanitize(t) for t in self]))[0:3]


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

# Testing code for new functionality - we simply use the objects of the class as any other list!
vera = Athlete('Vera Vi', '1991-01-02')
vera.append('1.31')
printObj(vera)
vera.extend(['2.22', "1-21", '2:22'])
printObj(vera)