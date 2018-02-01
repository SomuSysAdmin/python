import os
james = []
julie = []
mikey = []
sarah = []

# Functions


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


def get_unique(timelist):
    unique_timelist = []
    for time in timelist:
        if time not in unique_timelist:
            unique_timelist.append(time)
    return unique_timelist


# Main program:
try:
    # Multiple open() functions in a single `with` statement.
    with open('athleteTraining/james.txt') as jamesData, open('athleteTraining/julie.txt') as julieData:
        line = jamesData.readline()
        for time in line.strip().split(','):        # This is called Method chaining.
            james.append(time)

        julie = julieData.readline().strip().split(',')     # Does the same thing as the above code-block

except IOError as err:
    print("File Error : " + str(err))

mikey = data_grepper('athleteTraining/mikey.txt')   # Does the same thing as above, but directly from the file name.
sarah = data_grepper('athleteTraining/sarah.txt')

if not 'james' in locals() and 'julie' in locals() and 'mikey' in locals() and 'sarah' in locals():
    print("Unable to add the data to the lists!")
    exit(1)

# Sorted lists below:
clean_james = sorted([sanitize(time) for time in james])
clean_julie = sorted([sanitize(time) for time in julie])
clean_mikey = sorted([sanitize(time) for time in mikey])
clean_sarah = sorted([sanitize(time) for time in sarah])

"""
Printing only a section of the list using list-slices:
======================================================
A list slice is a special notation that returns a subset of the list. Thus, to print only the first 3 elements in that
list, we could either write : listName[0], listName[1] and listName[2] or simply replace it with a slice listName[0:3].
Note that the slice is to print from the indices m-n, the notation is : listName[m,n+1]. 
"""

# Creating unique lists using loops:
unique_james = get_unique(clean_james)
unique_julie = get_unique(clean_julie)
unique_mikey = get_unique(clean_mikey)
unique_sarah = get_unique(clean_sarah)

print("\nProcessed using a loop: ")
print("James'  top 3 times: " + str(unique_james[0:3]))
print("Julie's top 3 times: " + str(unique_julie[0:3]))
print("Mikey's top 3 times: " + str(unique_mikey[0:3]))
print("Sarah's top 3 times: " + str(unique_sarah[0:3]))

"""
The code below does everything that the above code does, but with far lesser effort. 
"""
# Creating sets to store unique data:
print("\nProcessed using a set: ")
print("James'  top 3 times: " + str(sorted(set([sanitize(time) for time in james]))[0:3]))  # This is called function
                                                                                            # chaining
print("Julie's top 3 times: " + str(sorted(set([sanitize(time) for time in julie]))[0:3]))
print("Mikey's top 3 times: " + str(sorted(set([sanitize(time) for time in mikey]))[0:3]))
print("Sarah's top 3 times: " + str(sorted(set([sanitize(time) for time in sarah]))[0:3]))