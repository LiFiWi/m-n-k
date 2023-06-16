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
player = [Player("p1", 1, b), Player("p2", 2, b)]


while (b.has_won() == 0):
    #print(counter)
    row = int(input("Row Number: "))
    col = int(input("Col Number: "))
    player[b.getTurn()].make_move(row, col) 
    b.display()

print(b.has_won())
print("Das Spiel wurde beendet!!!")
if (b.has_won() == 1): 
    print(player1name + " gewinnt")
elif (b.has_won() == 2):
    print(player2name + " gewinnt")
else:
    print("leider unentschieden.")