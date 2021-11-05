
"""
    Main class - Entry point that is responsible for creating players, deck of cards, shuffling and
    distributing the cards among players
"""


class Main:
    TITLE_PLAYER_ONE = 'Player-1'
    TITLE_PLAYER_TWO = 'Player-2'
    # Holds instance of Player-1
    player_one = None
    # Holds instance of Player-2
    player_two = None
    # Holds instance of the player that wins the game
    winner = None
    deck = None
    is_game_on = False
    is_war = False
    is_draw = False
    # Variable keep tracks of no. of war scenarios occured during the gameplay
    total_wars = 0

    def __init__(self):
        pass

    # This function increases the war counter when ever the war scenario occurs (Keep tracks of war count)
    def track_wars(self):
        self.total_wars += 1

    # Entry point that kick starts the game
    def start(self):
        pass

    # Function to create two player using the given player names
    def create_players(self, player_one_name, player_two_name):
        pass

    # Function creates instances of cards (52) and adds to the deck array - uses a builder design pattern
    def initialize_deck(self):
        pass

    # Function starts the gameplay once deck and players are initialized
    def start_game(self):
        pass


if __name__ == '__main__':
    Main().start()
