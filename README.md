# INTRODUCTION

This is a Tic Tac Toe game, which was given as an assignment at the Automation and Robotics Club.
The game is written in Python programming language, and makes use of OOP.

# GENERAL STRUCTURE 

## main.py file

- Included user input variables in the defined class, so as to use them throughout the code.
- Required several functions that needed to be called multiple times. Hence included them under the class as methods.
- Allowed easy import actions at necessary places.


_constructor method_: Included some user input variables
*player_1 method*: Used to call a function from tokens.py file
*player_2 method*: Used to call a function from tokens.py file
*incorrect_inputs method*, *repeated_inputs method*: Called multiple times within the Class
*inputs method*: Contains main input code, used to call other methods and variables several times.

## tokens.py file

- Included variables so as to be called multiple times within the code
- Required several functions that needed to be called multiple times. Hence included them under the class as methods.
- Allowed easy import actions at necessary places.


*x_shape*, *o_shape*, *empty_shape methods*: Contains necessary shapes stored as an array
*empty_board method*: Used to print out the empty board
*win_func method*: Contains code for winning condition
*main_conditions method*: Contains main code that prints out the board with necessary shapes in it.


used *sys* module: To exit out of the system after a game

***
