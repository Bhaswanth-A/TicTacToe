# Importing random module
import random
# Importing Tokens class from variables.py file
from tokens import Tokens, board_details

# Class Creation


class TicTacToe():

    def __init__(self):

        Tokens.empty_board()  # Calling empty_board() function to print the empty TicTacToe board

        # A random number that decides which Player plays first
        self.num = random.randint(1, 2)

        # When Player 1 starts first
        if(self.num == 1):
            print('\n\nPlayer 1 starts first.\n')
            self.var = input('Choose: X or O  ')
            if(self.var == 'X' or self.var == 'x'):  # If Player 1 chooses X
                print('Player 1 chose X')
                print('Player 2 plays O\n')
                self.var1 = 'X'   # var1 --> Player 1
                self.var2 = 'O'   # var2 --> Player 2
            if(self.var == 'O' or self.var == 'o'):  # If Player 1 chooses O
                print('Player 1 chose O')
                print('Player 2 plays X\n')
                self.var1 = 'O'   # var1 --> Player 1
                self.var2 = 'X'   # var2 --> Player 2

        # When Player 2 starts first
        if(self.num == 2):
            print('\n\nPlayer 2 starts first.\n')
            self.var = input('Choose: X or O  ')
            if(self.var == 'X' or self.var == 'x'):  # If Player 2 chooses X
                print('Player 2 chose X')
                print('Player 1 plays O\n')
                self.var2 = 'X'   # var2 --> Player 2
                self.var1 = 'O'   # var1 --> Player 1
            if(self.var == 'O' or self.var == 'o'):  # If Player 2 chooses O
                print('Player 2 chose O')
                print('Player 1 plays X\n')
                self.var2 = 'O'   # var2 --> Player 2
                self.var1 = 'X'   # var1 --> Player 1

        # Print input formats of the game
        print('\n\t INPUT FORMATS \n')
        print('00 --> Row 1, Column 1 \n01 --> Row 1, Column 2 \n02 --> Row 1, Column 3')
        print('10 --> Row 2, Column 1 \n11 --> Row 2, Column 2 \n12 --> Row 2, Column 3')
        print('20 --> Row 3, Column 1 \n21 --> Row 3, Column 2 \n22 --> Row 3, Column 3')
        print()

    # Player 1 method
    def player_1(self, pos, var1, var2, num):
        board_details(pos, var1, var2, num)

    # Player 2 method
    def player_2(self, pos, var1, var2, num):
        board_details(pos, var1, var2, num)

    # Method that avoids incorrect inputs from players
    def incorrect_inputs(self):

        if(self.num == 1):
            while not(self.position == '00' or self.position == '01' or self.position == '02' or self.position == '10' or self.position == '11' or self.position == '12'
                      or self.position == '20' or self.position == '21' or self.position == '22'):
                print("Incorrect input! Try again")
                self.position = input('\nEnter position Variable again: ')

        if(self.num == 2):
            while not(self.position == '00' or self.position == '01' or self.position == '02' or self.position == '10' or self.position == '11' or self.position == '12'
                      or self.position == '20' or self.position == '21' or self.position == '22'):
                print("Incorrect input! Try again")
                self.position = input('\nEnter position Variable again: ')

    # Method that avoids repeated inputs from both players
    def repeated_inputs(self):

        if(self.i != 0):
            while(self.position == self.pos[0] or self.position == self.pos[1] or self.position == self.pos[2] or self.position == self.pos[3] or self.position == self.pos[4]):
                print(
                    "\nThis block is already occupied..try a different space!")
                self.position = input(
                    '\nEnter position Variable again: ')

    # Method that takes inputs from both players
    def inputs(self):
        self.pos = ['x', 'o', 'x', 'o', 'x', 'o', 'x', 'o',
                    'x', 'o']  # List to store user inputs

        for self.i in [0, 1, 2, 3, 4]:

            if(self.num == 1):  # When Player 1 starts first
                self.position = input('\nPlayer 1 enter position Variable: ')
                print()

                # Incorrect inputs
                self.incorrect_inputs()
                # Repeated inputs
                self.repeated_inputs()
                # Incorrect inputs
                self.incorrect_inputs()

                # Storing user inputs in the list at different index positions
                self.pos[2*self.i] = self.position
                # Passing user inputs to player_1() method
                self.player_1(self.pos, self.var1, self.var2, self.num)

                self.position = input('\nPlayer 2 enter position Variable: ')
                print()

                # Incorrect inputs
                self.incorrect_inputs()
                # Repeated inputs
                self.repeated_inputs()
                # Incorrect inputs
                self.incorrect_inputs()

                # Storing user inputs in the list at different index positions
                self.pos[2*self.i + 1] = self.position
                # Passing user inputs to player_2() method
                self.player_2(self.pos, self.var1, self.var2, self.num)

            if(self.num == 2):  # When Player 2 starts first

                self.position = input('\nPlayer 2 enter position Variable: ')
                print()

                # Incorrect inputs
                self.incorrect_inputs()
                # Repeated inputs
                self.repeated_inputs()
                # Incorrect inputs
                self.incorrect_inputs()

                # Storing user inputs in the list at different index positions
                self.pos[2*self.i] = self.position
                # Passing user inputs to player_2() method
                self.player_2(self.pos, self.var1, self.var2, self.num)

                self.position = input('\nPlayer 1 enter position Variable: ')
                print()

                # Incorrect inputs
                self.incorrect_inputs()
                # Repeated inputs
                self.repeated_inputs()
                # Incorrect inputs
                self.incorrect_inputs()

                # Storing user inputs in the list at different index positions
                self.pos[2*self.i + 1] = self.position
                # Passing user inputs to player_1() method
                self.player_1(self.pos, self.var1, self.var2, self.num)


# Initializing game object
game = TicTacToe()
game.inputs()
