import os

def writeData():
    data = '\nHello World'
    with open('i_o_test.txt', 'a') as f:
        f.write(data)
        f.close()

def openFile():
    with open('i_o_test.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()

if __name__ == '__main__':
    writeData()
    openFile()
