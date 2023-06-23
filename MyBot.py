from Player import Player
from Board import Board
import numpy as np

class MyBot(Player):    

    difficulty_level = 0

    def __init__(self, name: str, player_number: int, level: int) -> None:
        '''
        This is the constructor for the class Player. It sets its name, player_number and Board.

                Parameters:
                        name(str): player's name
                        player_name(int): player's number
                        board(Board): Board where Player is active
                        level(int): difficulty level, deciding about the tactics used by the bot 
        '''
        super().__init__(name, player_number)
        self.difficulty_level = level
        print(self.difficulty_level)
    
    def make_move(self, board: Board) -> tuple:
        if  self.difficulty_level == 1:
            row = np.random.randint(0, board.nRow)
            col = np.random.randint(0, board.mCol)
        #print(row)
        #print(col)
        if self.difficulty_level == 2:

            return super().make_move(row, col, board)
        
    def check_in_danger(self,board: Board) -> tuple:
        check_danger = None
        check_danger = self.check_in_danger_horizontal(board)
        if check_danger == None:
            check_danger = self.check_in_danger_vertical(board)
        elif check_danger == None:
            check_danger = self.check_in_danger_TLBR(board)
        elif check_danger == None:
            check_danger = self.check_in_danger_BLTR(board)
        return check_danger
            
        
    
    def check_in_danger_horizontal(self, board: Board) -> tuple:
        if self.player_number == 1:
            check_number = 2
        else:
            check_number = 1
        for i in range(board.nRow):
            counter1 = 1   
            for j in range (board.mCol - 1):
                if board.field[i,j] == board.field[i, (j + 1)] == check_number:
                    counter1 += 1
                    if (counter1 == (board.kInARow-2)):
                        return (i, (j+2)) 
        return None
    
    def check_in_danger_vertical(self, board: Board) -> int:
        if self.player_number == 1:
            check_number = 2
        else:
            check_number = 1
        for i in range(board.mCol):
            counter1 = 1   
            for j in range (self.nRow-1):
                if self.field[j, i] == self.field[(j + 1), (i)] == 1:
                    counter1 += 1
                    if (counter1 == self.kInARow):
                        numberVertical = 1
                elif self.field[j, i] == self.field[(j+1), (i)] == 2:
                    counter2 += 1
                    if (counter2 == self.kInARow):
                        numberVertical = 2
        return numberVertical
    '''
    Bot Methoden: 
    Check if in danger: checks if enemy has row of k-2
    Check if can finish: checks if self can finish a row to k 
    Muster erkennen(Reihe eigene)
    Zwickmühle bauen
    '''
    #def check_in_danger(self) -> tuple: