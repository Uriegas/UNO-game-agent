from UnoGame import *

## In this file we define the configuration of the game:
## * How many cards there are?
## * How many players there are?
## * How many player bots there are?

## This configuration is static but can be done dinamically with further programming

## Current game configuration
colors = [ Color.red, Color.blue, Color.green, Color.yellow ] ## Card colors
specials = [Special.blockNextPlayer, Special.plusTwo, Special.reverse] ## Special powers
numbers = range(0, 10) # Numbers of the cards
players = [("Maquina de Fuego", True), ("Eduardo", False)] ## List with name and isBot of players
cards = [] ## Array of cards

## ---------------- Initialize cards array ----------------
## Cards from 0 to 9, 4 colors
for number in numbers:
    for color in colors:
        cards.append(UnoCard(number, color, None))

## Cards from 1 to 9, 4 colors
for number in numbers[1:]:
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
game = UnoGame(cards, playersNames=players, cardsPerPlayer=8)
game.start()