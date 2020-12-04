import random

codeLength = 4
maxRound = 8

def start():
    '''Runs before the game starts'''
    print("Welcome to Mastermind") 
    response = input("Press any button to start, or Q to quit: ")
    if(response=="Q" or response=="q"):
        quit()
    secret = randCode()
    currentRound = 1
    won = False
    while currentRound <= maxRound and not won:
        response = input("Guess the code... ")
        response = response.upper() #convert their guess into uppercase
        result = codeTest(secret, response)
        if result == ["R", "R", "R", "R"]:
            won = True
            print("YOU WON!")
        elif currentRound == maxRound:
            print("You Lost!")
            print("Correct code was: " + str(secret))
        else:
            roundDisplay(result,currentRound,response)
        currentRound += 1

def randCode():
    '''Generated the random code for the user to guess'''
    colours = ["B","G","M","O","P","Y"]
    random.shuffle(colours)
    colours.pop()
    colours.pop()
    return(colours)


def roundDisplay(result, roundNum, code):
    '''Basic CLI output formatting'''
    print("Round           " + result[0] + " " + result[1])
    print("No. " + str(roundNum) + "   " + code)
    print("of " + str(maxRound) + "            " + result[2] + " " + result[3])

def codeTest(secret, response):
    ''' Takes the users input and the predefined secret
        Returns " " if guess isn't in the secret
        Returns "W" if guess is in the secret but in the wrong location
        Returns "R" if guess is in the secret and in the correct location'''
    i = 0
    result = []
    while i < codeLength:
        if response[i] not in secret:
            result.append(" ")
        elif response[i] == secret[i]:
            result.append("R")
        else:
            result.append("W")
        i += 1
    random.shuffle(result)
    return(result)

start()