#	Author:		Edmund Alyn Jones
#
#	Purpose:	This scripts job is to check a specific folder on the hard drive
#				and verify whether a file ends with '.txt' file extension. If it does
#				the script should print the qualifying file names and time-stamps to the console for the user.
#	
#	File:		PyIODrill.py
#
#	Project:	GetThemTxtsYo!


#import os module
import os

#use the listdir() method from the os module to list directory in a folder.

#first we need to set variables for the path itself

pathName = 'C:\\Users\\'
userDirList = os.listdir(pathName)


def getDir():


    for file in userDirList:

        if 'txt' in file:
        
            #path.join to concat the file name to its file path. This allows us to print an absolute path to the console
            
            fullPath = os.path.join(pathName,file)
            
            #getmtime() is the method that will help us retrieve the timestamp for each file.
            
            timeStp = os.path.getmtime(fullPath)

            #Remember you need the script to print to the console the name of the 'txt' files AND their respective timestamps.

            print("The path is: " + fullPath + "\nThe last modification time is: " + str(timeStp))
                
        else:
            print('There are no files with the txt designation in this folder.')











if __name__ == "__main__":
    getDir()
  

