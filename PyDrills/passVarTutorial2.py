def start():
    fName = "Sarah"
    lName = "Connor"
    age = 28
    gender = "female"
    getName(fName,lName,age,gender)

def getName(fName,lName,age,gender):
    print(f'My name is {fName} {lName}. I am {age} years old, {gender}.')



if __name__ == "__main__":
    start()
