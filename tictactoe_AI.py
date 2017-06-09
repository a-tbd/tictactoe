'''
Tic tac toe game
Played in terminal.  Human player always goes first.
the computer player is 'O'.  

'''

import sys
from copy import deepcopy
from colors import bcolors

PLAYER = {1: 'X', 2: 'O'}

class GameManager(object):
    def __init__(self):
        self.board = Board()
        self.computerAI = None
    
    def set_computerAI(self, computerAI):
        self.computerAI = computerAI
    
    def start(self):
        turn = 1
        while not self.gameover():
            self.board.display_board()
            print 'Player %s\'s turn' % PLAYER[turn]
            if turn == 1:
                print 'Select a move from the board (enter number)'
                move = int(raw_input('-->')) - 1
                while not move in self.board.valid_moves():
                    move = int(self.invalid_move()) - 1
            elif turn == 2:
                move = self.computerAI.determine(self.board, turn)
            self.board.move(move, turn)
            turn = turn % 2 + 1
        self.end_game(turn % 2 + 1)

    def invalid_move(self):
        print 'That is not a valid move.  Please enter a valid move from the board.'
        return (raw_input('-->'))
    
    def gameover(self):
        return self.board.is_win() or not self.board.valid_moves()

    def end_game(self, turn):
        self.board.display_board()
        if self.board.is_win():
            print 'Congratulations player %s !' % PLAYER[turn]
        else:
            print 'Looks like it\'s a tie.'
        
        print 'Do you want to play again? (y/n)'
        restart = raw_input('-->')
        while not restart in ['y', 'n']:
            print 'That is not a valid input.  Do you want to play again? (y/n)'
            restart = raw_input('-->')
        if restart == 'y':
            main()
        else:
            print 'Thanks for playing!'
            sys.exit()

class Board(object):
    def __init__(self):
        self.state = [i for i in range(9)]

    def display_board(self):
        key = [i+1 if isinstance(i, int) 
               else bcolors.OKGREEN + str(i) + bcolors.ENDC if i == 'X'
               else bcolors.FAIL + str(i) + bcolors.ENDC for i in self.state]

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
        self.state[loc] = PLAYER[turn]

    def clone(self):
        board_copy = Board()
        board_copy.state = deepcopy(self.state)
        return board_copy

class ComputerAI(object):
    def __init__(self):
        self.all_moves = {}

    def determine(self, board, turn):
        moves = board.valid_moves()
        self.all_moves = {i: 0 for i in moves}
        move = self.minimax(board, turn, 0)
        if move:
            return move
        else:
            scores = {self.all_moves[i]: i for i in self.all_moves}
            best = max(scores.keys())
            move = scores[best]
        return move
    
    def minimax(self, board, turn, depth):
        moves = board.valid_moves()

        if board.is_win() or not moves:
            return self.evaluate(board)
        
        for move in moves:
            clone = board.clone()
            clone.move(move, turn)
            if depth == 0 and clone.is_win():
                return move
            score = self.minimax(clone, turn % 2 + 1, depth+1)
            if depth == 1:
                if score == 1:
                    self.all_moves[move] += 1
                else:
                    self.all_moves[move] -= 1

    def evaluate(self, board):
        if board.is_win():
            return 1
        else:
            return 0

def main():
    game_manager = GameManager()
    computerAI = ComputerAI() 
    game_manager.set_computerAI(computerAI)
    game_manager.start()

if __name__ == '__main__':
    main()