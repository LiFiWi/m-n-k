from Board import Board
import numpy as np

class Player:
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

    def make_move(self, row: int, col: int) -> tuple:
        '''
        Returns if existing and free the field. Sets the field to the given player_number.

                Parameters:
                        self: player
                        row(int): field's row
                        col(int): field's column
                        

                Returns:
                        tuple: field coordinates
        '''
        if self.board.positionExists(row, col) and self.board.positionFree(row, col):          
            #print("made a move")
            self.board.field[row, col] = self.player_number
            self.board.take_turn()
        else:
            #print("move failed")
            a = 1 + 1
        return(row, col)


    
    def toString(self) -> str:
        """Returns name and the number of a player as a string."""
        return("Name: " + self.name + '\n' + "Player Number: " + str(self.player_number))