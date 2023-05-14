import numpy as np

class Board:
    mCol = None
    nRow = None 
    kInARow = None 
    fields = None 

    def __init__(self, m = 5, n = 5, k = 4) -> None:
        self.mCol = m
        self.nRow = n
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
        #Border 

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

    def has_won(self) -> int:
        return 
    

    def toString(self) -> str:
        return ("mCol: " + str(self.mCol) + '\n'+ "nRow: " + str(self.nRow) + '\n' + "kInRow: " + str(self.kInARow) )

b = np.full([5, 4], 0)
b_list = b.tolist()
for i in range(len(b_list)):
    row = "| "
    for j in range(len(b_list[i])):
        row += (str(b_list[i][j]) + " | ")
    print(row)
    #print((len(row) - 1) * "-" )
#b.display()
#print(b.field[0].size)
board = Board()
board.display()

