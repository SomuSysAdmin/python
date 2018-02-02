import os
"""
We need to create a README.md file and fill its contents with that of the fileOrder.md file, but also, replace each
    file entry with an appropriate hyperlink.
"""

os.chdir('/home/somu/Programming/python/SysAdminPython')
try:
    with open ('fileOrder.md') as readFile, open("README.md", 'w') as writeFile:
        print("## Tutorials for System Administraiton & Automation using Python", file=writeFile)
        for line in readFile:
            if '-' in line and ".py" in line:
                startIdx = line.find("-")+2
                writeLoc = line.find(".py")+3
                link = (line[startIdx:writeLoc])
                newLine = line[0:startIdx] + "[" + link + "]" + "(" + link + ")" + line[writeLoc:]
                print(newLine, end="", file = writeFile)
            else:
                print(line, end="", file = writeFile)
except Exception as err:
    print("File Error: " + str(err))

print("\nREADME.md File Written!")
