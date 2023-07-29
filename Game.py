from Board import Board
from Player import Player
from MyBot import MyBot 
import numpy as np

class Game:
        
    def start(self) -> None:
        '''
            Initializing board's width(m_number_cols) and height(n_number_rows) and the number deciding how many elements you need to place in a row to win.
            Initializing the players, differentiating between three version(player vs player/ player vs bot/ bot vs bot) decided through the users input 
            Starting the game loop 
        '''
        #initializing board
        while True: 
            try: 
                self.n_number_rows = int(input("Number of Rows: "))
                break
            except:
                print("Invalid input type. Choose again.")
        while True: 
            try: 
                self.m_number_cols = int(input("Number of Columns: "))   
                break
            except:
                print("Invalid input type. Choose again.")
        while True: 
            try: 
                self.number_k_in_a_row = int(input("Length of Row needed to win (The input needs to be smaller than the row- and the col-number): "))        
                if(self.m_number_cols > self.number_k_in_a_row and self.n_number_rows > self.number_k_in_a_row):
                    break
            except:
                print("Invalid input. Choose again.")

        self.board = Board(self.n_number_rows, self.m_number_cols, self.number_k_in_a_row)
        self.board.display()
                        
        #choose player number
        while True: 
            try:         
                player_decision = int(input("How many players are taking part in the game? Choose between 0 and 2: "))
                if(player_decision == 1 or player_decision == 2 or player_decision == 0):
                    break
            except:
                print("Your input is out of the expected range!")
        #initializing players        
        self.player_list = []

        while(int(player_decision) > 0):
            self.player_list.append(Player(str(input("please enter a name for player " + str(len(self.player_list) + 1) + ": " )), (len(self.player_list) + 1)))
            player_decision = int(player_decision) - 1

        while(len(self.player_list) < 2):
            botName = str(input("please enter a bot name: "))
            while True:
                try:         
                    difficulty_level = int(input("please choose a bot difficulty between 1 and 3: "))
                    if(difficulty_level == 1 or difficulty_level == 2 or difficulty_level == 3):
                        break
                except:
                    print("Your input is out of the expected range!")
                    
            self.player_list.append(MyBot(botName, (len(self.player_list) + 1), difficulty_level))
        self.game_loop()

    def game_loop(self) -> None:
        '''Game loop alternating between the two players making their move, checking if the win condition is met and stopping if thats the case.'''
        #start game loop 
        end = False
        while not end:
            self.board.display()
            if(not(isinstance(self.player_list[0], MyBot) and isinstance(self.player_list[1], MyBot))):
                while (self.board.has_won() == 0):
                    print("turn: " + self.player_list[self.board.get_turn()].name)
                    if(isinstance(self.player_list[self.board.get_turn()], MyBot)):
                        print("bot turn")
                        self.player_list[self.board.get_turn()].make_move(self.board) 
                    else:
                        print("player turn")
                        while True:
                            try:
                                row = int(input("Row Number: "))
                                col = int(input("Col Number: "))
                                break
                            except:
                                print("Invalid input type. Choose Again.")
                        self.player_list[self.board.get_turn()].make_move(row, col, self.board) 
                    self.board.display()

                print("The game finished !!!")
                if (self.board.has_won() == 1): 
                    print(self.player_list[0].to_string() + '\n' + "has won!")
                elif(self.board.has_won() == 2):
                    print(self.player_list[1].to_string() + '\n' + "has won!")
                elif(self.board.has_won() == -1):
                    print("The game is a draw.")
                self.board.reset()
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
                    while (self.board.has_won() == 0):
                        self.player_list[self.board.get_turn()].make_move(self.board) 

                    print("The game finished !!!")
                    self.board.display()
                    if (self.board.has_won() == 1): 
                        print(self.player_list[0].to_string() + '\n' + "has won!")
                    elif (self.board.has_won() == 2):
                        print(self.player_list[1].to_string() + '\n' + "has won!")
                    elif(self.board.has_won() == -1):
                        print("The game is a draw.")
                    self.board.reset()
                    counter += 1
                end = True
            

game = Game()
game.start()