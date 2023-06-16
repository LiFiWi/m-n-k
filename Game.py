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

#initialzing players
playerDecision = int(input("How many players are taking part in the game? Choose between two and zero: "))
while((playerDecision != 1 or playerDecision != 2 or playerDecision != 0) and not isinstance(playerDecision, int)): 
    playerDecision = input("Your input is out of the expected range! Please enter a number between 0 and 2: ")
playerList = []
while(int(playerDecision) > 0):
    playerList.append(Player(str(input("please enter a name for player " + str(len(playerList) + 1) + ": " )), (len(playerList) + 1), board))
    playerDecision = int(playerDecision) - 1

while(len(playerList) < 2):
    playerList.append(MyBot(str(input("please enter a bot name: ")), (len(playerList) + 1), board))
    #please choose a bot difficulty between x and x

#start game loop 
if(not(isinstance(playerList[0], MyBot) and isinstance(playerList[0], MyBot))):
    while (board.has_won() == 0):
        if(isinstance(playerList[board.getTurn()], Player)):
            row = int(input("Row Number: "))
            col = int(input("Col Number: "))
            playerList[board.getTurn()].make_move(row, col) 
            board.display()
        elif(isinstance(playerList[board.getTurn()], MyBot)):
            playerList[board.getTurn()].make_move() 
else:
    #rounds = int(input("How many rounds do you want your bots to battle? "))
    rounds = 2
    counter = 0
    while (counter < rounds):
        print("zähler: " + str(counter) + " ---------------------------------------------------------------------------------------")
        while (board.has_won() == 0):
            playerList[board.getTurn()].make_move() 
            board.display()
        
        print("Das Spiel wurde beendet!!!")
        if (board.has_won() == 1): 
            print(playerList[0].name + " gewinnt")
        elif (board.has_won() == 2):
            print(playerList[1].name + " gewinnt")
        else:
            print("leider unentschieden.")
        board.reset()
        counter += 1


#print(board.has_won())
