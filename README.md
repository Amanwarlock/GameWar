
# WAR OF CARDS

War of Cards - A Python project based on the game of cards

## Overview

The game "War of Cards" is played between two players. There are 52 cards that are shuffled and distributed evenly among the two players, such that each player has 26 cards. The game is played until one of the players runs out of the cards. The player that acquires all the cards is declared the winner. Each player draws a card in turns, and the cards are compared based on their ranks. Suits are ignored in this game variant. The player with the card bearing the highest rank wins the particular round. In case the cards played by both the players have the same rank, then it's "War". When War arises, each player draws three cards face-down and then finally draws the 4th card face-up. The result of the War case is decided based on the rank of the 4th card that is drawn face-up. The player whose 4th card rank is highest wins the War round and collects all the cards played on the deck. 

## Assumptions

This section outlines the assumptions and corner cases considered during the implementation. The following assumptions are made in the design:

1. Cards are compared based on ranks, and suits are ignored
2. The game always starts with Player-1 (In current flow, Player-1 is always picked to start first)
3. The game continues as long as both the players have sufficient cards
4. The player that runs out of all cards first loses the game
5. If both players run out of cards simultaneously, then its a draw
6. The player drawing the card with the highest rank wins the particular round
7. When both players draw cards with the same ranks, it's considered War
8. In the case of War, each player draws three cards face-down and one card face-up
9. The result of the War is decided based on the rank of the 4th card drawn face-up

### Corner Cases

Case-1: In a particular round, both players have no cards
- The game results in a draw

Case-2: In a round, Player-1 has cards, and Player-2 has zero cards
- Player-1 wins the game

Case-3: In a round, Player-2 has cards, and Player-1 has zero cards
- Player-2 wins  the game

Case-4: Player-1 draws a card with suit Diamonds and rank Jack; Player-2 draws a card with suit Spades and rank Ace
- Player-2 wins the round (suits are ignored)

Case-5: Both players 1 and 2 draw cards with the same ranks
- War is declared
- Each player draws three cards face-down and one card face-up

Case-6: Repeated Wars in subsequent rounds
- The game continues until any one player runs out of all cards

Case-7: In a War round scenario, both players have exactly four cards each
- Since both the players have sufficient cards (minimum of 4) to draw three cards face-down and one card face-up the round continues

Case-8: In a War round scenario, Player-1 has three cards, and Player-2 has more than four cards
- Since Player-1 does not have sufficient cards to draw three face-down cards and a face-up card, it is the first player to run out of cards
- Therefore Player-1 loses the game and must surrender all the cards to Player-2
- Player-2 wins the game

Case-9: In a War scenario, Player-2 has three cards, and Player-1 has more than four cards
- In this case, Player-2 is the first player that runs out of cards
- Hence, Player-1 is the winner, and Player-2 must surrender all the cards to Player-1

Case-10: In a War scenario,  Player-1 has three cards, and Player-2 has one card
- Since Player-1 is the first player to run out of cards, it loses the game regardless of which player has the least number of cards
- Player-1 must surrender all cards to Player-2
- Player-2 wins the game

## Technical Specification

| Programming Language | Version |
| ------ | ------ |
| Python | 3.8.5 |


## Future Scope

This section highlights the potential improvements in the design architecture for further iterations. The improvements are categorized into three divisions, and they are as follows:
1. Design
2. User Experience
3. Test Coverage

From the design perspective, in the current version, the design uses a queue implemented using stacks. As the cards are issued in the FIFO order, the queue is an ideal data structure. For better performance, the queue can be implemented using Linked List in future revisions. In addition, the design uses a notification module to log game and round information on the screen. This module uses hard coded messages appending parameters dynamically. All these messages can be defined as templates in a separate dedicated file and can be read accordingly by the notification module. The advantage it offers is that, apart from modularity, in the future, when the messages need to be changed, the business logic need not be modified. Only modifying the message templates should be enough. Moreover, the current version does not handle any exceptions or throw custom errors. For graceful handling of exceptions and avoiding abrupt program termination, the code should implement exception handling.

Secondly, from the user experience point of view, the program chooses Player-1 to start the game by default. Logic can be implemented to decide which player can begin with the help of the user’s participation and interaction. Furthermore, different colors can be used for logging the messages to the console for better accessibility.   

Lastly, efforts can be made to enhance the test coverage by adding more use cases. The code is modular enough to test each functionality. The core functionality needs to be covered with additional scenarios to improve the quality of the code. 

## References

1. https://www.pagat.com/war/war.html
2. https://en.wikipedia.org/wiki/War_(card_game)


