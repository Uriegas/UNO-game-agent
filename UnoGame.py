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
        while self.winner is None or len(self.deck) > 0:
            self.play() ## In special cards we change the players array inside the board method call.
            if self.players[0].cards == []: ## If the player has no cards left, he's the winner
                self.winner = self.players[0]
            self.players.append( self.players.pop(0) ) ## This is the change of player turn
        self.printWinner()

    def play(self) -> None:
        ## The player plays
        player = self.players[0] ## This creates a pointer not a copy
        # An action is performed by the given player
        card = player.action(self.cardStack) ## TODO: Add more parameters to this function
        if card is not None:
            self.cardStack.append(card) ## Add card to the stack
            print(player.name + " selected card: " + str(card))
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
        if self.winner is None:
            print("Draw: There is no winner")
        else:
            print("The winner is: " + self.winner.name)
        print("Chika chika yeah!")
    
    def colorChangePrompt(self) -> None:
        """
        TODO: Change this function so that I have something like
        selection = self.players[0].selectColor(self.cardStack) -> Color

        It should return the color and the IO should be hidden in the UnoAgent class
        """
        ## The color of the special card changes to the selected one
        currentCard = self.cardStack[-1]
        while True: ## Ugliest code ever
            if self.players[0].isBot:
                selection = self.players[0].selectColor(self.cardStack)
            else:
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
        print(self.players[0].name + " selected color: " + str(currentCard.color))
    
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
        for i in range(number):
            nextPlayer.addCard( self.deck.pop() )
        ## This is faster than using pop()
        # selectedCards = self.deck[-number:]
        # del self.deck[-number:]
        # nextPlayer.addCards(selectedCards)