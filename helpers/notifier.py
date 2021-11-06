
class Notifier:

    @staticmethod
    def fire(msg):
        print(msg)

    @staticmethod
    def notify_card_drawn(title, player, card):
        Notifier.fire(f'\n {title}:{player.get_player_name()} drew card {card.show()}')

    @staticmethod
    def notify_game_winner(title, winner):
        Notifier.fire(f'\n {title}:{winner.get_player_name()} Won the game !!')

    @staticmethod
    def notify_round_winner(title, round_count, winner, loser):
        Notifier.fire(f'\n {title}:{winner.get_player_name()} Won Round - {round_count}')
        Notifier.notify_round_stats(winner, loser)

    @staticmethod
    def notify_round_stats(winner, loser):
        Notifier.fire(f'\n Round Stats:\t \t {winner.get_player_name()} Has {winner.player_cards_count()} cards '
                      f'\t | \t \t {loser.get_player_name()} Has {loser.player_cards_count()} cards \n')

    @staticmethod
    def notify_match_draw():
        Notifier.fire('\n\n It\'s a draw !!')

    @staticmethod
    def declare_war():
        Notifier.fire('\n It\'s War !!! \n')

    @staticmethod
    def notify_game_stats(rounds, wars, winner):
        Notifier.fire(f'\n\n-----------------------------------------------------------------------')
        Notifier.fire(f' GAME STATS: Rounds Played: {rounds} \t |'
                      f' \t Total Wars: {wars} \t |' 
                      f' \t Winner: {winner.get_player_name()} won the game !!')
        Notifier.fire(f'\n -------------------------------------------------------------------------')

