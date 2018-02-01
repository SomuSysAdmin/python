def data_grepper(file):
    try:
        with open(file) as data:
            return data.readline().strip().split(',')
    except IOError as err:
        print("File Error : " + str(err))


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

"""
Main Code:
==========
The code below does everything that athleteComprehension.py code does, but with far lesser effort.
"""
james = data_grepper('athleteTraining/james.txt')
julie = data_grepper('athleteTraining/julie.txt')
mikey = data_grepper('athleteTraining/mikey.txt')
sarah = data_grepper('athleteTraining/sarah.txt')

# Creating sets to store unique data:
print("\nProcessed using a set: ")
print("James'  top 3 times: " + str(sorted(set([sanitize(time) for time in james]))[0:3]))  # This is called function
                                                                                            # chaining
print("Julie's top 3 times: " + str(sorted(set([sanitize(time) for time in julie]))[0:3]))
print("Mikey's top 3 times: " + str(sorted(set([sanitize(time) for time in mikey]))[0:3]))
print("Sarah's top 3 times: " + str(sorted(set([sanitize(time) for time in sarah]))[0:3]))