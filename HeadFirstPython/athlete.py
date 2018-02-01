import os
james = []
julie = []
mikey = []
sarah = []

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
            for time in line.strip().split(','):
                mikey.append(time)

        for line in sarahData:
            for time in line.strip().split(','):
                sarah.append(time)

except Exception as err:
    print("File Error : " + str(err))

if not 'james' in locals() and 'julie' in locals() and 'mikey'  in locals() and 'sarah' in locals():
    print("Unable to add the data to the lists!")
    exit(1)

print("Times for James : " + str(james))
print("Times for Julie : " + str(julie))
print("Times for Mikey : " + str(mikey))
print("Times for Sarah : " + str(sarah))