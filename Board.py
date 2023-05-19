import numpy as np

class Board:
    # n Zeilen, äußere Arrays
    nRow = None 
    # m Spalten - Elemente in den inneren Arrays
    mCol = None
    kInARow = None 
    field = None 

    def __init__(self, m = 5, n = 5,  k = 4) -> None:
        '''
        This is the constructor for the class Board. It sets its number of columns and rows and the length of the row needed to win.

                Parameters:
                        m(int): Board's number of columns
                        n(int): Board's number of rows
                        k(int): length of the row needed to win         
        '''
        self.nRow = n
        self.mCol = m
        self.kInARow = k 
        self.field = np.full([m, n], 0)
    
    def reset(self) -> None:
        """Resets the board's fields to default (0)."""
        self.field.fill(0)
        

    def fillUp(self, number: int) -> None:
        """Fills the Board's fields with"""
        self.field.fill(number)

    def createTopBorder(self) -> str:
        """Returns a string that displays the board's columns."""
        topBorder = "  | "
        for i in range(len(self.field.tolist())):
            topBorder += str(i) + " | "
        return(topBorder)

    def createBoardRow(self, rowIndex: int) -> str:
        """Returns a string that displays the board's rows including the field itself."""
        row = str(rowIndex) + " | "
        for j in range(len(self.field.tolist()[rowIndex])):
            row += self.visualizeNumber(self.field.tolist()[rowIndex][j]) + " | "
        return(row)

    def createBorder(self) -> str:
        """Returns a string that is a dotted line, matching the board's length."""
        return((len(self.createBoardRow(0)) - 1) * "-")

    def display(self) -> None:
        """Returns the Board as a complete string."""
        field_list = self.field.tolist()        
        #Information
        print(self.toString())
        #Top Border
        print(self.createTopBorder())
        print(self.createBorder())
        #Board
        for i in range(len(field_list)):
            row = str(i) + " | "
            print(self.createBoardRow(i))
        #Bottom Border
        print(self.createBorder())
        

    def visualizeNumber(self, number: int) -> str:
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

    def positionFree(self, row: int, col: int) -> bool:
        '''
        Checks if Position is free. Returns boolean

                Parameters:
                        row(int): Row of the field to check
                        col(int): Column of the field to check

                Returns: 
                        Returns if field is free as a boolean
        '''
        if self.field[row, col] == 0:
            print("position free")
            return True
        else:
            print("position not free")
            return False

    def positionExists(self, row:int, col:int) -> bool:
        '''
        Checks if Position exists. Returns boolean

                Parameters:
                        row(int): Row of the field to check
                        col(int): Column of the field to check

                Returns: 
                        Returns if field exists as a boolean
        '''
        if self.nRow <= row or row < 0 or self.mCol <= col or col < 0:
            print("position doesnt exist")
            return False
        else:
            print("position exists")
            return True

            
    def has_won(self) -> int:
        if 0 in np.unique(self.field): 
            return 0
    

    def toString(self) -> str:
        """Returns the number of columns and rows and the needed span of fields to win."""
        return ("mCol: " + str(self.mCol) + '\n'+ "nRow: " + str(self.nRow) + '\n' + "kInRow: " + str(self.kInARow) )

#board = Board()
#board.fillUp(2)
#board.display()
#board.reset()
#board.display()
#board.fillUp(2)
#board.display()