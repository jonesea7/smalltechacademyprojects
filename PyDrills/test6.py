
def getInfo():
    var1 = input('Please provide the first numeric value: ')
    var2 = input('Please provide the second numeric value: ')
    compute(var1, var2)
    
def compute(var1, var2):
    try:
        var3 = int(var1) + int(var2)
        print(f'{var1} + {var2} = {var3}')
    except ValueError:
        print('You did not provide a numeric value')
    except:
        print('Oops, invalid input, program will close now')
    
        







if __name__ == "__main__":
    getInfo()
    
