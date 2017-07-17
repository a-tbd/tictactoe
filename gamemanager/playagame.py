'''
Game Manager for all available available games (currently only tictactoe)

TODO:
- add a new game (connectfour)
'''

import computerAI
import gameboard
import pdb
import games


class GameManager(object):
    AVAIL_GAMES = {'tictactoe': ['X', 'O'], 'connectfour': ['red', 'yellow']}

    def __init__(self):
        pass
    
    def start(self):
        game = self.choose_game()
        level = self.choose_level() 
        player = self.choose_player(game)
        player_num = self.AVAIL_GAMES[game].index(player.upper()) + 1
        
        if game == 'tictactoe':
            if level == 'easy':
                compAI = computerAI.TicTacToeEasyAI()
            else:
                compAI = computerAI.TicTacToeHardAI()
            g = games.TicTacToeManager(compAI, player_num)
        elif game == 'connectfour':
            compAI = computerAI.ConnectFourAI()
            g = games.ConnectFourManager()
        g.start()
    
    def choose_game(self):
        print 'Welcome!  What game would you like to play?  (tictactoe or connectfour)'
        game = raw_input('-->')
        while not game in self.AVAIL_GAMES.keys():
            print 'Sorry, that\'s not a valid choice.  Choose again. (tictactoe or connectfour)'
            game = raw_input('-->')
        return game

    def choose_level(self):
        while True:
            print 'Select a level of play: easy or hard'
            level = raw_input('-->')
            if not level.lower() in ['easy', 'hard']:
                print 'That is not a valid choice.'
            else:
                return level

    def choose_player(self, game):
        turn_options = self.AVAIL_GAMES[game]
        while True:
            print 'Would you like to be %s or %s?' % tuple(turn_options)
            turn_choice = raw_input('-->')
            if not turn_choice.upper() in self.AVAIL_GAMES[game]:
                print 'That is not a valid choice.'
            else:
                return turn_choice


def main():
    game_manager = GameManager()
    game_manager.start()

if __name__ == '__main__':
    main()