#	Author:		Edmund Alyn Jones
#
#	Purpose:	This scripts job is to check a specific folder on the hard drive
#				and verify whether a file ends with '.txt' file extension. If it does
#				the script should print the qualifying file names and time-stamps to the console for the user.
#	
#	File:		IODrill.py
#
#	Project:	GetThemTxtsYo!


#import os module
import os

#use the listdir() method from the os module to list directory in a folder.

#first we need to set variables for the path itself

pathName = 'C:\\'
userDirList = os.listdir(pathName)


def getDir():
	for file in userDirList:
		print(file)

#path.join to concat the file name to its file path. This allows us to print an absolute path to the console

def creatAbPath():
	for root, dir, filename in userDirList():
		fullPath = join(root, dir, filename)
		print(fullPath)

#getmtime() is the method that will help us retrieve the timestamp for each file.

#Remember you need the script to print to the console the name of the 'txt' files AND their respective timestamps.

if __name__ == "__main__":
	getDir()
	createAbPath()