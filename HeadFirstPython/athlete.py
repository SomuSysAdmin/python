import os
james = []
julie = []
mikey = []
sarah = []

# Functions


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

try:
    with open('athleteTraining/james.txt') as jamesData, open('athleteTraining/julie.txt') as julieData, \
            open('athleteTraining/mikey.txt') as mikeyData, open('athleteTraining/sarah.txt') as sarahData:
        for line in jamesData:
            for time in line.strip().split(','):        # This is called Method chaining.
                james.append(sanitize(time))

        for line in julieData:
            for time in line.strip().split(','):
                julie.append(sanitize(time))

        for line in mikeyData:
            for time in line.strip().split(','):
                mikey.append(sanitize(time))

        for line in sarahData:
            for time in line.strip().split(','):
                sarah.append(sanitize(time))

except Exception as err:
    print("File Error : " + str(err))

if not 'james' in locals() and 'julie' in locals() and 'mikey'  in locals() and 'sarah' in locals():
    print("Unable to add the data to the lists!")
    exit(1)

print("Sorted Times for James : " + str(sorted(james)))     # This is called function chaining.
print("Sorted Times for Julie : " + str(sorted(julie)))
print("Sorted Times for Mikey : " + str(sorted(mikey)))
print("Sorted Times for Sarah : " + str(sorted(sarah)))