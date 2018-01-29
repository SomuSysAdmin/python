import os
"""
We need to create a README.md file and fill its contents with that of the fileOrder.md file, but also, replace each 
    file entry with an appropriate hyperlink. 
"""

os.chdir('/home/somu/Programming/python/HeadFirstPython')
readFile = open ('fileOrder.md')
writeFile = open("README.md", 'w')

print("## SomuSysAdmin Python Tutorials", file = writeFile)
for line in readFile:
    if '-' in line and ".py" in line:
        startIdx = line.find("-")+2
        writeLoc = line.find(".py")+3
        link = (line[startIdx:writeLoc])
        newLine = line[0:startIdx] + "[" + link + "]" + "(" + link + ")" + line[writeLoc:]
        print(newLine, end="", file = writeFile)
    else:
        print(line, end="", file = writeFile)

print("\nREADME.md File Written!")