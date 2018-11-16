import random
import time
import os
print()
print('''gamarjoba chemi pirveli programaa 
 shen daiwyeb  ?50 
shegidzlia gamoiyeno yes/no. aseve shegidzlia gamoiyeno y/n
BAR\tBAR\tBAR\t\tpays\t?250
BELL\tBELL\tBELL/BAR\tpays\t?20
PLUM\tPLUM\tPLUM/BAR\tpays\t?14
ORANGE\tORANGE\tORANGE/BAR\tpays\t?10
CHERRY\tCHERRY\tCHERRY\t\tpays\t?7
CHERRY\tCHERRY\t  -\t\tpays\t?5
CHERRY\t  -\t  -\t\tpays\t?2
7\t  7\t  7\t\tpays\t The Jackpot!
''')
time.sleep(10)
#Constants:
INIT_STAKE = 50
INIT_BALANCE = 1000
ITEMS = ["CHERRY", "LEMON", "ORANGE", "PLUM", "BELL", "BAR", "7"]


firstWheel = None
secondWheel = None
thirdWheel = None
stake = INIT_STAKE
balance = INIT_BALANCE


def play():
    global stake, firstWheel, secondWheel, thirdWheel
    playQuestion = askPlayer()
    while(stake != 0 and playQuestion == True):
        firstWheel = spinWheel()
        secondWheel = spinWheel()
        thirdWheel = spinWheel()
        printScore()
        playQuestion = askPlayer()


def askPlayer():
    '''
    ekitxeba tamashi undatuara kidev ki ari y an yes uaria n an no case sensitive arari
    '''
    global stake
    global balance
    while(True):
        os.system('cls' if os.name == 'nt' else 'clear')
        if (balance <=1):
            print ("Machine balance reset.")
            balance = 1000

        print ("exlandeli jekpoti aris: ?" + str(balance) + ".")
        answer = input("gaagrdzeleb? tu fuls gaanagdeb? ")
        answer = answer.lower()
        if(answer == "yes" or answer == "y"):
            return True
        elif(answer == "no" or answer == "n"):
            print("You ended the game with ?" + str(stake) + " in your hand. Great job!")
            time.sleep(5)
            return False
        elif(answer == "check" or answer == "CHECK"):
            print ("You currently have ?" + str(stake) + ".")
        else:
            print("cota acdi dzamia.")


def spinWheel():
    '''
    gamoaq raime aitemi rendom it
    '''
    randomNumber = random.randint(0, 5)
    return ITEMS[randomNumber]


def printScore():
    '''
    exlandel qulas printavs
    '''
    global stake, firstWheel, secondWheel, thirdWheel, balance
    if((firstWheel == "CHERRY") and (secondWheel != "CHERRY")):
        win = 2
        balance = balance - 2
    elif((firstWheel == "CHERRY") and (secondWheel == "CHERRY") and (thirdWheel != "CHERRY")):
        win = 5
        balance = balance - 5
    elif((firstWheel == "CHERRY") and (secondWheel == "CHERRY") and (thirdWheel == "CHERRY")):
        win = 7
        balance = balance - 7
    elif((firstWheel == "ORANGE") and (secondWheel == "ORANGE") and ((thirdWheel == "ORANGE") or (thirdWheel == "BAR"))):
        win = 10
        balance = balance - 10
    elif((firstWheel == "PLUM") and (secondWheel == "PLUM") and ((thirdWheel == "PLUM") or (thirdWheel == "BAR"))):
        win = 14
        balance = balance - 14
    elif((firstWheel == "BELL") and (secondWheel == "BELL") and ((thirdWheel == "BELL") or (thirdWheel == "BAR"))):
        win = 20
        balance = balance - 20
    
    elif((firstWheel == "BAR") and (secondWheel == "BAR") and (thirdWheel == "BAR")):
        win = 250
        balance = balance - 250
    elif((firstWheel == "7") and (secondWheel == "7") and (thridWheel == "7")):
        win = balance
        balance = balance - win
    else:
        win = -1
        balance = balance + 1


        stake += win
    if win == balance:
        print ("moige da egaxar!!")
    if(win > 0):
        print(firstWheel + '\t' + secondWheel + '\t' + thirdWheel + ' -- You win ?' + str(win))
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print(firstWheel + '\t' + secondWheel + '\t' + thirdWheel + ' -- kide cade')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

play()











