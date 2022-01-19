import enum

# Colors of the cards
class Color(enum.Enum):
    red = 1
    blue = 2
    green = 3
    yellow = 4

# Special powers in the game of UNO
# Plus Two = add 2 cards to next player
# Plus Four = add 4 cards to next player and change color
# Color Change = change the next card color
# Reverse = change the direction flow of the game
# Block Next Player = Next immediate player doesn't play
class Special(enum.Enum):
    plusTwo = 1
    plusFour = 2
    colorChange = 3
    reverse = 4
    blockNextPlayer = 5