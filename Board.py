import numpy as np

class Board:
    # n Zeilen, äußere Arrays
    nRow = None 
    # m Spalten - Elemente in den inneren Arrays
    mCol = None
    kInARow = None 
    field = None 
    flippedField = None

    takeTurn = 0

    def __init__(self, n = 5, m = 5,  k = 4) -> None:
        '''
        This is the constructor for the class Board. It sets its number of columns and rows and the length of the row needed to win.

                Parameters:
                        n(int): Board's number of rows
                        m(int): Board's number of columns
                        k(int): length of the row needed to win         
        '''
        self.nRow = n
        self.mCol = m
        self.kInARow = k 
        self.field = np.full([n, m], 0)
        self.flippedField = np.fliplr(self.field)

    
    def reset(self) -> None:
        """Resets the board's fields to default (0)."""
        self.field.fill(0)
        self.takeTurn = 0
        
    def fillUp(self, number: int) -> None:
        """Fills the Board's fields with the given player_number."""
        self.field.fill(number)

    def createTopBorder(self) -> str:
        """Returns a string that displays the board's columns."""
        topBorder = "  │ "
        if(self.mCol <= 10):
            for i in range(self.mCol):
                topBorder += str(i) + " │ "
        else:
            for i in range(10):
                topBorder += str(i) + " │ "
            for i in range(10,self.mCol):
                topBorder += str(i) + "│ "
        return(topBorder)

    def createBoardRow(self, rowIndex: int) -> str:
        """Returns a string that displays the board's rows including the field itself."""
        row = str(rowIndex) + " │ "
        for j in range(len(self.field.tolist()[rowIndex])):
            row += self.visualizeNumber(self.field.tolist()[rowIndex][j]) + " │ "
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
            #print("position free")
            return True
        else:
            #print("position not free")
            return False
        
    def positionExists(self, row: int, col: int) -> bool:
        '''
        Checks if Position exists. Returns boolean

                Parameters:
                        row(int): Row of the field to check
                        col(int): Column of the field to check

                Returns: 
                        Returns if field exists as a boolean
        '''
        if self.nRow <= row or row < 0 or self.mCol <= col or col < 0:
            #print("position doesnt exist")
            return False
        else:
            #print("position exists")
            return True
            
    def has_won(self) -> int:
        if not (0 in np.unique(self.field)): 
            return -1
        wonInt = self.checkHorizontal()
        if(wonInt == 0):
            wonInt = self.checkVertical()
        if(wonInt == 0):
            wonInt = self.checkDiagonalTLBR()
        if(wonInt == 0):
            wonInt = self.checkDiagonalBLTR()    
        return wonInt
    
    def take_turn(self): 
        self.takeTurn = (self.takeTurn + 1) % 2
    
    def getTurn(self) -> int:
        return self.takeTurn 

    def toString(self) -> str:
        """Returns the number of columns and rows and the needed span of fields to win."""
        return ("mCol: " + str(self.mCol) + '\n'+ "nRow: " + str(self.nRow) + '\n' + "kInRow: " + str(self.kInARow) )

    def checkHorizontal(self) -> int:
        """Returns if winning condition is achieved horizontally."""

        numberHorizontal = 0
        for i in range(self.nRow):
            counter1 = 1
            counter2 = 1    
            for j in range (self.mCol - 1):
                if self.field[i,j] == self.field[i, (j + 1)] == 1:
                    counter1 += 1
                    if (counter1 == self.kInARow):
                        numberHorizontal = 1
                elif self.field[i , j] == self.field[i, (j + 1)] == 2:
                    counter2 += 1
                    if (counter2 == self.kInARow):
                        numberHorizontal = 2 
        return numberHorizontal       
            
    def checkVertical(self) -> int:
        """Returns if winning condition is achieved vertically."""
        
        numberVertical = 0
        for i in range(self.mCol):
            counter1 = 1
            counter2 = 1    
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
    
    def checkDiagonalTLBR(self) -> int:
        """Returns if winning condition is achieved diagonally from top left to bottom right"""
        
        numberDiagonal = 0
        for i in range((0-(self.nRow-1)), (self.nRow - (self.kInARow-1))):
            diagonalArray = np.diagonal(self.field, i)
            counter1 = 1 
            counter2 = 1
            for j in range(len(diagonalArray) - 1): 
                if diagonalArray[j] == diagonalArray[(j + 1)] == 1:
                    counter1 += 1
                    if (counter1 == self.kInARow):
                        numberDiagonal = 1
                elif diagonalArray[j] == diagonalArray[(j + 1)] == 2:
                    counter2 += 1
                    if (counter2 == self.kInARow):
                        numberDiagonal = 2
        return numberDiagonal

    def checkDiagonalBLTR(self) -> int:
        """Returns if winning condition is achieved diagonally from bottom left to top right"""
        
        numberDiagonal = 0
        for i in range(-1, self.nRow - 3):
            flippedField = np.fliplr(self.field)
            diagonalArray = np.diagonal(flippedField, i)
            counter1 = 1 
            counter2 = 1
            for j in range(len(diagonalArray) - 1): 
                if diagonalArray[j] == diagonalArray[(j + 1)] == 1:
                    counter1 += 1
                    if (counter1 == self.kInARow):
                        numberDiagonal = 1
                elif diagonalArray[j] == diagonalArray[(j + 1)] == 2:
                    counter2 += 1
                    if (counter2 == self.kInARow):
                        numberDiagonal = 2
        return numberDiagonal

    '''def flip(self) -> None: 
        self.field = np.fliplr(self.field)
        self.flipped = not self.flipped'''