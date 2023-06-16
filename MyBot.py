from Player import Player
from Board import Board
import numpy as np

class MyBot(Player):    
    def __init__(self, name: str, player_number: int, board: Board ) -> None:
        '''
        This is the constructor for the class Player. It sets its name, player_number and Board.

                Parameters:
                        name(str): player's name
                        player_name(int): player's number
                        board(Board): Board where Player is active
        '''
        super().__init__(name, player_number, board)
    
    def make_move(self) -> tuple:
        row = np.random.randint(0, self.board.nRow)
        col = np.random.randint(0, self.board.mCol)
        print(row)
        print(col)
        return super().make_move(row, col, self.board)
        


board = Board()
bot1 = MyBot("b1", 1, board)
bot2 = MyBot("b2", 2, board)
bot = [bot1, bot2]


while(board.has_won() == 0):
    bot1.make_move()
    bot2.make_move()
    board.display()
if (board.has_won() == 1): 
    print(bot2.name + " gewinnt")
elif (board.has_won() == 2):
    print(bot1.name + " gewinnt")
else:
    print("leider unentschieden.")