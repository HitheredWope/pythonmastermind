
maxRound = 8

def start():
    '''Runs before the game starts'''
    print("Welcome to Mastermind") 
    response = input("Press any button to start, or Q to quit: ")
    if(response=="Q" or response=="q"):
        quit()
    else:
        print("GAME")
def roundDisplay(result, roundNum, code):
    print("Round          " + result[0] + " " + result[1])
    print("No. " + str(roundNum) + "   " + code)
    print("  " + str(maxRound) + "            " + result[2] + " " + result[3])

#result = ["W", "W", "R", " "]
#roundNum = 1
#code = "BGMO"
