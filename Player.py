from board import Board
import numpy as np

class Player:
    def __init__(self, name: str, player_number: int, board: Board ) -> None:
        self.player_number = player_number
        self.name = name
        self.board = board

    def make_move(self, row: int, col: int, board:Board) -> tuple:
        if board.positionExists(row, col) and board.positionFree(row, col):          
            board.field[row, col] = self.player_number
            return(row, col)

#board: Board 
b = Board(1)
p = Player("name", 1, b)
print(p.name)
print(p.player_number)
b.display()

p.make_move(0, 0, b)
b.display()