from typing import List
from UnoAgent import UnoAgent
from UnoCard import UnoCard
from Utilities import *;
import random

class UnoGame:
    def __init__(self, deck, playersNames: List, cardsPerPlayer: int) -> None:
        self.deck = deck # The bunch of cards in the game
        self.players = []
        self.currentCard = None
        self.winner = None

        random.shuffle(self.deck) # Shuffle cards

        # Set players cards
        # TODO: Program fails if cardsPerPlayer or numberPlayers are so big
        for name in playersNames:
            self.players.append( UnoAgent(id=random.randint(1, 1000), name=name, cards=[self.deck.pop() for i in range(cardsPerPlayer)]) )


    def start(self) -> None:
        print("           )     )   ")
        print("        ( /(  ( /(   ")
        print("    (   )\()) )\())  ")
        print("    )\ ((_)\ ((_)\   ")
        print(" _ ((_) _((_)  ((_)  ")
        print("| | | || \| | / _ \  Welcome to UNO GAME from terminal.")
        print("| |_| || .` || (_) | You are playing against a machine.")
        print(" \___/ |_|\_| \___/\n")

        while( self.winner is None ):
            # Print environment
            for player in self.players:
                print(player)
            print("Current card is: " + str(self.currentCard))
            movement = input("Your turn (Type '?' for help)> ")
            try:
                selectedCard = self.players[i].getCardAt(int(movement))
                if selectedCard == self.currentCard: ## Validate card can be selected
                    self.currentCard = selectedCard
                else: # TODO: Need to move validation of movement to a parser, otherwise I need to use a goto here
                    print("Your movement is not valid, please make a valid one.")
            except:
                if(movement == 'g'): # Get card from deck
                    self.players[1].addCard(self.deck.pop())
                elif(movement == '?'):
                    print("Type on of the following options")
                    for i, card in zip( range(len(self.players[1].getCards())), self.players[1].getCards() ):
                        print(str(i) + ". " + str(card))
                    print("g. For getting a card from the deck")
                    print("?. For help (You are already seeing this)")
                    input("Press any key to continue >") ## Change this and add a keyboard Listener https://stackoverflow.com/questions/48787563/press-esc-to-stop-and-any-other-key-to-continue-in-python#48960318
                else:
                    print("Invalid move, try again!")
            
            # Machine plays
            self.currentCard, self.deck = self.players[0].move(self.currentCard, self.deck)

            for player in self.players:
                if(len(player.getCards()) == 0):
                    self.winner = player
                    break
        
        print(self.winner.getName() + " wins!")
        print("Chika chika yeah!")

    
    def __str__(self) -> str:
        string = "UNO GAME\n"
        string += "UNO CARDS:\n"
        for card in self.deck:
            string += str(card) + '\n'
        string += "UNO players:\n"
        for player in self.players:
            string += str(player) + '\n'
        return string
