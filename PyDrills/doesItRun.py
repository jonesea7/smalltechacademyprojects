import os


pathName = 'C:\\Documents and Settings\\'
userDirList = os.listdir(pathName)

def getDir():
    for file in userDirList:
        print(file)

if __name__ == '__main__':
    getDir()
