from Player import Player
from Board import Board
import numpy as np

class MyBot(Player):    

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
        '''
        Chooses a field varying by selected difficulty. Difficulty 1 is the random Bot. Difficulty 2 is the defensive Bot. Difficulty 3 is the offensive Bot. 
        Returns if existing and free the field. Sets the field to the given player_number.

                Parameters:
                        self: bot
                        board: Board where Player is active
                        

                Returns:
                        tuple: field coordinates
        '''
        if  self.difficulty_level == 1:
            row = np.random.randint(0, board.n_row)
            col = np.random.randint(0, board.m_col)
        if self.difficulty_level == 2:
            if (self.check_in_danger(board) != None):
                row = self.check_in_danger(board)[0]
                col = self.check_in_danger(board)[1]
            elif (self.finish_game(board) != None):
                row = self.finish_game(board)[0]
                col = self.finish_game(board)[1]
            else:
                row = np.random.randint(0, board.n_row)
                col = np.random.randint(0, board.m_col)
        if self.difficulty_level == 3:
            if not (np.any(board.field)):
                row = round((board.n_row-1)/2)
                col = round((board.m_col-1)/2)
            elif (self.finish_game(board) != None):
                row = self.finish_game(board)[0]
                col = self.finish_game(board)[1]
            elif (self.check_in_danger(board) != None):
                row = self.check_in_danger(board)[0]
                col = self.check_in_danger(board)[1]
            elif (self.start_attack(board) != None):
                row = self.start_attack(board)[0]
                col = self.start_attack(board)[1]
            else:
                row = np.random.randint(0, board.n_row)
                col = np.random.randint(0, board.m_col)
        return super().make_move(row, col, board)
        
    def check_in_danger(self, board: Board) -> tuple:
        '''
        Checks if bot is in danger of being defeated. If thats the case he tries to stop the threatening row.

                Parameters:
                        self: bot
                        board: Board where Player is active
                        

                Returns:
                        tuple: field coordinates
        '''
        if self.player_number == 1:
            check_number = 2
        else:
            check_number = 1
        check_danger = None
        check_danger = self.check_in_danger_horizontal(board, check_number)
        if check_danger == None:
            check_danger = self.check_in_danger_vertical(board, check_number)
        if check_danger == None:
            check_danger = self.check_in_danger_TLBR(board, check_number)
        if check_danger == None:
            check_danger = self.check_in_danger_BLTR(board, check_number)
        return check_danger

    def check_in_danger_horizontal(self, board: Board, check_number: int) -> tuple:
        '''
        Checks if bot is in danger of being defeated horizontally. If thats the case he tries to stop the threatening row.

                Parameters:
                        self: bot
                        board: Board where Player is active
                        check_number: playernumber of the opponent 

                Returns:
                        tuple: field coordinates
        '''
        for offset_horizontal in range(board.n_row):
            counter1 = 1   
            for offset_vertical in range (board.m_col - 1):
                if board.field[offset_horizontal,offset_vertical] != board.field[offset_horizontal, (offset_vertical + 1)]:
                    counter1 =1
                if board.field[offset_horizontal,offset_vertical] == board.field[offset_horizontal, (offset_vertical + 1)] == check_number:
                    counter1 += 1
                    for i in range (2, board.k_in_a_row):
                        if (counter1 == i):
                            if(board.position_valid(offset_horizontal, (offset_vertical - (i - 1)))):
                                return (offset_horizontal, (offset_vertical - (i - 1)))
                            elif (board.position_valid(offset_horizontal, (offset_vertical + 2))):
                                return (offset_horizontal, (offset_vertical + 2))
        return None
    
    def check_in_danger_vertical(self, board: Board, check_number: int) -> tuple:
        '''
        Checks if bot is in danger of being defeated vertically. If thats the case he tries to stop the threatening row.

                Parameters:
                        self: bot
                        board: Board where Player is active
                        check_number: playernumber of the opponent 

                Returns:
                        tuple: field coordinates
        '''
        for offset_vertical in range(board.m_col):
            counter1 = 1   
            for offset_horizontal in range (board.n_row-1):
                if board.field[offset_horizontal, offset_vertical] != board.field[(offset_horizontal + 1), (offset_vertical)]:
                    counter1 = 1
                if board.field[offset_horizontal, offset_vertical] == board.field[(offset_horizontal + 1), (offset_vertical)] == check_number:
                    counter1 += 1
                    for i in range (2, board.k_in_a_row):
                        if (counter1 == i):
                            if(board.position_valid((offset_horizontal - (i - 1)), offset_vertical)):
                                return ((offset_horizontal - (i - 1)), offset_vertical)
                            elif (board.position_valid((offset_horizontal + 2), offset_vertical)):
                                return ((offset_horizontal + 2), offset_vertical)
        return None
    
    def check_in_danger_TLBR(self, board: Board, check_number: int) -> tuple:
        '''
        Checks if bot is in danger of being defeated diagonally (top left to bottom right). If thats the case he tries to stop the threatening row.

                Parameters:
                        self: bot
                        board: Board where Player is active
                        check_number: playernumber of the opponent 

                Returns:
                        tuple: field coordinates
        '''
        for offset_horizontal in range((0 - board.n_row), (board.n_row - (board.k_in_a_row - 1))):
            diagonal_array = np.diagonal(board.field, offset_horizontal)
            counter1 = 1 
            for offset_vertical in range(len(diagonal_array) - 1): 
                if diagonal_array[offset_vertical] != diagonal_array[(offset_vertical + 1)]:
                    counter1 = 1
                if diagonal_array[offset_vertical] == diagonal_array[(offset_vertical + 1)] == check_number:
                    counter1 += 1
                    offset_absolute_value = abs(offset_horizontal) + (offset_vertical -1)
                    for i in range (2, board.k_in_a_row): 
                        if self.make_defending_move_TLBR(counter1, offset_horizontal, offset_absolute_value, offset_vertical, board, i) != None:
                            return self.make_defending_move_TLBR(counter1, offset_horizontal, offset_absolute_value, offset_vertical, board, i)  
        return None
    
    def check_in_danger_BLTR(self, board: Board, check_number: int) -> tuple:
        '''
        Checks if bot is in danger of being defeated diagonally (bottom left to top right). If thats the case he tries to stop the threatening row.

                Parameters:
                        self: bot
                        board: Board where Player is active
                        check_number: playernumber of the opponent 

                Returns:
                        tuple: field coordinates
        '''
        for offset_horizontal in range((0-board.n_row), (board.n_row -(board.k_in_a_row-1))):
            diagonal_array = np.diagonal(board.flipped_field, offset_horizontal)
            counter1 = 1 
            for offset_vertical in range(len(diagonal_array) - 1): 
                if diagonal_array[offset_vertical] != diagonal_array[(offset_vertical + 1)]:
                    counter1 = 1
                if diagonal_array[offset_vertical] == diagonal_array[(offset_vertical + 1)] == check_number:
                    counter1 += 1
                    offset_absolute_value = abs(offset_horizontal) + (offset_vertical -1)
                    for i in range (2, board.k_in_a_row): 
                        if self.make_defending_move_BLTR(counter1, offset_horizontal, offset_absolute_value, offset_vertical, board, i) != None:
                            return self.make_defending_move_BLTR(counter1, offset_horizontal, offset_absolute_value, offset_vertical, board, i)
        return None
    
    def from_flipped_to_non_flipped(self, flipped_col: int, board: Board) -> int:
        '''
            Calculates the matching field of the flipped field for the normal field.
                Parameters:
                        self: bot
                        board: Board where Player is active
                        check_number: playernumber of the opponent 

                Returns:
                        tuple: field coordinates
        '''
        return (board.m_col - flipped_col)

    def make_defending_move_TLBR(self, counter: int, offset_horizontal: int, offset_absolute: int, offset_vertical: int, board: Board, length: int) -> tuple:
        '''
            Checks if given lenght of opponent row is reached (top left to bottom right). If thats the case he tries to stop the threatening row.
                Parameters:
                        self: bot
                        counter: Lenght of the opposing row
                        offset_horizontal: horizontal offset 
                        offset_absolute: absolute value of the horizontal offset 
                        offset_vertical: vertical 
                        board: Board where Player is active
                        length: Length row needs to reach

                Returns:
                        tuple: field coordinates
        '''
        if counter == length and self.make_move_TLBR(offset_horizontal, offset_absolute, offset_vertical, board, length) != None:
            return self.make_move_TLBR(offset_horizontal, offset_absolute, offset_vertical, board, length)
        return None
    
    def make_defending_move_BLTR(self, counter: int, offset_horizontal: int, offset_absolute: int, offset_vertical: int, board: Board, length: int) -> tuple:
        '''
            Checks if given lenght of opponent row is reached (bottom left to top right). If thats the case he tries to stop the threatening row.
                Parameters:
                        self: bot
                        counter: Lenght of the opposing row
                        offset_horizontal: horizontal offset 
                        offset_absolute: absolute value of the horizontal offset 
                        offset_vertical: vertical offset
                        board: Board where Player is active
                        length: Length row needs to reach

                Returns:
                        tuple: field coordinates
        '''
        if counter == length and self.make_move_BLTR(offset_horizontal, offset_absolute, offset_vertical, board, length) != None:
            return self.make_move_BLTR(offset_horizontal, offset_absolute, offset_vertical, board, length)
            
    def make_move_TLBR(self, offset_horizontal: int, offset_absolute: int, offset_vertical: int, board: Board, length: int) -> tuple:
        '''
            Calculates field where to make own move.
            (top left to bottom right)
                Parameters:
                        self: bot
                        offset_horizontal: horizontal offset 
                        offset_absolute: absolute value of the horizontal offset 
                        offset_vertical: vertical offset
                        board: Board where Player is active
                        length: Length row needs to reach

                Returns:
                        tuple: field coordinates
        '''
        if offset_horizontal >= 0:
            if board.position_valid((offset_vertical+(1-length)), (offset_absolute-(length-2))):
                return ((offset_vertical+(1-length)), (offset_absolute-(length-2)))
            elif board.position_valid((offset_vertical+2), (offset_absolute+3)):
                return ((offset_vertical+2), (offset_absolute+3))
        if offset_horizontal < 0:
            if board.position_valid((offset_absolute-(length-2)), (offset_vertical+(1-length))):
                return ((offset_absolute-(length-2)), (offset_vertical+(1-length)))
            elif board.position_valid((offset_absolute+3), (offset_vertical+2)):
                return ((offset_absolute+3), (offset_vertical+2))  
            
    def make_move_BLTR(self, offset_horizontal: int, offset_absolute: int, offset_vertical: int, board: Board, length: int) -> tuple:
        '''
            Calculates field where to make own move.
            (bottom left to top right)
                Parameters:
                        self: bot
                        offset_horizontal: horizontal offset 
                        offset_absolute: absolute value of the horizontal offset 
                        offset_vertical: vertical offset
                        board: Board where Player is active
                        length: Length row needs to reach

                Returns:
                        tuple: field coordinates
        '''
        if offset_horizontal >= 0:
            if board.position_valid((offset_vertical+(1-length)), (self.from_flipped_to_non_flipped(offset_absolute-(length-2), board)-1)):
                return ((offset_vertical+(1-length)), (self.from_flipped_to_non_flipped(offset_absolute-(length-2), board)-1))
            elif board.position_valid((offset_vertical+2), (self.from_flipped_to_non_flipped(offset_absolute+3, board)-1)):
                return ((offset_vertical+2), (self.from_flipped_to_non_flipped(offset_absolute+3, board)-1))
        if offset_horizontal < 0:
            if board.position_valid((offset_absolute-(length-2)), (self.from_flipped_to_non_flipped(offset_vertical+(1-length), board)-1)):
                return ((offset_absolute-(length-2)), (self.from_flipped_to_non_flipped(offset_vertical+(1-length), board)-1))
            elif board.position_valid((offset_absolute+3), (self.from_flipped_to_non_flipped(offset_vertical+2, board)-1)):
                return ((offset_absolute+3), (self.from_flipped_to_non_flipped(offset_vertical+2, board)-1))

    def finish_game(self, board: Board) -> tuple:
        '''
        Checks if bot has the chance to win. If thats the case he tries to finish the row.

                Parameters:
                        self: bot
                        board: Board where Player is active
                        

                Returns:
                        tuple: field coordinates
        '''
        check_number = self.player_number
        check_winning = None
        check_winning = self.check_in_danger_horizontal(board,check_number)
        if check_winning == None:
            check_winning = self.check_in_danger_vertical(board, check_number)
        if check_winning == None:
            check_winning = self.check_in_danger_TLBR(board,check_number)
        if check_winning == None:
            check_winning = self.check_in_danger_BLTR(board, check_number)
        return check_winning
    
    def start_attack(self, board: Board) -> tuple:
        '''
        Starts an attacking row of two. This will enable the finish_game method.

                Parameters:
                        self: bot
                        board: Board where Player is active
                        

                Returns:
                        tuple: field coordinates
        '''
        for offset_horizontal in range (board.n_row - 1):
            for offset_vertical in range (board.m_col - 1):
                if board.field[offset_horizontal, offset_vertical] == self.player_number:
                    if board.position_valid(offset_horizontal + 1, offset_vertical):
                        return (offset_horizontal + 1, offset_vertical)
                    elif board.position_valid(offset_horizontal - 1, offset_vertical):
                        return (offset_horizontal - 1, offset_vertical)
                    elif board.position_valid(offset_horizontal, offset_vertical + 1):
                        return (offset_horizontal, offset_vertical + 1)
                    elif board.position_valid(offset_horizontal, offset_vertical - 1):
                        return (offset_horizontal, offset_vertical - 1)
                    elif board.position_valid(offset_horizontal + 1, offset_vertical + 1):
                        return (offset_horizontal + 1, offset_vertical + 1)
                    elif board.position_valid(offset_horizontal - 1, offset_vertical - 1):
                        return (offset_horizontal - 1, offset_vertical - 1)
                    elif board.position_valid(offset_horizontal + 1, offset_vertical - 1):
                        return (offset_horizontal + 1, offset_vertical - 1)
                    elif board.position_valid(offset_horizontal - 1, offset_vertical + 1):
                        return (offset_horizontal - 1, offset_vertical + 1)
        return None

    def to_string(self) -> str:
        """Returns the name, the number and the difficulty level of the bot as a string."""
        return(super().to_string() + '\n' + f"Schwierigkeitslevel: {self.difficulty_level}")

