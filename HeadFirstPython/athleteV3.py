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
            athlete = {}
            line = data.readline().strip().split(',')
            athlete['Name'] = line.pop(0)
            athlete['DOB'] = line.pop(0)

            # Sanitizing the data
            athlete['Times'] = sorted(set([sanitize(t) for t in line]))[0:3]
            return athlete
    except IOError as err:
        print("File Error : " + str(err))


# Main code

james = data_grepper('athleteTraining/james2.txt')  # Contains raw data from each of the files.
julie = data_grepper('athleteTraining/julie2.txt')
mikey = data_grepper('athleteTraining/mikey2.txt')
sarah = data_grepper('athleteTraining/sarah2.txt')

print(james['Name'] + ", born on " + james['DOB'] + " has the fastest times of : " + str(james['Times']), sep="")
print(julie['Name'] + ", born on " + julie['DOB'] + " has the fastest times of : " + str(julie['Times']), sep="")
print(mikey['Name'] + ", born on " + mikey['DOB'] + " has the fastest times of : " + str(mikey['Times']), sep="")
print(sarah['Name'] + ", born on " + sarah['DOB'] + " has the fastest times of : " + str(sarah['Times']), sep="")
