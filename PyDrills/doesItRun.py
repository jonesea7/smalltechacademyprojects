import os

#let's cook up a directory and some files for this wonderful exercise.

newFileList = ['eddy.txt', 'jones.txt', 'samson.py', 'miracle.html', 'gary.txt', 'fallout3.html', 'pizza.txt', 'erick.py', 'malcolm.html', 'lather.py']

pathName = 'C:\\Users\\'

def createDir():
    for filename in newFileList:
        newDir = os.path.join(pathName,filename)
        print(newDir)

createDir()
