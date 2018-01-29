# Custom Functions:


def list_print(subject, dest=None):
    for dia in subject:
        if dest is not None:
            print(dia, file=dest)
        else:
            print(dia)


# Creating the data to be saved.
man = []
other = []

try:
    data = open('sketch.txt')
    for line in data:
        try:
            (role, dialog) = line.split(":", 1)
            dialog = dialog.strip()

            # Adding dialog to the correct list:
            if role == "Man":
                man.append(dialog)
            elif role == "Other Man":
                other.append(dialog)
        except ValueError:
            pass
    data.close()
except IOError:
    print("The file wasn't found.")
    exit(1)

try:
    manOut = open("saveDataFiles/man_data.txt", 'w')
    otherOut = open("saveDataFiles/other_data.txt", 'w')
    """
    The above two files are opened in *Write*(w) mode, and this causes the existing data in these files to be erased 
        also known as _clobbering_, every time the files are opened. To prevent this, i.e., to append files we should 
        use open the files in _Access_(a) mode. If the files don't exist, they'll be created and then opened (written 
        to). To open file both for reading and writing (without clobbering) we use `w+` mode. 
    """
except IOError:
    print("There was a problem while writing to the files!")

print("Writing to man_data.txt...", end="")
print("Dialogs for Man: \n", file = manOut)
list_print(man, manOut)
print("\t\tDONE!\nWriting to other_data.txt...", end="")
print("Dialogs for Other Man: \n", file = otherOut)
list_print(other, otherOut)
print("\tDONE!")
