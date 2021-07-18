# I HAVE NOT IMPORTED THIS FILE ANYWHERE
# JUST A PRACTICE PROGRAM TO CREATE X, O AND THE EMPTY BOARD USING LOOPS INSTEAD OF A NORMAL LIST

import numpy as np


class Board():

    def __init__(self):
        pass

    def x_func(self):

        for i in range(0, 5):
            #print(' | ',end="")

            for j in [0, 2, 4, 6, 8]:
                if((2*i - 1) < j < (2*i + 1)):
                    print('xx', end="")

                elif((7 - 2*i) < j < (9 - 2*i)):
                    print('xx', end="")

                else:
                    print("  ", end="")

            print('')

    def o_func(self):

        for i in range(0, 3):

            # print('|',end="")

            for j in [0, 1, 3, 5, 7, 8]:

                if((1 - i) < j <= (4 - 2*i)):
                    print('oo', end="")

                elif((3 + 2*i) < j <= (5 + 2*i)):
                    print('oo', end="")

                else:
                    print('  ', end="")

            print('')

        for i in range(0, 2)[::-1]:

            # print('|',end="")

            for j in [0, 1, 3, 5, 7, 8]:

                if((1 - i) < j <= (4 - 2*i)):
                    print('oo', end="")

                elif((3 + 2*i) < j <= (5 + 2*i)):
                    print('oo', end="")

                else:
                    print('  ', end="")

            print('')

    def board_func(self):

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


board = Board()
board.x_func()
print()
board.o_func()
print()
board.board_func()
print()
