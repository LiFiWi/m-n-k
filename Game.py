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
    

NumberRows = int(input("Number of Rows: "))
NumberCols = int(input("Number of Columns: "))
NumberKInARow = int(input("Length of Row needed to win: "))
b = Board(NumberRows, NumberCols, NumberKInARow)
player1name = str(input("Name von Spieler 1: "))
player2name = str(input("Name von Spieler 2: "))
'''if(player2name=="Bot"):'''
p1 = Player(player1name, 1, b)
p2 = MyBot(player2name, 2, b)
'''else:
    p1 = Player(player1name, 1, b)
    p2 = Player(player2name, 2, b)'''
player = [p1, p2]
counter = 0


while (b.has_won() == 0):
    #print(counter)
    row = int(input("Row Number: "))
    col = int(input("Col Number: "))
    if player[counter].make_move(row, col, b) == (row, col):
        counter += 1
        counter = counter % 2
    p2.make_move(b)
    b.display()
print(b.has_won())
print("Das Spiel wurde beendet!!!")
if (b.has_won() == 1): 
    print(player1name + " gewinnt")
elif (b.has_won() == 2):
    print(player2name + " gewinnt")
else:
    print("leider unentschieden.")