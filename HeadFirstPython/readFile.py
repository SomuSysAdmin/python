"""

Python gets data from files one line at a time. The `open()` BIF interacts with files and has to be used in combination
with a loop. The open() BIF fetches one line of data from the file and sends it to the file.

Since to open and operate on files we need help from the Operating System, we import the `os` module. Then, we can use
`os.getcwd()` to obtain the current working directory [equivalent of `pwd` in bash].

"""

import os

os.chdir('/home/somu/Programming/python/HeadFirstPython')  # Changes the working directory to the argument.
print("Present directory: ", os.getcwd())  # Prints the current working directory; Verifying the directory change.

data = open('sketch.txt')  # The open() command returns a stream to the data variable, which can provide the contents.

# Obtaining a single line of the file:
print("First Line:", data.readline(), end="")   # The end="" specifies the print statement to print nothing at the end
                                                #   instead of the usual `\n`.
print("Second Line:", data.readline())

# Rewinding the file
data.seek(0)    # We can also use tell(lineNo) to start reading from (lineNo+1)th line [Similar to array index].

# Using a for loop to print the entire file
for each_line in data:
    print(each_line, end="")    # We need the end="" to avoid printing additional newlines as the `\n`s in the file are
                                #   already printed.
print()     # Printing a blank line.

# Printing the entire file with while loop
data.seek(0)
lineNo = 1
line = data.readline()
while line:
    print(lineNo, ": ", line, sep="", end="")   # The sep="" states that there should be no seperator between strings.
                                                # The default value is sep=" ".
    line = data.readline()
    lineNo += 1

data.close()    # Closing the file once we're done with it.

