from Board import Board
from Player import Player
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
    

b = Board()
p1 = Player("t1", 1, b)
p2 = Player("t2", 2, b)
player = [p1, p2]
counter = 1

while (b.has_won()==0):
    #print(counter)
    row = int(input("Row Number: "))
    col = int(input("Col Number: "))
    if player[counter].make_move(row, col, b) == (row, col):
        counter += 1
        counter = counter % 2
    
    b.display()
print("Das Spiel wurde beendet!!!")    

