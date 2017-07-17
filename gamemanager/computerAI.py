'''

'''

import random

class ComputerAI(object):
    pass


class EasyAI(ComputerAI):
    def __init__(self):
        ComputerAI.__init__(self)
    
    def determine(self, board, turn):
        """Takes board as list, returns a random move as integer."""
        moves = board.valid_moves()
        next_move = random.randint(0,8)
        while not next_move in moves:
            next_move = random.randint(0,8)
        return next_move


class HardAI(ComputerAI):
    def __init__(self):
        self.all_moves = {}
        ComputerAI.__init__(self)

    def determine(self, board, turn):
        """
        Takes board as list. Takes winning move if available.
        Else makes the move that will result in the most ways to win.
        """  
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
        """
        Evaluates all possible moves given the current board (list).
        For each move, performs a recursive search until a win, tie, or loss is reached.
        Returns the resulting score (1 for win, 0 for tie or loss).
        """
        moves = board.valid_moves()

        if len(moves) == 9:
            return 4
        elif board.is_win() or not moves:
            return self.evaluate(board)
        
        for move in moves:
            # instead of having a function just have
            # clone = deepcopy(board) or whatever

            # however!  lots of clones.  instead of doing that.
            # make the move, check what you need to check
            # then have a reverse the move function (undo)
            # so you're just using one board  
            ##### QUESTION: Would I need to clone the board if there was a left/right recursion or something?
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
