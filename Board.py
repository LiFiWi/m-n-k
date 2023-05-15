import numpy as np

class Board:
    nRow = None 
    mCol = None
    kInARow = None 
    field = None 

    def __init__(self, n = 5,  m = 5, k = 4) -> None:
        self.nRow = n
        self.mCol = m
        self.kInARow = k 
        self.field = np.full([m, n], 0)
    
    def reset(self) -> None:
        return

    def display(self) -> None:
        field_list = self.field.tolist()
        #Information
        print(self.toString())
        #Variables 
        field_list = self.field.tolist()
        #Board
        for i in range(len(field_list)):
            row = "| "
            for j in range(len(field_list[i])):
                row += (self.visualizeNumber((field_list[i][j])) + " | ")
            print(row)
        #Border
        print((len(row) - 1) * "-" )
        #print(self.field)

    def visualizeNumber(self, number: int) -> str:
        if number == 1:
            return "O"
        elif number == 2:
            return "X"
        else:
            return " "

    def positionFree(self, row: int, col: int) -> bool:
        if self.field[row, col] == 0:
            return True
        else:
            return False

    def positionExists(self, row:int, col:int) -> bool:
        if self.nRow <= row or self.mCol <= col:
            return False
        else:
            return True
            
    def has_won(self) -> int:
        if 0 in numpy.unique(field): 
            return 0 
    

    def toString(self) -> str:
        return ("mCol: " + str(self.mCol) + '\n'+ "nRow: " + str(self.nRow) + '\n' + "kInRow: " + str(self.kInARow) )



#board = Board()
#board.display()

