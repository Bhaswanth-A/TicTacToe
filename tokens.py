# Importing numpy module
import numpy as np
# Importing sys module
import sys

# Class Creation


class Tokens():

    def __init__(self):
        pass  # Leave constructor empty

    # Method that stores X shape
    def x_shape(self):

        x = list([['| ', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x '],
                  ['| ', ' ', ' ', 'x', 'x', ' ', ' ', 'x', 'x', ' ', '  '],
                  ['| ', ' ', ' ', ' ', ' ', 'x', 'x', ' ', ' ', ' ', '  '],
                  ['| ', ' ', ' ', 'x', 'x', ' ', ' ', 'x', 'x', ' ', '  '],
                  ['| ', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x ']])

        return x

    # Method that stores O shape
    def o_shape(self):

        o = list([['| ', ' ', ' ', ' ', 'o', 'o', 'o', 'o', ' ', ' ', '  '],
                  ['| ', ' ', 'o', 'o', ' ', ' ', ' ', ' ', 'o', 'o', '  '],
                  ['| ', 'o', 'o', ' ', ' ', ' ', ' ', ' ', ' ', 'o', 'o '],
                  ['| ', ' ', 'o', 'o', ' ', ' ', ' ', ' ', 'o', 'o', '  '],
                  ['| ', ' ', ' ', ' ', 'o', 'o', 'o', 'o', ' ', ' ', '  ']])

        return o

    # Method that stores an empty shape
    def empty_shape(self):

        e = list([['| ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '  '],
                  ['| ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '  '],
                  ['| ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '  '],
                  ['| ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '  '],
                  ['| ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '  ']])

        return e

    # Method that prints an empty board
    def empty_board():

        for k in range(0, 3):
            for i in range(0, 5):
                matrix_empty = np.array(
                    ['|', ' '*12, '|', ' '*12, '|', ' '*12, '|'])

                for row in matrix_empty:
                    for val in row:
                        print(val, end="")
                    print('', end="")
                print()
            if(k == 2):
                break
            else:
                print('-'*40)

    # Method that defines the winning condition
    def win_func(self):

        if(self.var1 == 'X'):  # Player 1 chooses X or Player 2 chooses O

            # Horizontal X win
            if(self.my_matrix_1[0] == self.my_matrix_1[1] == self.my_matrix_1[2] == self.x_shape()):
                sys.exit('\nPlayer 1 wins')
            if(self.my_matrix_2[0] == self.my_matrix_2[1] == self.my_matrix_2[2] == self.x_shape()):
                sys.exit('\nPlayer 1 wins')
            if(self.my_matrix_3[0] == self.my_matrix_3[1] == self.my_matrix_3[2] == self.x_shape()):
                sys.exit('\nPlayer 1 wins')

            # Horizontal O win
            if(self.my_matrix_1[0] == self.my_matrix_1[1] == self.my_matrix_1[2] == self.o_shape()):
                sys.exit('\nPlayer 2 wins')
            if(self.my_matrix_2[0] == self.my_matrix_2[1] == self.my_matrix_2[2] == self.o_shape()):
                sys.exit('\nPlayer 2 wins')
            if(self.my_matrix_3[0] == self.my_matrix_3[1] == self.my_matrix_3[2] == self.o_shape()):
                sys.exit('\nPlayer 2 wins')

            # Vertical X win
            if(self.my_matrix_1[0] == self.my_matrix_2[0] == self.my_matrix_3[0] == self.x_shape()):
                sys.exit('\nPlayer 1 wins')
            if(self.my_matrix_1[1] == self.my_matrix_2[1] == self.my_matrix_3[1] == self.x_shape()):
                sys.exit('\nPlayer 1 wins')
            if(self.my_matrix_1[2] == self.my_matrix_2[2] == self.my_matrix_3[2] == self.x_shape()):
                sys.exit('\nPlayer 1 wins')

            # Vertical O win
            if(self.my_matrix_1[0] == self.my_matrix_2[0] == self.my_matrix_3[0] == self.o_shape()):
                sys.exit('\nPlayer 2 wins')
            if(self.my_matrix_1[1] == self.my_matrix_2[1] == self.my_matrix_3[1] == self.o_shape()):
                sys.exit('\nPlayer 2 wins')
            if(self.my_matrix_1[2] == self.my_matrix_2[2] == self.my_matrix_3[2] == self.o_shape()):
                sys.exit('\nPlayer 2 wins')

            # Diagonal X win
            if(self.my_matrix_1[0] == self.my_matrix_2[1] == self.my_matrix_3[2] == self.x_shape()):
                sys.exit('\nPlayer 1 wins')
            if(self.my_matrix_1[2] == self.my_matrix_2[1] == self.my_matrix_3[0] == self.x_shape()):
                sys.exit('\nPlayer 1 wins')

            # Diagonal O win
            if(self.my_matrix_1[0] == self.my_matrix_2[1] == self.my_matrix_3[2] == self.o_shape()):
                sys.exit('\nPlayer 2 wins')
            if(self.my_matrix_1[2] == self.my_matrix_2[1] == self.my_matrix_3[0] == self.o_shape()):
                sys.exit('\nPlayer 2 wins')

            # Draw condition
            else:
                if(self.val[8] != 'x'):
                    sys.exit('\nMatch Draw\n')

        if(self.var1 == 'O'):  # Player 1 chooses O or Player 2 chooses X

            # Horizontal O win
            if(self.my_matrix_1[0] == self.my_matrix_1[1] == self.my_matrix_1[2] == self.o_shape()):
                sys.exit('\nPlayer 1 wins')
            if(self.my_matrix_2[0] == self.my_matrix_2[1] == self.my_matrix_2[2] == self.o_shape()):
                sys.exit('\nPlayer 1 wins')
            if(self.my_matrix_3[0] == self.my_matrix_3[1] == self.my_matrix_3[2] == self.o_shape()):
                sys.exit('\nPlayer 1 wins')

            # Horizontal X win
            if(self.my_matrix_1[0] == self.my_matrix_1[1] == self.my_matrix_1[2] == self.x_shape()):
                sys.exit('\nPlayer 2 wins')
            if(self.my_matrix_2[0] == self.my_matrix_2[1] == self.my_matrix_2[2] == self.x_shape()):
                sys.exit('\nPlayer 2 wins')
            if(self.my_matrix_3[0] == self.my_matrix_3[1] == self.my_matrix_3[2] == self.x_shape()):
                sys.exit('\nPlayer 2 wins')

            # Vertical O win
            if(self.my_matrix_1[0] == self.my_matrix_2[0] == self.my_matrix_3[0] == self.o_shape()):
                sys.exit('\nPlayer 1 wins')
            if(self.my_matrix_1[1] == self.my_matrix_2[1] == self.my_matrix_3[1] == self.o_shape()):
                sys.exit('\nPlayer 1 wins')
            if(self.my_matrix_1[2] == self.my_matrix_2[2] == self.my_matrix_3[2] == self.o_shape()):
                sys.exit('\nPlayer 1 wins')

            # Vertical X win
            if(self.my_matrix_1[0] == self.my_matrix_2[0] == self.my_matrix_3[0] == self.x_shape()):
                sys.exit('\nPlayer 2 wins')
            if(self.my_matrix_1[1] == self.my_matrix_2[1] == self.my_matrix_3[1] == self.x_shape()):
                sys.exit('\nPlayer 2 wins')
            if(self.my_matrix_1[2] == self.my_matrix_2[2] == self.my_matrix_3[2] == self.x_shape()):
                sys.exit('\nPlayer 2 wins')

            # Diagonal O win
            if(self.my_matrix_1[0] == self.my_matrix_2[1] == self.my_matrix_3[2] == self.o_shape()):
                sys.exit('\nPlayer 1 wins')
            if(self.my_matrix_1[2] == self.my_matrix_2[1] == self.my_matrix_3[0] == self.o_shape()):
                sys.exit('\nPlayer 1 wins')

            # Diagonal X win
            if(self.my_matrix_1[0] == self.my_matrix_2[1] == self.my_matrix_3[2] == self.x_shape()):
                sys.exit('\nPlayer 2 wins')
            if(self.my_matrix_1[2] == self.my_matrix_2[1] == self.my_matrix_3[0] == self.x_shape()):
                sys.exit('\nPlayer 2 wins')

            # Draw condition
            else:
                if(self.val[8] != 'x'):
                    sys.exit('\nMatch Draw\n')

    # Method that defines the main conditions for printing the board along with the elements at suitable places
    def main_conditions(self, val, var1, var2, num):

        self.val = val  # List that contains user inputs

        self.var1 = var1  # 'X or 'O' picked by Player 1
        self.var2 = var2  # 'X or 'O' picked by Player 2

        self.num = num

        # Initializing variables to store an empty shape
        self.v00 = self.empty_shape()
        self.v01 = self.empty_shape()
        self.v02 = self.empty_shape()
        self.v10 = self.empty_shape()
        self.v11 = self.empty_shape()
        self.v12 = self.empty_shape()
        self.v20 = self.empty_shape()
        self.v21 = self.empty_shape()
        self.v22 = self.empty_shape()

        if(self.num == 1):  # Player 1 picks first

            # Player 1 picks X
            if(self.var1 == 'X'):

                # Condition for varuiables to store X shape
                if(val[0] == '00' or val[2] == '00' or val[4] == '00' or val[6] == '00' or val[8] == '00'):
                    self.v00 = self.x_shape()
                if(val[0] == '01' or val[2] == '01' or val[4] == '01' or val[6] == '01' or val[8] == '01'):
                    self.v01 = self.x_shape()
                if(val[0] == '02' or val[2] == '02' or val[4] == '02' or val[6] == '02' or val[8] == '02'):
                    self.v02 = self.x_shape()
                if(val[0] == '10' or val[2] == '10' or val[4] == '10' or val[6] == '10' or val[8] == '10'):
                    self.v10 = self.x_shape()
                if(val[0] == '11' or val[2] == '11' or val[4] == '11' or val[6] == '11' or val[8] == '11'):
                    self.v11 = self.x_shape()
                if(val[0] == '12' or val[2] == '12' or val[4] == '12' or val[6] == '12' or val[8] == '12'):
                    self.v12 = self.x_shape()
                if(val[0] == '20' or val[2] == '20' or val[4] == '20' or val[6] == '20' or val[8] == '20'):
                    self.v20 = self.x_shape()
                if(val[0] == '21' or val[2] == '21' or val[4] == '21' or val[6] == '21' or val[8] == '21'):
                    self.v21 = self.x_shape()
                if(val[0] == '22' or val[2] == '22' or val[4] == '22' or val[6] == '22' or val[8] == '22'):
                    self.v22 = self.x_shape()

                # Condition for varuiables to store O shape
                if(val[1] == '00' or val[3] == '00' or val[5] == '00' or val[7] == '00' or val[9] == '00'):
                    self.v00 = self.o_shape()
                if(val[1] == '01' or val[3] == '01' or val[5] == '01' or val[7] == '01' or val[9] == '01'):
                    self.v01 = self.o_shape()
                if(val[1] == '02' or val[3] == '02' or val[5] == '02' or val[7] == '02' or val[9] == '02'):
                    self.v02 = self.o_shape()
                if(val[1] == '10' or val[3] == '10' or val[5] == '10' or val[7] == '10' or val[9] == '10'):
                    self.v10 = self.o_shape()
                if(val[1] == '11' or val[3] == '11' or val[5] == '11' or val[7] == '11' or val[9] == '11'):
                    self.v11 = self.o_shape()
                if(val[1] == '12' or val[3] == '12' or val[5] == '12' or val[7] == '12' or val[9] == '12'):
                    self.v12 = self.o_shape()
                if(val[1] == '20' or val[3] == '20' or val[5] == '20' or val[7] == '20' or val[9] == '20'):
                    self.v20 = self.o_shape()
                if(val[1] == '21' or val[3] == '21' or val[5] == '21' or val[7] == '21' or val[9] == '21'):
                    self.v21 = self.o_shape()
                if(val[1] == '22' or val[3] == '22' or val[5] == '22' or val[7] == '22' or val[9] == '22'):
                    self.v22 = self.o_shape()

            # Player 1 picks O
            if(self.var1 == 'O'):

                # Condition for varuiables to store O shape
                if(val[0] == '00' or val[2] == '00' or val[4] == '00' or val[6] == '00' or val[8] == '00'):
                    self.v00 = self.o_shape()
                if(val[0] == '01' or val[2] == '01' or val[4] == '01' or val[6] == '01' or val[8] == '01'):
                    self.v01 = self.o_shape()
                if(val[0] == '02' or val[2] == '02' or val[4] == '02' or val[6] == '02' or val[8] == '02'):
                    self.v02 = self.o_shape()
                if(val[0] == '10' or val[2] == '10' or val[4] == '10' or val[6] == '10' or val[8] == '10'):
                    self.v10 = self.o_shape()
                if(val[0] == '11' or val[2] == '11' or val[4] == '11' or val[6] == '11' or val[8] == '11'):
                    self.v11 = self.o_shape()
                if(val[0] == '12' or val[2] == '12' or val[4] == '12' or val[6] == '12' or val[8] == '12'):
                    self.v12 = self.o_shape()
                if(val[0] == '20' or val[2] == '20' or val[4] == '20' or val[6] == '20' or val[8] == '20'):
                    self.v20 = self.o_shape()
                if(val[0] == '21' or val[2] == '21' or val[4] == '21' or val[6] == '21' or val[8] == '21'):
                    self.v21 = self.o_shape()
                if(val[0] == '22' or val[2] == '22' or val[4] == '22' or val[6] == '22' or val[8] == '22'):
                    self.v22 = self.o_shape()

                # Condition for varuiables to store X shape
                if(val[1] == '00' or val[3] == '00' or val[5] == '00' or val[7] == '00' or val[9] == '00'):
                    self.v00 = self.x_shape()
                if(val[1] == '01' or val[3] == '01' or val[5] == '01' or val[7] == '01' or val[9] == '01'):
                    self.v01 = self.x_shape()
                if(val[1] == '02' or val[3] == '02' or val[5] == '02' or val[7] == '02' or val[9] == '02'):
                    self.v02 = self.x_shape()
                if(val[1] == '10' or val[3] == '10' or val[5] == '10' or val[7] == '10' or val[9] == '10'):
                    self.v10 = self.x_shape()
                if(val[1] == '11' or val[3] == '11' or val[5] == '11' or val[7] == '11' or val[9] == '11'):
                    self.v11 = self.x_shape()
                if(val[1] == '12' or val[3] == '12' or val[5] == '12' or val[7] == '12' or val[9] == '12'):
                    self.v12 = self.x_shape()
                if(val[1] == '20' or val[3] == '20' or val[5] == '20' or val[7] == '20' or val[9] == '20'):
                    self.v20 = self.x_shape()
                if(val[1] == '21' or val[3] == '21' or val[5] == '21' or val[7] == '21' or val[9] == '21'):
                    self.v21 = self.x_shape()
                if(val[1] == '22' or val[3] == '22' or val[5] == '22' or val[7] == '22' or val[9] == '22'):
                    self.v22 = self.x_shape()

        if(self.num == 2):  # Player 2 picks first

            # Player 2 picks X
            if(self.var2 == 'X'):

                # Condition for varuiables to store X shape
                if(val[0] == '00' or val[2] == '00' or val[4] == '00' or val[6] == '00' or val[8] == '00'):
                    self.v00 = self.x_shape()
                if(val[0] == '01' or val[2] == '01' or val[4] == '01' or val[6] == '01' or val[8] == '01'):
                    self.v01 = self.x_shape()
                if(val[0] == '02' or val[2] == '02' or val[4] == '02' or val[6] == '02' or val[8] == '02'):
                    self.v02 = self.x_shape()
                if(val[0] == '10' or val[2] == '10' or val[4] == '10' or val[6] == '10' or val[8] == '10'):
                    self.v10 = self.x_shape()
                if(val[0] == '11' or val[2] == '11' or val[4] == '11' or val[6] == '11' or val[8] == '11'):
                    self.v11 = self.x_shape()
                if(val[0] == '12' or val[2] == '12' or val[4] == '12' or val[6] == '12' or val[8] == '12'):
                    self.v12 = self.x_shape()
                if(val[0] == '20' or val[2] == '20' or val[4] == '20' or val[6] == '20' or val[8] == '20'):
                    self.v20 = self.x_shape()
                if(val[0] == '21' or val[2] == '21' or val[4] == '21' or val[6] == '21' or val[8] == '21'):
                    self.v21 = self.x_shape()
                if(val[0] == '22' or val[2] == '22' or val[4] == '22' or val[6] == '22' or val[8] == '22'):
                    self.v22 = self.x_shape()

                # Condition for varuiables to store O shape
                if(val[1] == '00' or val[3] == '00' or val[5] == '00' or val[7] == '00' or val[9] == '00'):
                    self.v00 = self.o_shape()
                if(val[1] == '01' or val[3] == '01' or val[5] == '01' or val[7] == '01' or val[9] == '01'):
                    self.v01 = self.o_shape()
                if(val[1] == '02' or val[3] == '02' or val[5] == '02' or val[7] == '02' or val[9] == '02'):
                    self.v02 = self.o_shape()
                if(val[1] == '10' or val[3] == '10' or val[5] == '10' or val[7] == '10' or val[9] == '10'):
                    self.v10 = self.o_shape()
                if(val[1] == '11' or val[3] == '11' or val[5] == '11' or val[7] == '11' or val[9] == '11'):
                    self.v11 = self.o_shape()
                if(val[1] == '12' or val[3] == '12' or val[5] == '12' or val[7] == '12' or val[9] == '12'):
                    self.v12 = self.o_shape()
                if(val[1] == '20' or val[3] == '20' or val[5] == '20' or val[7] == '20' or val[9] == '20'):
                    self.v20 = self.o_shape()
                if(val[1] == '21' or val[3] == '21' or val[5] == '21' or val[7] == '21' or val[9] == '21'):
                    self.v21 = self.o_shape()
                if(val[1] == '22' or val[3] == '22' or val[5] == '22' or val[7] == '22' or val[9] == '22'):
                    self.v22 = self.o_shape()

            # Player 2 picks O
            if(self.var2 == 'O'):

                # Condition for varuiables to store O shape
                if(val[0] == '00' or val[2] == '00' or val[4] == '00' or val[6] == '00' or val[8] == '00'):
                    self.v00 = self.o_shape()
                if(val[0] == '01' or val[2] == '01' or val[4] == '01' or val[6] == '01' or val[8] == '01'):
                    self.v01 = self.o_shape()
                if(val[0] == '02' or val[2] == '02' or val[4] == '02' or val[6] == '02' or val[8] == '02'):
                    self.v02 = self.o_shape()
                if(val[0] == '10' or val[2] == '10' or val[4] == '10' or val[6] == '10' or val[8] == '10'):
                    self.v10 = self.o_shape()
                if(val[0] == '11' or val[2] == '11' or val[4] == '11' or val[6] == '11' or val[8] == '11'):
                    self.v11 = self.o_shape()
                if(val[0] == '12' or val[2] == '12' or val[4] == '12' or val[6] == '12' or val[8] == '12'):
                    self.v12 = self.o_shape()
                if(val[0] == '20' or val[2] == '20' or val[4] == '20' or val[6] == '20' or val[8] == '20'):
                    self.v20 = self.o_shape()
                if(val[0] == '21' or val[2] == '21' or val[4] == '21' or val[6] == '21' or val[8] == '21'):
                    self.v21 = self.o_shape()
                if(val[0] == '22' or val[2] == '22' or val[4] == '22' or val[6] == '22' or val[8] == '22'):
                    self.v22 = self.o_shape()

                # Condition for varuiables to store X shape
                if(val[1] == '00' or val[3] == '00' or val[5] == '00' or val[7] == '00' or val[9] == '00'):
                    self.v00 = self.x_shape()
                if(val[1] == '01' or val[3] == '01' or val[5] == '01' or val[7] == '01' or val[9] == '01'):
                    self.v01 = self.x_shape()
                if(val[1] == '02' or val[3] == '02' or val[5] == '02' or val[7] == '02' or val[9] == '02'):
                    self.v02 = self.x_shape()
                if(val[1] == '10' or val[3] == '10' or val[5] == '10' or val[7] == '10' or val[9] == '10'):
                    self.v10 = self.x_shape()
                if(val[1] == '11' or val[3] == '11' or val[5] == '11' or val[7] == '11' or val[9] == '11'):
                    self.v11 = self.x_shape()
                if(val[1] == '12' or val[3] == '12' or val[5] == '12' or val[7] == '12' or val[9] == '12'):
                    self.v12 = self.x_shape()
                if(val[1] == '20' or val[3] == '20' or val[5] == '20' or val[7] == '20' or val[9] == '20'):
                    self.v20 = self.x_shape()
                if(val[1] == '21' or val[3] == '21' or val[5] == '21' or val[7] == '21' or val[9] == '21'):
                    self.v21 = self.x_shape()
                if(val[1] == '22' or val[3] == '22' or val[5] == '22' or val[7] == '22' or val[9] == '22'):
                    self.v22 = self.x_shape()

        # Initializing matrix to store variables
        self.my_matrix_1 = list([self.v00, self.v01, self.v02])
        self.my_matrix_2 = list([self.v10, self.v11, self.v12])
        self.my_matrix_3 = list([self.v20, self.v21, self.v22])

        # Loops to print board along with necessary elements
        for num in range(0, 5):
            for k in range(0, 3):
                for i in self.my_matrix_1[k][num]:
                    print(i, end="")
            print('| ')
        print('-'*40)

        for num in range(0, 5):
            for k in range(0, 3):
                for i in self.my_matrix_2[k][num]:
                    print(i, end="")
            print('| ')
        print('-'*40)

        for num in range(0, 5):
            for k in range(0, 3):
                for i in self.my_matrix_3[k][num]:
                    print(i, end="")
            print('| ')

        # Calling win_func() method that defines winning condition
        self.win_func()


# Function that calls the Tokens() class
def board_details(val, var1, var2, num):
    token1 = Tokens()
    token1.main_conditions(val, var1, var2, num)
