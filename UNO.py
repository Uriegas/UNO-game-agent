from UnoGame import *

## Globals
colors = [ Color.red, Color.blue, Color.green, Color.yellow ]
specials = [Special.blockNextPlayer, Special.plusTwo, Special.reverse]
cards = []

## ---------------- Initialize cards array ----------------
## Cards from 0 to 9, 4 colors
for number in range(0, 9):
    for color in colors:
        cards.append(UnoCard(number, color, None))

## Cards from 1 to 9, 4 colors
for number in range(1, 9):
    for color in colors:
        cards.append(UnoCard(number, color, None))


## Special Cards, 3 special cards 2 times each color = 3 x 2 x 4 = 24 cards
for special in specials:
    for color in colors:
        cards.append(UnoCard(None, color, special))
        cards.append(UnoCard(None, color, special))

## Add +4 and color change cards for each color : 8 cards
for color in colors:
    cards.append(UnoCard(None, color, Special.plusFour))
    cards.append(UnoCard(None, color, Special.colorChange))


## ---------------- Start UNO game ----------------
game = UnoGame(cards, playersNames=["Maquina de Fuego", "Eduardo"], cardsPerPlayer=8)
game.start()
# print(game)