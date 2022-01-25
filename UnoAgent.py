from typing import List, Tuple
from xmlrpc.client import Boolean
from UnoCard import UnoCard
import random

DIFFICULTY = 1 # Hardcoded difficulty

class UnoAgent:
    def __init__(self, id: int, name: str, isBot: Boolean, cards: List ) -> None:
        self.id = id
        self.name = name
        self.isBot = isBot
        self.cards = cards
        if(isBot):
            self.difficulty = DIFFICULTY
        # self.state ## Bot state
    def setName(self, name: str) -> None:
        self.name = name
    def getCards(self) -> List:
        return self.cards
    def addCards(self, cards: List) -> None:
        self.cards.append(cards)
    def addCard(self, card: UnoCard) -> None:
        self.cards.append(card)
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
        print(self) ## Print the players cards
        if self.isBot is False: ## If not a bot display prompt
            ## TODO: Make a better validation of the input
            while True:
                print("Current card is: " + str(currentCard))
                # print("Previous actions: ")
                # for action in actionsQueue:
                #     print("\t" + str(action))
                try:
                    while True: ## Loop for invalid **number** input
                        movement = input("Insert the number of your selection (Type '?' for help)> ")
                        index = int(movement)
                        selectedCard = self.cards[index] # If this fails, except will be raised
                        if selectedCard == currentCard: ## Validate card can be selected. Remember __eq__ is implemented
                            return self.cards.pop(index)
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
        '''
        Consider that the agent could be modeled in such a way that
        it makes inferences about what cards other players have
        State is not necesary because the agent is always playing when executing this method
        '''
        seq = cardStack ## Sequence of cards
        actions = self.getActions(cardStack[-1], self.cards) ## Actions of the agent: list of indexes
        if actions != []: ## If there are actions that can be performed
            return self.cards.pop(self.getAction(actions)) ## Return the selected card
        else: ## Since there are no possible actions eat a card
            return None
    
    def getActions(self, currentCard: UnoCard, cards: List) -> List:
        '''
        Returns a list of indexes of cards that can be selected to perform the action
        '''
        actions = []
        for i in range(len(cards)):
            if currentCard == cards[i]:
                actions.append(i)
        return actions
    
    def getAction(self, actions: List) -> int:
        '''
        Returns the index of the selected card
        '''
        if self.difficulty == 0:
            return random.choice(actions)
        elif self.difficulty == 1:
            return self.getActionMedium(actions)
        elif self.difficulty == 2:
            return self.getActionHard(actions)
        else:
            print("Invalid difficulty")
            return None
    
    def getActionMedium(self, actions: List) -> int:
        '''
        Returns the index of the selected card
        '''
        if len(actions) == 1:
            return actions[0]
        else:
            return random.choice(actions)
    
    def selectColor(self, cardStack: List) -> str:
        '''
        Returns the color of the selected card

        Note: At the moment this function only handles if self.isBot is True
        but in the future it should handle both cases and the function should return a Color
        selectColor(self, cardStack: List) -> Color
        '''
        return random.choice(["red", "blue", "green", "yellow"])