import numpy as np

class Board:
    # n Zeilen, äußere Arrays
    nRow = None 
    # m Spalten - Elemente in den inneren Arrays
    mCol = None
    kInARow = None 
    field = None 

    def __init__(self, m = 5, n = 5,  k = 4) -> None:
        self.nRow = n
        self.mCol = m
        self.kInARow = k 
        self.field = np.full([m, n], 0)
    
    def reset(self) -> None:
        return 

    def createTopBorder(self) -> str:
        topBorder = "  | "
        for i in range(len(self.field.tolist())):
            topBorder += str(i) + " | "
        return(topBorder)

    def createBoardRow(self, rowIndex: int) -> str:
        row = str(rowIndex) + " | "
        for j in range(len(self.field.tolist()[rowIndex])):
            row += self.visualizeNumber(self.field.tolist()[rowIndex][j]) + " | "
        return(row)

    def createBorder(self) -> str:
        return((len(self.createBoardRow(0)) - 1) * "-")

    def display(self) -> None:
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
        return ("mCol: " + str(self.mCol) + '\n'+ "nRow: " + str(self.nRow) + '\n' + "kInRow: " + str(self.kInARow) )



#board = Board()
#board.display()

#test