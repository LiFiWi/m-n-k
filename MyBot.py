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
    
    def make_move(self, board: Board) -> tuple:
        if  self.difficulty_level == 1:
            row = np.random.randint(0, board.n_row)
            col = np.random.randint(0, board.m_col)
        #print(row)
        #print(col)
        if self.difficulty_level == 2:
            if (self.check_in_danger(board) != None):
                row = self.check_in_danger(board)[0]
                col = self.check_in_danger(board)[1]
            else:
                row = np.random.randint(0, board.n_row)
                col = np.random.randint(0, board.m_col)
        return super().make_move(row, col, board)
        
    def check_in_danger(self, board: Board) -> tuple:
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
        for i in range(board.n_row):
            counter1 = 1   
            for j in range (board.m_col - 1):
                if board.field[i,j] == board.field[i, (j + 1)] == check_number:
                    counter1 += 1
                    if (counter1 == 2):
                        if(board.position_exists(i, (j - 1)) and board.position_free(i, (j - 1))):
                            return (i, (j-1))
                        elif (board.position_exists(i, (j + 2)) and board.position_free(i, (j + 2))):
                            return (i, (j + 2))
                    if (counter1 == 3):
                        if(board.position_exists(i, (j - 2)) and board.position_free(i, (j - 2))):
                                return (i, (j - 2))
                        elif (board.position_exists(i, (j + 2)) and board.position_free(i, (j + 2))):
                            return (i, (j + 2)) 
        return None
    
    def check_in_danger_vertical(self, board: Board) -> tuple:
        if self.player_number == 1:
            check_number = 2
        else:
            check_number = 1
        for j in range(board.m_col):
            counter1 = 1   
            for i in range (board.n_row-1):
                if board.field[i, j] == board.field[(i + 1), (j)] == 1:
                    counter1 += 1
                    if (counter1 == 2):
                        if(board.position_exists((i - 1), j) and board.position_free((i - 1), j)):
                            return ((i - 1), j)
                        elif (board.position_exists((i + 2), j) and board.position_free((i + 2), j)):
                            return ((i + 2), j)
                    if (counter1 == 3):
                        if(board.position_exists((i - 2), j) and board.position_free((i - 2), j)):
                                return ((i - 2), j)
                        elif (board.position_exists((i + 2), j) and board.position_free((i + 2), j)):
                            return ((i + 2), j)
        return None
    
    def check_in_danger_TLBR(self, board: Board) -> tuple:
        if self.player_number == 1:
            check_number = 2
        else:
            check_number = 1
        for offset_horizontal in range((0 - board.n_row), (board.n_row - (board.k_in_a_row - 1))):
            diagonal_array = np.diagonal(board.field, offset_horizontal)
            counter1 = 1 
            for offset_vertical in range(len(diagonal_array) - 1): 
                if diagonal_array[offset_vertical] == diagonal_array[(offset_vertical + 1)] == check_number:
                    counter1 += 1
                    offset_absolute_value = abs(offset_horizontal) + (offset_vertical - 1)
                    if self.make_defending_move_TLBR(counter1, offset_horizontal, offset_absolute_value, offset_vertical, board) != None:
                        return self.make_defending_move_TLBR(counter1, offset_horizontal, offset_absolute_value, offset_vertical, board) #returned nur einmal    
        return None
    
    def check_in_danger_BLTR(self, board: Board) -> tuple:
        if self.player_number == 1:
            check_number = 2
        else:
            check_number = 1
        for offset_horizontal in range((0-board.n_row), (board.n_row -(board.k_in_a_row-1))):
            diagonal_array = np.diagonal(board.flipped_field, offset_horizontal)
            counter1 = 1 
            for offset_vertical in range(len(diagonal_array) - 1): 
                if diagonal_array[offset_vertical] == diagonal_array[(offset_vertical + 1)] == 1:
                    counter1 += 1
                    offset_absolute_value = abs(offset_horizontal) + (offset_vertical - 1)
                    if self.make_defending_move_BLTR(counter1, offset_horizontal, offset_absolute_value, offset_vertical, board) != None:
                        return self.make_defending_move_BLTR(counter1, offset_horizontal, offset_absolute_value, offset_vertical, board)
        return None
    
    def from_flipped_to_non_flipped(self, flipped_col: int, board: Board) -> int:
            return (board.m_col - flipped_col)

    def make_defending_move_TLBR(self, counter: int, offset_horizontal: int, offset_absolute: int, offset_vertical: int, board: Board) -> tuple:
        if counter == 2 and self.make_move_TLBR_2(offset_horizontal, offset_absolute, offset_vertical, board) != None:
            return self.make_move_TLBR_2(offset_horizontal, offset_absolute, offset_vertical, board)
        if counter == 3 and self.make_move_TLBR_3(offset_horizontal, offset_absolute, offset_vertical, board) != None:
            return self.make_move_TLBR_3(offset_horizontal, offset_absolute, offset_vertical, board)
        return None
    
    def make_defending_move_BLTR(self, counter: int, offset_horizontal: int, offset_absolute: int, offset_vertical: int, board: Board) -> tuple:
        if counter == 2 and self.make_move_BLTR_2(offset_horizontal, offset_absolute, offset_vertical, board) != None:
            return self.make_move_BLTR_2(offset_horizontal, offset_absolute, offset_vertical, board)
        if counter == 3 and self.make_move_BLTR_3(offset_horizontal, offset_absolute, offset_vertical, board) != None:
            return self.make_move_BLTR_3(offset_horizontal, offset_absolute, offset_vertical, board)

    def make_move_TLBR_2(self, offset_horizontal: int, offset_absolute: int, offset_vertical: int, board: Board) -> tuple:
        if offset_horizontal >= 0:
            print(offset_vertical-1)
            print(offset_absolute)
            if board.position_valid((offset_vertical-1), (offset_absolute)):
                print(offset_vertical-1)
                print(offset_absolute)
                return ((offset_vertical-1), (offset_absolute))
            elif board.position_valid((offset_vertical+2), (offset_absolute+3)):
                return ((offset_vertical+2), (offset_absolute+3))#funktioniert
        if offset_horizontal < 0:
            if board.position_valid((offset_absolute), (offset_vertical-1)):
                return ((offset_absolute), (offset_vertical-1))
            elif board.position_valid((offset_absolute+3), (offset_vertical+2)):
                return ((offset_absolute+3), (offset_vertical+2))

    def make_move_BLTR_2(self, offset_horizontal: int, offset_absolute: int, offset_vertical: int, board: Board) -> tuple:
        if offset_horizontal >= 0:
            if board.position_valid((offset_vertical-1), (self.from_flipped_to_non_flipped(offset_absolute, board)-1)):
                return ((offset_vertical-1), (self.from_flipped_to_non_flipped(offset_absolute, board)-1)) #funktioniert
            elif board.position_valid((offset_vertical+2), (self.from_flipped_to_non_flipped((offset_absolute+3), board)-1)):
                return ((offset_vertical+2), (self.from_flipped_to_non_flipped((offset_absolute+3), board)-1)) #funktioniert
        if offset_horizontal < 0:
            if board.position_valid((offset_absolute), (self.from_flipped_to_non_flipped((offset_vertical-1), board)-1)):
                return ((offset_absolute), (self.from_flipped_to_non_flipped((offset_vertical-1), board)-1))
            elif board.position_valid((offset_absolute+3), (self.from_flipped_to_non_flipped((offset_vertical+2), board)-1)):
                return ((offset_absolute+3), (self.from_flipped_to_non_flipped((offset_vertical+2), board)-1))

    def make_move_TLBR_3(self, offset_horizontal: int, offset_absolute: int, offset_vertical: int, board: Board) -> tuple:
        if offset_horizontal >= 0:
            if board.position_valid((offset_vertical-2), (offset_absolute-1)):
                return ((offset_vertical-2), (offset_absolute-1))
            elif board.position_valid((offset_vertical+2), (offset_absolute+3)):
                return ((offset_vertical+2), (offset_absolute+3)) 
        if offset_horizontal < 0:
            if board.position_valid((offset_absolute-1), (offset_vertical-2)):
                return ((offset_absolute-1), (offset_vertical-2))
            elif board.position_valid((offset_absolute+3), (offset_vertical+2)):
                return ((offset_absolute+3), (offset_vertical+2))

    def make_move_BLTR_3(self, offset_horizontal: int, offset_absolute: int, offset_vertical: int, board: Board) -> tuple:
        if offset_horizontal >= 0:
            if board.position_valid((offset_vertical-2), (self.from_flipped_to_non_flipped((offset_absolute-1), board)-1)):
                return ((offset_vertical-2), (self.from_flipped_to_non_flipped((offset_absolute-1), board)-1))
            elif board.position_valid((offset_vertical+2), self.from_flipped_to_non_flipped((offset_absolute+4), board)):
                return ((offset_vertical+2), self.from_flipped_to_non_flipped((offset_absolute+4), board)) 
        if offset_horizontal < 0:
            if  board.position_valid((self.from_flipped_to_non_flipped((offset_vertical-2), board)-1), (offset_absolute-1)):
                return ((self.from_flipped_to_non_flipped((offset_vertical-2), board)-1), (offset_absolute-1))
            elif board.position_valid((offset_absolute+3), self.from_flipped_to_non_flipped((offset_vertical+2), board)):
                return ((offset_absolute+3), self.from_flipped_to_non_flipped((offset_vertical+2), board))
    
    
    def finish_game(self, board: Board) -> tuple:
        check_winning = None
        check_winning = self.check_winning_horizontal(board)
        if check_winning == None:
            check_winning = self.check_winning_vertical(board)
        if check_winning == None:
            check_winning = self.check_winning_TLBR(board)
        if check_winning == None:
            check_winning = self.check_winning_BLTR(board)
        return check_winning
    
    '''
    Bot Methoden: 
    Check if in danger: checks if enemy has row of k-2
    Check if can finish: checks if self can finish a row to k 
    Muster erkennen(Reihe eigene)
    Zwickmühle bauen
    '''