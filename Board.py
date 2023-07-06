import numpy as np

class Board:
    # n Zeilen, äußere Arrays
    n_row = None 
    # m Spalten - Elemente in den inneren Arrays
    m_col = None
    k_in_a_row = None 
    field = None 
    flipped_field = None

    your_turn = 0

    def __init__(self, n = 5, m = 5,  k = 4) -> None:
        '''
        This is the constructor for the class Board. It sets its number of columns and rows and the length of the row needed to win.

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

    
    def reset(self) -> None:
        """Resets the board's fields to default (0)."""
        self.field.fill(0)
        self.take_turn = 0
        
    def fill_up(self, number: int) -> None:
        """Fills the Board's fields with the given player_number."""
        self.field.fill(number)

    def create_top_border(self) -> str:
        """Returns a string that displays the board's columns."""
        top_border = "  │ "
        if(self.m_col <= 10):
            for i in range(self.m_col):
                top_border += str(i) + " │ "
        else:
            for i in range(10):
                top_border += str(i) + " │ "
            for i in range(10,self.m_col):
                top_border += str(i) + "│ "
        return(top_border)

    def create_board_row(self, row_index: int) -> str:
        """Returns a string that displays the board's rows including the field itself."""
        row = str(row_index) + " │ "
        for j in range(len(self.field.tolist()[row_index])):
            row += self.visualize_number(self.field.tolist()[row_index][j]) + " │ "
        return(row)

    def create_border(self) -> str:
        """Returns a string that is a dotted line, matching the board's length."""
        return((len(self.create_board_row(0)) - 1) * "-")

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
            row = str(i) + " | "
            print(self.create_board_row(i))
        #Bottom Border
        print(self.create_border())
        
    def visualize_number(self, number: int) -> str:
        '''
        Visualizes player_number to either O, X or simple gap. Returns a string.

                Parameters:
                        number(int): Number to visualize

                Returns:
                        if number is 1, "O" is returned
                        if number is 2, "X" is returned
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
        Checks if Position is free. Returns boolean

                Parameters:
                        row(int): Row of the field to check
                        col(int): Column of the field to check

                Returns: 
                        Returns if field is free as a boolean
        '''
        if self.field[row, col] == 0:
            #print("position free")
            return True
        else:
            #print("position not free")
            return False
        
    def position_exists(self, row: int, col: int) -> bool:
        '''
        Checks if Position exists. Returns boolean

                Parameters:
                        row(int): Row of the field to check
                        col(int): Column of the field to check

                Returns: 
                        Returns if field exists as a boolean
        '''
        if self.n_row <= row or row < 0 or self.m_col <= col or col < 0:
            #print("position doesnt exist")
            return False
        else:
            #print("position exists")
            return True
            
    def has_won(self) -> int:
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
    
    def take_turn(self): 
        self.your_turn = (self.your_turn + 1) % 2
    
    def get_turn(self) -> int:
        return self.your_turn

    def to_string(self) -> str:
        """Returns the number of columns and rows and the needed span of fields to win."""
        return ("m_col: " + str(self.m_col) + '\n'+ "n_row: " + str(self.n_row) + '\n' + "k_in_a_row: " + str(self.k_in_a_row) )

    def check_horizontal(self) -> int:
        """Returns if winning condition is achieved horizontally."""

        number_horizontal = 0
        for i in range(self.n_row):
            counter1 = 1
            counter2 = 1    
            for j in range (self.m_col - 1):
                if self.field[i,j] == self.field[i, (j + 1)] == 1:
                    counter1 += 1
                    if (counter1 == self.k_in_a_row):
                        number_horizontal = 1
                elif self.field[i , j] == self.field[i, (j + 1)] == 2:
                    counter2 += 1
                    if (counter2 == self.k_in_a_row):
                        number_horizontal = 2 
        return number_horizontal       
            
    def check_vertical(self) -> int:
        """Returns if winning condition is achieved vertically."""
        
        number_vertical = 0
        for i in range(self.m_col):
            counter1 = 1
            counter2 = 1    
            for j in range (self.n_row -1):
                if self.field[j, i] == self.field[(j + 1), (i)] == 1:
                    counter1 += 1
                    if (counter1 == self.k_in_a_row):
                        number_vertical = 1
                elif self.field[j, i] == self.field[(j+1), (i)] == 2:
                    counter2 += 1
                    if (counter2 == self.k_in_a_row):
                        number_vertical = 2
        return number_vertical
    
    def check_diagonal_TLBR(self) -> int:
        """Returns if winning condition is achieved diagonally from top left to bottom right"""
        
        number_diagonal = 0
        for i in range((0-(self.n_row - 1)), (self.n_row - (self.k_in_a_row - 1))):
            diagonal_array = np.diagonal(self.field, i)
            counter1 = 1 
            counter2 = 1
            for j in range(len(diagonal_array) - 1): 
                if diagonal_array[j] == diagonal_array[(j + 1)] == 1:
                    counter1 += 1
                    if (counter1 == self.k_in_a_row):
                        number_diagonal = 1
                elif diagonal_array[j] == diagonal_array[(j + 1)] == 2:
                    counter2 += 1
                    if (counter2 == self.k_in_a_row):
                        number_diagonal = 2
        return number_diagonal

    def check_diagonal_BLTR(self) -> int:
        """Returns if winning condition is achieved diagonally from bottom left to top right"""
        
        number_diagonal = 0
        for i in range(-1, self.n_row - 3):
            flipped_field = np.fliplr(self.field)
            diagonal_array = np.diagonal(flipped_field, i)
            counter1 = 1 
            counter2 = 1
            for j in range(len(diagonal_array) - 1): 
                if diagonal_array[j] == diagonal_array[(j + 1)] == 1:
                    counter1 += 1
                    if (counter1 == self.k_in_a_row):
                        number_diagonal = 1
                elif diagonal_array[j] == diagonal_array[(j + 1)] == 2:
                    counter2 += 1
                    if (counter2 == self.k_in_a_row):
                        number_diagonal = 2
        return number_diagonal
    
    def position_valid(self, row: int, col: int) -> bool:
        return (self.position_exists(row, col) and self.position_free(row, col))
