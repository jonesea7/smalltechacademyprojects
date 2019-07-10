#
#   Purpose:    This piece of code creates an absolute path using the 'join' module.
#               


import os

fName = 'Hello.txt'

#Notice how we needed to use the escape backslash to insure we can use the backslashes to actually create the absolute file path.
fPath = 'C:\\PyProjects\\'

#here we set up a variable/container and linked it to
#the path.join module using the var fPath and fName to create an absolute path and file.
abPath = os.path.join(fPath, fName)
print(abPath)
