import gameboard

class GamePlay(object):
    def __init__(self, computerAI, turn=1, game_on=True):
        self.computerAI = computerAI
        self.board = gameboard.ConnectFourBoard()
        self.turn = turn
        self.game_on = game_on

class ConnectFourManager(GamePlay):
    PLAYER = {1: 'R', 2: 'Y'}
    def __init__(self, computerAI, turn=1, game_on=True):
        GamePlay.__init__(self, computerAI, turn=1, game_on=True)

class TicTacToeManager(GamePlay):
    PLAYER = {1: 'X', 2: 'O'}

    def __init__(self, computerAI, turn=1, game_on=True):
        GamePlay.__init__(self, computerAI, turn=1, game_on=True)
    
    def start(self):
        turn = self.turn

        while self.game_on:
            self.board.display_board()
            print 'Player %s\'s turn' % self.PLAYER[turn]
            if turn == 1:
                print 'Select a move from the board (enter number)'
                move = int(raw_input('-->')) - 1
                while not move in self.board.valid_moves():
                    move = int(self.invalid_move()) - 1
            elif turn == 2:
                move = self.computerAI.determine(self.board, turn)
            self.board.move(move, turn)
            turn = turn % 2 + 1
            if self.gameover():
                turn = self.end_game(turn % 2 + 1)  # TO DO: changes player after each game for tic tac toe.

    def invalid_move(self):
        print 'That is not a valid move.  Please enter a valid move from the board.'
        return (raw_input('-->'))
    
    def gameover(self):
        return self.board.is_win() or not self.board.valid_moves()

    def end_game(self, turn):
        self.board.display_board()
        if self.board.is_win():
            print 'Congratulations player %s !' % self.PLAYER[turn]
        else:
            print 'Looks like it\'s a tie.'
        
        print 'Do you want to play again? (y/n)'
        restart = raw_input('-->')
        while not restart.lower() in ['y', 'n']:
            print 'That is not a valid input.  Do you want to play again? (y/n)'
            restart = raw_input('-->')
        if restart == 'y':
            self.board.reset_board()
            return self.turn  # shouldn't return either a value or a boolean from same function...
        else:
            print 'Thanks for playing!'
            self.game_on = False    ### QUESTION : is it bad to change attributes like this in modules?
