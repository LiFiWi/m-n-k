from Player import Player
from Board import Board
import numpy as np

class MyBot(Player):    
    def __init__(self, name: str, player_number: int, board: Board, level: int) -> None:
        '''
        This is the constructor for the class Player. It sets its name, player_number and Board.

                Parameters:
                        name(str): player's name
                        player_name(int): player's number
                        board(Board): Board where Player is active
                        level(int): difficulty level, deciding about the tactics used by the bot 
        '''
        super().__init__(name, player_number, board)
        self.difficulty_level = level
    
    def make_move(self) -> tuple:
        if self.difficulty_level == 1:
            row = np.random.randint(0, self.board.nRow)
            col = np.random.randint(0, self.board.mCol)
        #print(row)
        #print(col)
        return super().make_move(row, col)
        
