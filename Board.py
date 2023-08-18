import numpy as np
from random import randint as r

class Board:


    def __init__(self, n = 5, m = 5,  k = 4) -> None:
        '''
            Constructor for the class Board. It initializes the field size(rows, cols) and the length of the elements in a row needed to win, with the given arguments.

            Parameters:
                    n(int): Board's number of rows
                    m(int): Board's number of columns
                    k(int): length of the row needed to win         
        '''
        self.n_row = n
        self.m_col = m
        self.k_in_a_row = k 
        self.field = np.full([n, m], 0)
        self.flipped_field = np.fliplr(self.field)        
        self.your_turn = r(0, 0)
    
    def reset(self) -> None:
        """Resets the board's squares to default (0)."""
        self.field.fill(0)
        self.your_turn = r(0, 0)        

    def create_top_border(self) -> str:
        """Returns a string that displays the board's columns."""
        whitespace = len(str(self.m_col))
        top_border = len(str(self.n_row)) * " " + " │ "
        
        for i in range(self.m_col):
            top_border += str(i)  + " │" + " " * (whitespace - len(str(i + 1)))
            if whitespace == 1:
                top_border += " "
        return top_border


    def create_board_row(self, row_index: int) -> str:
        """
            Returns a string that displaying a specific rows from the board.
            Parameter:
                row_index(int): indicating which row should be displayed
        """
        whitespace = len(str(self.n_row))
        row = str(row_index) + (" " * (whitespace - len(str(row_index)))) + " │ "        
        for j in range(len(self.field.tolist()[row_index])):
            row += self.visualize_number(self.field.tolist()[row_index][j]) + " │ "
        return(row)

    def create_border(self) -> str:
        """Returns a string that is a dotted line, matching the board's length."""
        return((len(self.create_board_row(0)) - 1) * "-")

    def to_string(self) -> str:
        """Returns the number of columns and rows and the needed span of fields to win."""
        return ("m_col: " + str(self.m_col) + '\n'+ "n_row: " + str(self.n_row) + '\n' + "k_in_a_row: " + str(self.k_in_a_row) )

    def display(self) -> None:
        """Prints a visualized version of the board."""
        field_list = self.field.tolist()        
        #Information
        print(self.to_string())
        #Top Border
        print(self.create_top_border())
        print(self.create_border())
        #Board
        for i in range(len(field_list)):
            print(self.create_board_row(i))
        #Bottom Border
        print(self.create_border())
        
    def visualize_number(self, number: int) -> str:
        '''
            isualizes player_number to either O, X or simple gap. 

                Parameters:
                    number(int): Number to visualize

                Return:
                    1 -> "O" is returned
                    2 -> "X" is returned
                    else " " is returned
        '''
        if number == 1:
            return "O"
        elif number == 2:
            return "X"
        else:
            return " "

    def position_free(self, row: int, col: int) -> bool:
        '''
            Checks if Position is not taken. 

                Parameters:
                        row(int): Row of the field to check
                        col(int): Column of the field to check

                Return: 
                        Returns if field is free as a boolean
        '''
        if self.field[row, col] == 0:
            return True
        else:
            return False
        
    def position_exists(self, row: int, col: int) -> bool:
        '''
            Checks if Position exists. Returns boolean.

                Parameters:
                        row(int): Row of the field to check
                        col(int): Column of the field to check
                Return: 
                    true -> positon exists in board(Board)
                    false -> positon doesn't exist in board(Board)
        '''
        if self.n_row <= row or row < 0 or self.m_col <= col or col < 0:
            return False
        else:
            return True
            
    def position_valid(self, row: int, col: int) -> bool:
        '''
            Checks if the given position is valid(existing on the field and not already taken)

                Parameters: 
                    row(int): y coordinate to be checked 
                    col(int): x coordinate to be checked 

                Return:
                    Boolean indicating if the position exists and is not taken.
        '''
        return (self.position_exists(row, col) and self.position_free(row, col))
    
    def take_turn(self) -> None: 
        '''Shifts an int between 0 and 1 indicating whose turn it is to make a move.'''
        self.your_turn = (self.your_turn + 1) % 2
    
    def get_turn(self) -> int:
        '''
            Getter returning the value of 'your_turn' indicating whose turn it is to make a move.
            
            Return:
                your_turn(int)
                0 -> player1's turn to make a move    
                1 -> player2's turn to make a move    
        '''
        return self.your_turn

    def has_won(self) -> int:
        '''
            Returns an int indicating if a player has met the win condition or if the game ended in a draw. 

                Return:
                    -1 -> game ended in a draw 
                    0 -> neither a win nor a draw, game continues 
                    1 -> Player 1 has won
                    2 -> Player 2 has won
                
        '''
        if not (0 in np.unique(self.field)): 
            return -1
        wonInt = self.check_horizontal()
        if(wonInt == 0):
            wonInt = self.check_vertical()
        if(wonInt == 0):
            wonInt = self.check_diagonal_TLBR()
        if(wonInt == 0):
            wonInt = self.check_diagonal_BLTR()    
        return wonInt

    def check_horizontal(self) -> int:
        """
            Returns if winning condition is achieved horizontal.

                Return: 
                number_horizontal(int): 1 -> player1 achieved a win horizontal 
                                        2 -> player2 achieved a win horizontal
                                        0 -> winning condition not met 
        """

        number_horizontal = 0
        for i in range(self.n_row):
            counter1 = 1
            counter2 = 1    
            for j in range (self.m_col - 1):
                if self.field[i,j] == self.field[i, (j + 1)] == 1:
                    counter1 += 1
                    counter2 = 1
                elif self.field[i , j] == self.field[i, (j + 1)] == 2:
                    counter2 += 1
                    counter1 = 1                    
                if (counter1 == self.k_in_a_row or counter2 == self.k_in_a_row):
                    if (counter1 == self.k_in_a_row):
                        number_horizontal = 1
                    else:
                        number_horizontal = 2
        return number_horizontal       
            
    def check_vertical(self) -> int:
        """
            Returns if winning condition is achieved vertical.

                Return: 
                number_vertical(int):   1 -> player1 achieved a win vertical 
                                        2 -> player2 achieved a win vertical
                                        0 -> winning condition not met 
        """
        
        number_vertical = 0
        for i in range(self.m_col):
            counter1 = 1
            counter2 = 1    
            for j in range (self.n_row -1):
                if self.field[j, i] == self.field[(j + 1), (i)] == 1:
                    counter1 += 1
                    counter2 = 1
                    if (counter1 == self.k_in_a_row):
                        number_vertical = 1
                elif self.field[j, i] == self.field[(j+1), (i)] == 2:
                    counter2 += 1
                    counter1 = 1
                    if (counter2 == self.k_in_a_row):
                        number_vertical = 2
        return number_vertical
    
    def check_diagonal_TLBR(self) -> int: # top left to bottom right corner 
        """
            Returns if winning condition is achieved diagonal from top left to bottom right

                Return: 
                number_diagonal(int):   1 -> player1 achieved a win diagonal 
                                        2 -> player2 achieved a win diagonal
                                        0 -> winning condition not met 
        """
        
        number_diagonal = 0
        for i in range((0-(self.n_row - 1)), (self.n_row - (self.k_in_a_row - 1))):
            diagonal_array = np.diagonal(self.field, i)
            counter1 = 1 
            counter2 = 1
            for j in range(len(diagonal_array) - 1): 
                if diagonal_array[j] == diagonal_array[(j + 1)] == 1:
                    counter1 += 1
                    counter2 = 1
                    if (counter1 == self.k_in_a_row):
                        number_diagonal = 1
                elif diagonal_array[j] == diagonal_array[(j + 1)] == 2:
                    counter2 += 1
                    counter1 = 1
                    if (counter2 == self.k_in_a_row):
                        number_diagonal = 2
        return number_diagonal

    def check_diagonal_BLTR(self) -> int: # bottom left to top right corner 
        """
            Returns if winning condition is achieved diagonal from bottom left to top right
                
                Return: 
                number_diagonal(int):   1 -> player1 achieved a win diagonal 
                                        2 -> player2 achieved a win diagonal
                                        0 -> winning condition not met 
        """
        
        number_diagonal = 0
        for i in range(-1, self.n_row - 3):
            flipped_field = np.fliplr(self.field)
            diagonal_array = np.diagonal(flipped_field, i)
            counter1 = 1 
            counter2 = 1
            for j in range(len(diagonal_array) - 1): 
                if diagonal_array[j] == diagonal_array[(j + 1)] == 1:
                    counter1 += 1
                    counter2 = 1
                    if (counter1 == self.k_in_a_row):
                        number_diagonal = 1
                elif diagonal_array[j] == diagonal_array[(j + 1)] == 2:
                    counter2 += 1
                    counter1 = 1
                    if (counter2 == self.k_in_a_row):
                        number_diagonal = 2
        return number_diagonal
    

