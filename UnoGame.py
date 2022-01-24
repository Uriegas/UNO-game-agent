from typing import List

from UnoAgent import UnoAgent
from Utilities import *;
import random

class UnoGame:
    def __init__(self, deck, playersConfig: List, cardsPerPlayer: int) -> None:
        self.deck = deck # The bunch of cards in the game
        self.players = [] # List of players in the game
        # self.currentCard = None # Deprecated
        self.winner = None # Set to None if there is no winner yet
        self.cardStack = [] # Stack of cards that had been played

        random.shuffle(self.deck) # Shuffle cards

        # Set players cards
        # TODO: Program fails if cardsPerPlayer or numberPlayers are so big
        for config in playersConfig:
            self.players.append( UnoAgent(id=random.randint(1, 1000), name=config[0], isBot=config[1], cards=[self.deck.pop() for i in range(cardsPerPlayer)]) )

    def start(self) -> None:
        print("           )     )   ")
        print("        ( /(  ( /(   ")
        print("    (   )\()) )\())  ")
        print("    )\ ((_)\ ((_)\   ")
        print(" _ ((_) _((_)  ((_)  ")
        print("| | | || \| | / _ \  Welcome to UNO GAME from terminal.")
        print("| |_| || .` || (_) | You are playing against a machine.")
        print(" \___/ |_|\_| \___/\n")
        while self.winner is None:
            print(self.players[0]) # Verbose
            self.play() ## In special cards we change the players array inside the board method call.
            self.players.append( self.players.pop(0) ) ## This is the change of player turn
        self.printWinner()

    def play(self) -> None:
        ## The player plays
        player = self.players[0] ## This creates a pointer not a copy
        # An action is performed by the given player
        card = player.action(self.cardStack) ## TODO: Add more parameters to this function
        if card is not None:
            self.cardStack.append(card) ## Add card to the stack
            if card.special is not None: ## Is a special action
                if card.special == Special.plusTwo:
                    self.requestAdd(2)
                elif card.special == Special.plusFour:
                    self.colorChangePrompt()
                    self.requestAdd(4)
                elif card.special == Special.colorChange:
                    self.colorChangePrompt()
                elif card.special == Special.reverse:
                    tmp = self.players[1:]
                    tmp.reverse()
                    self.players = [self.players[0]] + tmp
                elif card.special == Special.blockNextPlayer:
                    self.players.append( self.players.pop(0) ) # As if the next player had played
        else:## Is a card request petition
            newCard = self.deck.pop()
            print( player.name + " your new card is: " + str(newCard) )
            player.addCard(newCard)


    def printWinner(self) -> None:
        print("The winner is: " + self.winner.name)
        print("Chika chika yeah!")
    
    def colorChangePrompt(self) -> None:
        ## The color of the special card changes to the selected one
        currentCard = self.cardStack[-1]
        while True: ## Ugliest code ever
            selection = input("Choose new color (red, green, blue, yellow)> ")
            if selection == "red":
                currentCard.setColor( Color.red )
                break
            elif selection == "green":
                currentCard.setColor( Color.green )
                break
            elif selection == "blue":
                currentCard.setColor( Color.blue )
                break
            elif selection == "yellow":
                currentCard.setColor( Color.yellow )
                break
            else:
                print("Invalid color, please type a valid one.")
    
    def __str__(self) -> str:
        string = "UNO GAME\n"
        string += "UNO CARDS:\n"
        for card in self.deck:
            string += str(card) + '\n'
        string += "UNO players:\n"
        for player in self.players:
            string += str(player) + '\n'
        return string
    
    ## NEED TO TEST THIS CODE
    def requestAdd(self, number: int) -> None:
        ## The current player requests to add a number of cards to the next player
        nextPlayer = self.players[1] ## Guaranteed that there at list 2 players
        nextPlayer.addCard(self.deck.pop() for i in range(number))
        ## This is faster than using pop()
        # selectedCards = self.deck[-number:]
        # del self.deck[-number:]
        # nextPlayer.addCards(selectedCards)