from Board import Board
from Player import Player
from MyBot import MyBot 
import numpy as np

class Game:
    def __init__(self):
        return 
        
    def start(self) -> None:
        return

    def game_loop(self) -> None:
        finished = false 
        while not finished:
            print()
    
#build outer game loop, making several playthroughs possible without restarting programm

#initializing board
while True: 
    try: 
        NumberRows = int(input("Number of Rows: "))        
        break
    except:
        print("Invalid input type. Choose again.")
while True: 
    try: 
        NumberCols = int(input("Number of Columns: "))   
        break
    except:
        print("Invalid input type. Choose again.")
while True: 
    try: 
        NumberKInARow = int(input("Length of Row needed to win (The input needs to be smaller than the row- and the col-number): "))        
        if(NumberCols > NumberKInARow and NumberRows > NumberKInARow):
            break
    except:
        print("Invalid input. Choose again.")

board = Board(NumberRows, NumberCols, NumberKInARow)

#choose player number
while True: 
    try:         
        playerDecision = int(input("How many players are taking part in the game? Choose between 0 and 2: "))
        if(playerDecision == 1 or playerDecision == 2 or playerDecision == 0):
            break
    except:
        print("Your input is out of the expected range!")
#initialzing players
playerList = []
while(int(playerDecision) > 0):
    playerList.append(Player(str(input("please enter a name for player " + str(len(playerList) + 1) + ": " )), (len(playerList) + 1), board))
    playerDecision = int(playerDecision) - 1

while(len(playerList) < 2):
    botName = str(input("please enter a bot name: "))
    while True:
        try:         
            difficultyLevel = int(input("please choose a bot difficulty between 1 and 3: "))
            if(difficultyLevel == 1 or difficultyLevel == 2 or difficultyLevel == 3):
                break
        except:
            print("Your input is out of the expected range!")
    playerList.append(MyBot(botName, (len(playerList) + 1), board, difficultyLevel))
    

#start game loop 
end = False
while not end:
    if(not(isinstance(playerList[0], MyBot) and isinstance(playerList[1], MyBot))):
        while (board.has_won() == 0):
            print("turn: " + playerList[board.getTurn()].name)
            if(isinstance(playerList[board.getTurn()], MyBot)):
                print("bot turn")
                playerList[board.getTurn()].make_move() 
            else:
                print("player turn")
                print("wir sind hier")
                while True:
                    try:
                        row = int(input("Row Number: "))
                        col = int(input("Col Number: "))
                        break
                    except:
                        print("Invalid input type. Choose Again.")
                playerList[board.getTurn()].make_move(row, col) 
            board.display()

        print("The game finished !!!")
        if (board.has_won() == 1): 
            print(playerList[0].name + " has won!")
        elif(board.has_won() == 2):
            print(playerList[1].name + " has won!")
        elif(board.has_won() == -1):
            print("The game is a draw.")
        board.reset()
        if(str(input("do you want to play another round? (yes/ no)")) != "yes"):
            end = True
        

    else:
        while True:
            try:
                rounds = int(input("How many rounds do you want your bots to battle? "))
                break
            except:
                print("Invalid input type. Choose Again.")
        counter = 0
        while (counter < rounds):
            print("Round: " + str(counter + 1) + " ---------------------------------------------------------------------------------------")
            while (board.has_won() == 0):
                playerList[board.getTurn()].make_move() 

            print("The game finished !!!")
            board.display()
            if (board.has_won() == 1): 
                print(playerList[0].name + " has won!")
            elif (board.has_won() == 2):
                print(playerList[1].name + " has won!")
            elif(board.has_won() == -1):
                print("The game is a draw.")
            board.reset()
            counter += 1
        end = True


