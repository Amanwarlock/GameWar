from classes.deck import Deck
from classes.player import Player
from helpers.notifier import Notifier
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
        Notifier.fire('\n \t\t\t\tLet\'s Play WAR of Cards !')
        player_one_name = input('\nEnter Player-1 name: ')
        player_two_name = input('\nEnter Player-2 name: ')
        self.create_players(player_one_name, player_two_name)
        self.initialize_deck()
        self.start_game()
        Notifier.notify_game_stats(self.deck.round, self.total_wars, self.winner)

    # Function to create two player using the given player names
    def create_players(self, player_one_name, player_two_name):
        self.player_one = Player(player_one_name)
        self.player_two = Player(player_two_name)
        Notifier.fire(f'\n\n Players Created! \n\n Welcome {self.player_one.get_player_name()} and '
                      f'{self.player_two.get_player_name()} onboard !\n')

    # Function creates instances of cards (52) and adds to the deck array - uses a builder design pattern
    def initialize_deck(self):
        self.deck = Deck()
        self.deck.build_deck().distribute(self.player_one, self.player_two)

    # Function starts the gameplay once deck and players are initialized
    def start_game(self):
        self.is_game_on = True

        while self.is_game_on:
            self.deck.inc_round()
            Notifier.fire(f'------------------ ROUND - {self.deck.round} -----------------------')

            if self.player_one.player_cards_count() == 0 and self.player_two.player_cards_count() > 0:
                Notifier.notify_game_winner(self.TITLE_PLAYER_TWO, self.player_two)
                self.winner = self.player_two
                self.is_game_on = False
                break

            if self.player_two.player_cards_count() == 0 and self.player_one.player_cards_count() > 0:
                Notifier.notify_game_winner(self.TITLE_PLAYER_ONE, self.player_one)
                self.winner = self.player_one
                self.is_game_on = False
                break

            if self.player_one.player_cards_count() == 0 and self.player_two.player_cards_count() == 0:
                Notifier.notify_match_draw()
                self.is_draw = True
                self.is_game_on = False
                break

            player_one_card = self.player_one.draw_one()
            player_two_card = self.player_two.draw_one()

            Notifier.fire(f'\n')
            Notifier.notify_card_drawn(self.TITLE_PLAYER_ONE, self.player_one, player_one_card)
            Notifier.notify_card_drawn(self.TITLE_PLAYER_TWO, self.player_two, player_two_card)

            result = player_one_card.compare(player_two_card)

            if result == 1:
                self.player_one.add_cards([player_one_card, player_two_card])
                Notifier.notify_round_winner(self.TITLE_PLAYER_ONE, self.deck.round, self.player_one, self.player_two)
            elif result == -1:
                self.player_two.add_cards([player_two_card, player_one_card])
                Notifier.notify_round_winner(self.TITLE_PLAYER_TWO, self.deck.round, self.player_two, self.player_one)
            else:
                self.is_game_on = self.on_war(player_one_card, player_two_card)

    def on_war(self, player_one_card, player_two_card):
        self.is_war = True

        while self.is_war:

            Notifier.declare_war()
            self.track_wars()

            if self.player_one.player_cards_count() < 4:
                Notifier.notify_game_winner(self.TITLE_PLAYER_TWO, self.player_two)
                self.winner = self.player_two
                self.is_war = False
                return False

            if self.player_two.player_cards_count() < 4:
                Notifier.notify_game_winner(self.TITLE_PLAYER_ONE, self.player_one)
                self.winner = self.player_one
                self.is_war = False
                return False

            player_one_card_pool = [player_one_card]
            player_two_card_pool = [player_two_card]

            player_one_card_pool.extend(self.player_one.draw_many(3))
            Notifier.fire(f'{self.player_one.get_player_name()} drew three cards face-down')

            player_two_card_pool.extend(self.player_two.draw_many(3))
            Notifier.fire(f'{self.player_two.get_player_name()} drew three cards face-down')

            player_one_card = self.player_one.draw_one()
            Notifier.fire(
                f'Player-1: {self.player_one.get_player_name()} drew one card face-up {player_one_card.show()}')

            player_two_card = self.player_two.draw_one()
            Notifier.fire(
                f'Player-2: {self.player_two.get_player_name()} drew one card face-up {player_two_card.show()}')

            result = player_one_card.compare(player_two_card)

            if result == 1:
                player_one_card_pool.append(player_one_card)
                player_two_card_pool.append(player_two_card)
                player_one_card_pool.extend(player_two_card_pool)
                self.player_one.add_cards(player_one_card_pool)
                self.is_war = False
                Notifier.notify_round_winner(self.TITLE_PLAYER_ONE, self.deck.round, self.player_one,
                                             self.player_two)
            elif result == -1:
                player_one_card_pool.append(player_one_card)
                player_two_card_pool.append(player_two_card)
                player_two_card_pool.extend(player_one_card_pool)
                self.player_two.add_cards(player_two_card_pool)
                self.is_war = False
                Notifier.notify_round_winner(self.TITLE_PLAYER_TWO, self.deck.round, self.player_two,
                                             self.player_one)
            else:
                continue

        return True


if __name__ == '__main__':
    Main().start()
