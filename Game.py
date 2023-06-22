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
NumberRows = 5 #int(input("Number of Rows: "))
NumberCols = 5 #int(input("Number of Columns: "))
NumberKInARow = 4 #int(input("Length of Row needed to win: "))
board = Board(NumberRows, NumberCols, NumberKInARow)

#choose player number
while True: 
    try:         
        playerDecision = int(input("How many players are taking part in the game? Choose between two and zero: "))
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
    difficultyLevel = int(input("please choose a bot difficulty between 1 and 3: "))
    while difficultyLevel != 1:
        difficultyLevel = int(input("please choose againg: "))
    playerList.append(MyBot(botName, (len(playerList) + 1), board, difficultyLevel))
    

#start game loop 
end = False
while not end:
    if(not(isinstance(playerList[0], MyBot) and isinstance(playerList[1], MyBot))):
        while (board.has_won() == 0):
            print("turn: " + str(board.getTurn()))
            if(isinstance(playerList[board.getTurn()], MyBot)):
                print("bot turn")
                playerList[board.getTurn()].make_move() 
            else:
                print("player turn")
                print("wir sind hier")
                row = int(input("Row Number: "))
                col = int(input("Col Number: "))
                playerList[board.getTurn()].make_move(row, col) 
            board.display()

        print("Das Spiel wurde beendet!!!")
        if (board.has_won() == 1): 
            print(playerList[0].name + " gewinnt")
        elif (board.has_won() == 2):
            print(playerList[1].name + " gewinnt")
        else:
            print("leider unentschieden.")
        board.reset()
        if(str(input("do you want to play another round? (yes/ no)")) != "yes"):
            end = True
        

    else:
        rounds = int(input("How many rounds do you want your bots to battle? "))
        counter = 0
        while (counter < rounds):
            print("zähler: " + str(counter) + " ---------------------------------------------------------------------------------------")
            while (board.has_won() == 0):
                playerList[board.getTurn()].make_move() 
                #board.display()
            
            print("Das Spiel wurde beendet!!!")
            board.display()
            if (board.has_won() == 1): 
                print(playerList[0].name + " gewinnt")
            elif (board.has_won() == 2):
                print(playerList[1].name + " gewinnt")
            else:
                print("leider unentschieden.")
            board.reset()
            counter += 1
        end = True


