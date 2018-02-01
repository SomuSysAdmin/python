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


# Main code

james = data_grepper('athleteTraining/james2.txt')  # Contains raw data from each of the files.
julie = data_grepper('athleteTraining/julie2.txt')
mikey = data_grepper('athleteTraining/mikey2.txt')
sarah = data_grepper('athleteTraining/sarah2.txt')

(sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)    # Each pop function returns the value of the element deleted.
sarah_time = sorted(set([sanitize(t) for t in sarah]))[0:3]
print("Data obtained without a dictionary: ")
print(sarah_name + ", born on " + sarah_dob + " has the fastest times of : " + str(sarah_time), sep="")
sarah = data_grepper('athleteTraining/sarah2.txt')  # Resetting the list.

print("\nData obtained with a dictionary: ")
sarah_data = {}
sarah_data['Name'] = sarah.pop(0)
sarah_data['DOB'] = sarah.pop(0)
sarah_data['Times'] = sorted(set([sanitize(t) for t in sarah]))[0:3]
print(sarah_data['Name'] + ", born on " + sarah_data['DOB'] + " has the fastest times of : " + str(sarah_data['Times']), sep="")
