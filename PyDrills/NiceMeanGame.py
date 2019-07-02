#
# Python:   3.7
#
# Author:   Edmund Alyn Jones
#
# Purpose:  The Tech Academy - Python Course, Creating our first program together.
#           Demonstratin how to pass variables from function to function.
#           while producing a functional game.
#
#           Remember, myFunction(myVariable) means we add the variable.
#           Return variable implies we are calling the variable back to the invoked function.


def start(nice=0,mean=0,name=""):
    #get user's name
    #this line establishes the var called name and sets it equal to the function describeGame
    name = describeGame(name)
    #here we have three variables set up in conjunction with the function called niceMean
    nice,mean,name = niceMean(nice,mean,name)

def describeGame(name):
    """
        Check if this is a new game or not.
        If it is new, get the user's name.
        If it is not a new game, thank the player for
        playing agian and continue the game.
    """

    if name != "":
        print(f"\nThank you for playing again, {name}!")
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print(f"\nWelcome, {name}!")
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean.")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
# We have to return name here in order to add it to the variable we established and the very beginning of the program.
    return name 

def niceMean(nice,mean,name):
    stop = True
    while stop:
        showScore(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == 'n':
            print("\nThe stranger walks away smiling...")
            nice = (nice+1)
            stop = False
        if pick == 'm':
            print('\nThe stranger glares at you \nmenacingly and storms off...')
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) #We're going to pass the three variables to the score()  function.


def showScore(nice,mean,name):
    print(f"\n{name}, your current total: \n({nice}, Nice) and ({mean}, Mean)")



def score(nice,mean,name):
    if nice > 2:
        win(nice,mean,name)
    if mean > 2:
        lose(nice,mean,name)
    else:
        niceMean(nice,mean,name)


def win(nice,mean,name):
    print(f"\nNice job {name}, you win! \nEveryone loves you and you've made \nlots of friends along the way!")
    again(nice,mean,name)


def lose(nice,mean,name):
    print(f"\nAhhh too bad, game over! \n{name}, you live in a dirty beat-up \nvan by the river, wretched and alone!")
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n): \n>>>: ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go! Thanks for playing.")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    start(nice,mean,name)
        





if __name__ == "__main__":
    start()
