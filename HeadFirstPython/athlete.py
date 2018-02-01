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
                james.append(time)

        for line in julieData:
            for time in line.strip().split(','):
                julie.append(time)

        for line in mikeyData:
            mikey = line.strip().split(',')     # Does the same thing as above, since a list is returned by split().

        for line in sarahData:
            sarah = line.strip().split(',')

except Exception as err:
    print("File Error : " + str(err))

if not 'james' in locals() and 'julie' in locals() and 'mikey' in locals() and 'sarah' in locals():
    print("Unable to add the data to the lists!")
    exit(1)

# Sorted lists below:

clean_james = []
for time in james:
    clean_james.append(sanitize(time))

clean_julie = []
for time in julie:
    clean_julie.append(sanitize(time))
"""
This operation (and others like it) are called list transformation. The need to transform lists, i.e., created a new 
list from the processed data from an existing list, is so frequent, that python provides a set of tools called *list 
comprehensions* to do it.  The same code as above can be written with list comprehensions as:
"""
clean_mikey = [sanitize(time) for time in mikey]
clean_sarah = [sanitize(time) for time in sarah]

print("Sorted Times for James : " + str(sorted(clean_james)))     # This is called function chaining.
print("Sorted Times for Julie : " + str(sorted(clean_julie)))
print("Sorted Times for Mikey : " + str(sorted(clean_mikey)))
print("Sorted Times for Sarah : " + str(sorted(clean_sarah)))