from Player import Player
from Board import Board
import numpy as np

class MyBot(Player):    
    def __init__(self, name: str, player_number: int, board: Board ) -> None:
        '''
        This is the constructor for the class Player. It sets its name, player_number and Board.

                Parameters:
                        name(string): player's name
                        player_name(int): player's number
                        board(Board): Board where Player is active
        '''
        self.player_number = player_number
        self.name = name
        self.board = board
    
    def make_move(self, board: Board) -> tuple:
        row = np.random.randint(1,Board.nRow)
        col = np.random.randint(Board.mCol)
        print(row)
        print(col)
        if board.positionExists(row, col) and board.positionFree(row, col):          
            print("made a move")
            board.field[row, col] = self.player_number
        else:
            self.make_move(board)
            return(row, col)
