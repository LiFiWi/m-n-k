from Board import Board
import numpy as np

class Player:
    def __init__(self, name: str, player_number: int, board: Board ) -> None:
        self.player_number = player_number
        self.name = name
        self.board = board

    def make_move(self, row: int, col: int, board:Board) -> tuple:
        if board.positionExists(row, col) and board.positionFree(row, col):          
            print("made a move")
            board.field[row, col] = self.player_number
            return(row, col)


    
    def toString(self) -> str:
        return("Name: " + self.name + '\n' + "Player Number: " + str(self.player_number))#
#b = Board(5, 5)
#p1 = Player("name", 1, b)
#p2 = Player("name", 2, b)
#print(p1.name)
#print(p1.player_number)
#b.display()
#
#p1.make_move(4, 0, b)
#b.display()
#p2.make_move(3, 0, b)
#b.display()
#print(p1.make_move(4, 2, b)) # returns tuple 
##b.display()