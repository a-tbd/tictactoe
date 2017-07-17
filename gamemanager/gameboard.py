'''
Board for tictactoe game
'''

from colors import bcolors
from copy import deepcopy


class TicTacToeBoard(object):
    PLAYER = {1: 'X', 2: 'O'}
    def __init__(self):
        self.state = list(range(9))

    def display_board(self):
        """Displays open moves as numbers 1-9, X's as red and O's as green"""
        key = [i+1 if isinstance(i, int) 
               else bcolors.GREEN + str(i) + bcolors.ENDC if i == 'X'
               else bcolors.RED + str(i) + bcolors.ENDC for i in self.state]

        print (' %s | %s | %s \n'
               '-----------   \n'
               ' %s | %s | %s \n'
               '-----------   \n'
               ' %s | %s | %s ') % tuple(key)

    def is_win(self):
        winning_state = [[0,1,2], [3,4,5], [6,7,8], # horizontal
                         [0,3,6],[1,4,7],[2,5,8], # vertical
                         [0,4,8], [2,4,6]] # diagonal
        for w in winning_state:
            plays = set([self.state[i] for i in w])
            if len(plays) == 1:
                return True
        return False

    def valid_moves(self):
        return [i for i in self.state if isinstance(i, int)]

    def move(self, loc, turn):
        self.state[loc] = self.PLAYER[turn]
    
    def clone(self):
        board_copy = deepcopy(self)
        return board_copy

    def reset_board(self):
        self.state = list(range(9))


class ConnectFourBoard(object):
    PLAYER = {1: 'R', 2: 'Y'}
    def __init__(self):
        self.state = list(range(42))

    def display_board(self):
        key = [i+1 if isinstance(i, int) 
               else bcolors.RED + str(i) + bcolors.ENDC if i == 'R'
               else bcolors.YELLOW + str(i) + bcolors.ENDC for i in self.state]

        print_elements = ['%-2s|'*6 + '%-2s']*6

        print '\n'.join(print_elements) % tuple(key)



