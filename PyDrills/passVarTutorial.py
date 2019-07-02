#
# Python:   3.7.
#
# Author:   Edmund Alyn Jones
#
# Purpose: The Tech Academy - Python Course, Creating our first program together.
#          Demonstrating how to pass variables from function to function
#          while producinc a functional game.
#
#           Remember, function_name(variable) _means that we pass in the variable.
#           return variable _means that we are returning the variable to
#            back to the calling function.


def start():
    print("Hello {}!".format(get_name()))

def get_number():
    number = 12
    return number

def get_name():
    name = input("What is your name? ")
    return name






if __name__ == '__main__':
    start()
