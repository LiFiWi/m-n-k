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
            if (self.check_in_danger(board) != None):
                row = self.check_in_danger(board)[0]
                col = self.check_in_danger(board)[1]
            else:
                row = np.random.randint(0, board.nRow)
                col = np.random.randint(0, board.mCol)
        return super().make_move(row, col, board)
        
    def check_in_danger(self,board: Board) -> tuple:
        check_danger = None
        check_danger = self.check_in_danger_horizontal(board)
        if check_danger == None:
            check_danger = self.check_in_danger_vertical(board)
        if check_danger == None:
            check_danger = self.check_in_danger_TLBR(board)
        if check_danger == None:
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
                    if (counter1 == 2):
                        if(board.positionExists(i, (j-1)) and board.positionFree(i, (j-1))):
                            return (i, (j-1))
                        elif (board.positionExists(i, (j+2)) and board.positionFree(i, (j+2))):
                            return (i, (j+2))
                    if (counter1 == 3):
                        if(board.positionExists(i, (j-2)) and board.positionFree(i, (j-2))):
                                return (i, (j-2))
                        elif (board.positionExists(i, (j+2)) and board.positionFree(i, (j+2))):
                            return (i, (j+2)) 
        return None
    
    def check_in_danger_vertical(self, board: Board) -> tuple:
        if self.player_number == 1:
            check_number = 2
        else:
            check_number = 1
        for j in range(board.mCol):
            counter1 = 1   
            for i in range (board.nRow-1):
                if board.field[i, j] == board.field[(i + 1), (j)] == 1:
                    counter1 += 1
                    if (counter1 == 2):
                        if(board.positionExists((i-1), j) and board.positionFree((i-1), j)):
                            return ((i-1), j)
                        elif (board.positionExists((i+2), j) and board.positionFree((i+2), j)):
                            return ((i+2), j)
                    if (counter1 == 3):
                        if(board.positionExists((i-2), j) and board.positionFree((i-2), j)):
                                return ((i-2), j)
                        elif (board.positionExists((i+2), j) and board.positionFree((i+2), j)):
                            return ((i+2), j)
        return None
    
    def check_in_danger_TLBR(self, board: Board) -> tuple:
        if self.player_number == 1:
            check_number = 2
        else:
            check_number = 1
        for i in range((0-board.nRow), (board.nRow -(board.kInARow-1))):
            diagonalArray = np.diagonal(board.field, i)
            counter1 = 1 
            for j in range(len(diagonalArray) - 1): 
                if diagonalArray[j] == diagonalArray[(j + 1)] == 1:
                    counter1 += 1
                    offsetAbsoluteValue = abs(i) + (j-1)
                    return self.make_defending_move_TLBR(counter1, i, offsetAbsoluteValue, j , board)    
        return None
    
    def check_in_danger_BLTR(self, board: Board) -> tuple:
        if self.player_number == 1:
            check_number = 2
        else:
            check_number = 1
        for i in range((0-board.nRow), (board.nRow -(board.kInARow-1))):
            diagonalArray = np.diagonal(board.flippedField, i)
            counter1 = 1 
            for j in range(len(diagonalArray) - 1): 
                if diagonalArray[j] == diagonalArray[(j + 1)] == 1:
                    counter1 += 1
                    offsetAbsoluteValue = abs(i) + (j-1)
                    return self.make_defending_move_BLTR(counter1, i, offsetAbsoluteValue, j, board)
        return None
    
    def fromFlippedToNonFlipped(self, flippedCol: int, board: Board) -> int:
            return (board.mCol - flippedCol)

    def make_defending_move_TLBR(self, counter: int, offset_horizontal: int, offset_absolute: int, offset_vertical: int, board: Board) -> tuple:
        if counter == 2:
            if offset_horizontal >= 0:
                if (board.positionExists((offset_vertical-1), (offset_absolute)) and board.positionFree((offset_vertical-1), (offset_absolute))):
                    return ((offset_vertical-1), (offset_absolute))
                elif (board.positionExists((offset_vertical+2), (offset_absolute+3)) and board.positionFree((offset_vertical+2), (offset_absolute+3))):
                    return ((offset_vertical+2), (offset_absolute+3))
            if offset_horizontal < 0:
                if (board.positionExists((offset_absolute), (offset_vertical-1)) and board.positionFree((offset_absolute), (offset_vertical-1))):
                    return ((offset_absolute), (offset_vertical-1))
                elif (board.positionExists((offset_absolute+3), (offset_vertical+2)) and board.positionFree((offset_absolute+3), (offset_vertical+2))):
                    return ((offset_absolute+3), (offset_vertical+2))
        if counter == 3:
            if offset_horizontal >= 0:
                if (board.positionExists((offset_vertical-2), (offset_absolute-1)) and board.positionFree((offset_vertical-2), (offset_absolute-1))):
                    return ((offset_vertical-2), (offset_absolute-1))
                elif (board.positionExists((offset_vertical+2), (offset_absolute)) and board.positionFree((offset_vertical+2), (offset_absolute+3))):
                    return ((offset_vertical+2), (offset_absolute+3)) 
            if offset_horizontal < 0:
                if (board.positionExists((offset_absolute-1), (offset_vertical-2)) and board.positionFree((offset_absolute-1), (offset_vertical-2))):
                    return ((offset_absolute-1), (offset_vertical-2))
                elif (board.positionExists((offset_absolute+3), (offset_vertical+2)) and board.positionFree((offset_absolute+3), (offset_vertical+2))):
                    return ((offset_absolute+3), (offset_vertical+2))
        return None
    
    def make_defending_move_BLTR(self, counter: int, offset_horizontal: int, offset_absolute: int, offset_vertical: int, board: Board) -> tuple:
        if counter == 2:
            if offset_horizontal >= 0:
                if board.position_valid((offset_vertical-1), (self.fromFlippedToNonFlipped(offset_absolute, board)-1)):
                    return ((offset_vertical-1), (self.fromFlippedToNonFlipped(offset_absolute, board)-1))
                elif board.position_valid((offset_vertical+2), (self.fromFlippedToNonFlipped((offset_absolute+3), board)-1)):
                    return ((offset_vertical+2), (self.fromFlippedToNonFlipped((offset_absolute+3), board)-1))
            if offset_horizontal < 0:
                if board.position_valid((offset_absolute), (self.fromFlippedToNonFlipped((offset_vertical-1), board)-1)):
                    return ((offset_absolute), (self.fromFlippedToNonFlipped((offset_vertical-1), board)-1))
                elif board.position_valid((offset_absolute+3), (self.fromFlippedToNonFlipped((offset_vertical+2), board)-1)):
                    return ((offset_absolute+3), (self.fromFlippedToNonFlipped((offset_vertical+2), board)-1))
        if counter == 3:
            if offset_horizontal >= 0:
                if board.position_valid((offset_vertical-2), (self.fromFlippedToNonFlipped((offset_absolute-1), board)-1)):
                    return ((offset_vertical-2), (self.fromFlippedToNonFlipped((offset_absolute-1), board)-1))
                elif board.position_valid((offset_vertical+2), self.fromFlippedToNonFlipped((offset_absolute+4), board)):
                    return ((offset_vertical+2), self.fromFlippedToNonFlipped((offset_absolute+4), board)) 
            if offset_horizontal < 0:
                if  board.position_valid((self.fromFlippedToNonFlipped((offset_vertical-2), board)-1), (offset_absolute-1)):
                    return ((self.fromFlippedToNonFlipped((offset_vertical-2), board)-1), (offset_absolute-1))
                elif board.position_valid((offset_absolute+3), self.fromFlippedToNonFlipped((offset_vertical+2), board)):
                    return ((offset_absolute+3), self.fromFlippedToNonFlipped((offset_vertical+2), board))
    
    '''
    Bot Methoden: 
    Check if in danger: checks if enemy has row of k-2
    Check if can finish: checks if self can finish a row to k 
    Muster erkennen(Reihe eigene)
    Zwickmühle bauen
    '''