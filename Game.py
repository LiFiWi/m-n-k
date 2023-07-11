from Board import Board
from Player import Player
from MyBot import MyBot 
import numpy as np

class Game:
    def __init__(self):
        return 
        
    def start(self) -> None:
        return

    def game_loop(self) -> None:
        finished = False 
        while not finished:
            print()
    
#build outer game loop, making several playthroughs possible without restarting programm

#initializing board
while True: 
    try: 
        number_rows = int(input("Number of Rows: "))
        break
    except:
        print("Invalid input type. Choose again.")
while True: 
    try: 
        number_cols = int(input("Number of Columns: "))   
        break
    except:
        print("Invalid input type. Choose again.")
while True: 
    try: 
        number_k_in_a_row = int(input("Length of Row needed to win (The input needs to be smaller than the row- and the col-number): "))        
        if(number_cols > number_k_in_a_row and number_rows > number_k_in_a_row):
            break
    except:
        print("Invalid input. Choose again.")

board = Board(number_rows, number_cols, number_k_in_a_row)
board.display()
#choose player number
while True: 
    try:         
        player_decision = int(input("How many players are taking part in the game? Choose between 0 and 2: "))
        if(player_decision == 1 or player_decision == 2 or player_decision == 0):
            break
    except:
        print("Your input is out of the expected range!")
#initialzing players
player_list = []
while(int(player_decision) > 0):
    player_list.append(Player(str(input("please enter a name for player " + str(len(player_list) + 1) + ": " )), (len(player_list) + 1)))
    player_decision = int(player_decision) - 1

while(len(player_list) < 2):
    botName = str(input("please enter a bot name: "))
    while True:
        try:         
            difficulty_level = int(input("please choose a bot difficulty between 1 and 3: "))
            if(difficulty_level == 1 or difficulty_level == 2 or difficulty_level == 3):
                break
        except:
            print("Your input is out of the expected range!")
    player_list.append(MyBot(botName, (len(player_list) + 1), difficulty_level))
    

#start game loop 
end = False
while not end:
    board.display()
    if(not(isinstance(player_list[0], MyBot) and isinstance(player_list[1], MyBot))):
        while (board.has_won() == 0):
            print("turn: " + player_list[board.get_turn()].name)
            if(isinstance(player_list[board.get_turn()], MyBot)):
                print("bot turn")
                player_list[board.get_turn()].make_move(board) 
            else:
                print("player turn")
                while True:
                    try:
                        row = int(input("Row Number: "))
                        col = int(input("Col Number: "))
                        break
                    except:
                        print("Invalid input type. Choose Again.")
                player_list[board.get_turn()].make_move(row, col, board) 
            board.display()

        print("The game finished !!!")
        if (board.has_won() == 1): 
            print(player_list[0].name + " has won!")
        elif(board.has_won() == 2):
            print(player_list[1].name + " has won!")
        elif(board.has_won() == -1):
            print("The game is a draw.")
        board.reset()
        if(str(input("do you want to play another round? (yes/ no) ")) != "yes"):
            print("Thanks for playing.")
            end = True
        

    else:
        while True:
            try:
                rounds = int(input("How many rounds do you want your bots to battle? "))
                break
            except:
                print("Invalid input type. Choose Again.")
        counter = 0
        while (counter < rounds):
            print("Round: " + str(counter + 1) + " ---------------------------------------------------------------------------------------")
            while (board.has_won() == 0):
                player_list[board.get_turn()].make_move(board) 

            print("The game finished !!!")
            board.display()
            if (board.has_won() == 1): 
                print(player_list[0].name + " has won!")
            elif (board.has_won() == 2):
                print(player_list[1].name + " has won!")
            elif(board.has_won() == -1):
                print("The game is a draw.")
            board.reset()
            counter += 1
        end = True