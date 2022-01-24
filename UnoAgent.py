from typing import List, Tuple
from xmlrpc.client import Boolean
from UnoCard import UnoCard
import random

class UnoAgent:
    def __init__(self, id: int, name: str, isBot: Boolean, cards: List ) -> None:
        self.id = id
        self.name = name
        self.isBot = isBot
        self.cards = cards
    def setName(self, name: str) -> None:
        self.name = name
    def getCards(self) -> List:
        return self.cards
    def addCards(self, cards: List) -> None:
        self.cards.append(cards)
    def addCard(self, card: UnoCard) -> None:
        self.cards.append(card)
    def getCardAt(self, index: int) -> UnoCard:
        return self.cards[index]
    def removeCardAt(self, index: int) -> UnoCard:
        return self.cards.pop(index)
    def getName(self) -> str:
        return self.name
    def __str__(self) -> str:
        string = self.name + "{\n\tid: " + str(self.id) + ",\n\tcards{\n"
        if self.cards != None:
            for card in self.cards: ## TODO: Change to indexed for loop
                string += '\t\t' + str(card) + '\n'
        return string + "\t}\n}"

    def action(self, cardStack: List, actionsQueue: List = None) -> UnoCard:
        if cardStack != []:
            currentCard = cardStack[-1]
        else:
            currentCard = None
        ## Returns selected card or None when there is a withdraw from deck request
        if self.isBot is False: ## If not a bot display prompt
            ## TODO: Make a better validation of the input
            while True:
                print(self) ## Print the players cards
                print("Current card is: " + str(currentCard))
                # print("Previous actions: ")
                # for action in actionsQueue:
                #     print("\t" + str(action))
                try:
                    while True: ## Loop for invalid **number** input
                        movement = input("Insert the number of your selection (Type '?' for help)> ")
                        selectedCard = self.getCardAt(int(movement)) # If this fails, except will be raised
                        if selectedCard == currentCard: ## Validate card can be selected. Remember __eq__ is implemented
                            return selectedCard
                        else: # TODO: Need to move validation of movement to a parser, otherwise I need to use a goto here
                            print("Invalid move, try again!")
                except: ## if a **string** is inputted
                    if(movement == 'g'): # Get card from deck
                        return None ## Bad practice, but it works, so passing None means get card from deck
                    elif(movement == '?'):
                        print("Type on of the following options")
                        for i, card in zip( range(len(self.getCards())), self.getCards() ):
                            print(str(i) + ". " + str(card))
                        print("g. For getting a card from the deck")
                        print("?. For help (You are already seeing this)")
                        input("Press any key to continue >") ## Change this for keyboard Listener https://stackoverflow.com/questions/48787563/press-esc-to-stop-and-any-other-key-to-continue-in-python#48960318
                    else:
                        print("What the heck brah, try again!")
        else:
            return self.move(cardStack)

    def move(self, cardStack: List) -> UnoCard:
        '''Consider that the agent could be modeled in such a way that
           it makes inferences about what cards other players have'''
        # Get set of possible actions
        actions = [] ## Indexes of cards that can be selected to perform the action
        selectedAction  = None
        for i in range(len(self.cards)): ## Search for cards that meet the action criteria
            ## If card is of the same color or same number or is special it is eligable
            if currentCard == self.cards[i]:
                actions.append(i)
        ## Note that in this selection process we do self.cards.append(card) when we select
        ## a card, in order to just pop it from the cards list at the end of the function.
        if actions != None: ## If there are actions that can be performed
            indexSelectedCard = random.choice(actions) ## Select random action
            self.cards.append(self.cards.pop(indexSelectedCard))
        else: ## Since there are not possible actions eat card
            newCard = deck.pop()
            self.cards.append(newCard)
            while currentCard != newCard:
                newCard = deck.pop()
                self.cards.append(newCard)
        # Select a card according to the card
        # Remove that card from the list and return it
        return self.cards.pop()