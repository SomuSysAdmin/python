"""
*Pickle* is a standard library for _Saving data to_ and _Loading data from_ files. The data can be saved from almost any
python data object, including lists. A standard library contians a bunch of pre-built functions that add a lot of
complex functionality that a coder would otherwise have to write by hand. Just one of these is the ability to read lists
from files!

The *Pickle* engine converts the data as stored in the memory to a format and stores it in the desired file. Next, when
the data needs to be re-read, the pickle engine loads the data from the file and converts it to the same format it was
in when first pickled.

The `dump` command saves (_pickled_) data while the `load` command loads (_pickled_) data from a file. The only
restriction with pickle is that the files have to be opened in binary access mode, i.e., `wb`.

This is an extremely powerful tool since we can write entire data-structures to a file using this method!
"""
import os
import pickle

# Section that creates the list from sketch.txt
man = []
other = []
try:
    os.chdir('/home/somu/Programming/python/HeadFirstPython')
    with open('sketch.txt') as data:
        for line in data:
            try:
                (role, dialog) = line.split(":", 1)
                dialog = dialog.strip()  # Strings are immutable, hence a new object with removed whitespace is assigned

                # Adding dialog to the correct list:
                if role == "Man":
                    man.append(dialog)
                elif role == "Other Man":
                    other.append(dialog)
            except ValueError:
                pass
except IOError as err:
    print("File Error: " + str(err))

# Directly printing the lists to files:
try:
    with open('saveDataFiles/pickle_man_data.txt', 'wb') as manOut, open('saveDataFiles/pickle_other_data.txt', 'wb') \
            as otherOut:
        pickle.dump(man, manOut)
        pickle.dump(other, otherOut)
        print("Files Written (as pickled data)!")
except IOError as err:
    print("File Error: " + str(err))

# Reading pickled data at a later point:
try:
    with open('saveDataFiles/pickle_man_data.txt', 'rb') as manIn, open('saveDataFiles/pickle_other_data.txt', 'rb') \
            as otherIn:
        man_list = pickle.load(manIn)
        other_list = pickle.load(otherIn)
except IOError as err:
    print("File Error: " + str(err))
except pickle.PickleError as perr:
    print("Pickle Error: " + str(perr))

if 'man_list' in locals() and 'other_list' in locals():
    for line in man_list:
        print(line)
    for line in other_list:
        print(line)




