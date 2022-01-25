from typing import List, Tuple
from UnoCard import UnoCard
import random
from Utilities import *

DIFFICULTY = 0 # Hardcoded difficulty

class UnoAgent:
    def __init__(self, id: int, name: str, isBot: bool, cards: List ) -> None:
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
            return self.cards.pop(self.getAction(actions, cardStack)) ## Return the selected card
        else: ## Since there are no possible actions eat a card
            return None
    
    def getActions(self, currentCard: UnoCard, cards: List) -> List:
        '''
        Returns a list of indexes of cards that can be selected to perform the action
        '''
        actions = []
        for i in range(len(cards)):
            if cards[i] == currentCard:
                actions.append(i)
        return actions
    
    def getAction(self, actions: List, cardStack: List ) -> int:
        '''
        Returns the index of the selected card
        '''
        if self.difficulty == 0:
            return self.getActionEasy(actions)
        elif self.difficulty == 1:
            return self.getActionMedium(actions, cardStack)
        else: ## Should never execute
            print("Invalid difficulty")
            return None
    
    def getActionEasy(self, actions: List) -> int:
        '''
        Returns the index of the selected card
        '''
        return random.choice(actions)
    
    def getActionMedium(self, actions: List, cardStack: List) -> int:
        '''
        Returns the index of the selected card
        '''
        if len(actions) == 1:
            return actions[0]
        else:
            actionsCards = []
            for action in actions:
                actionsCards.append(self.cards[action])
            # Count how many cards of each color there are in the stack
            colorsCounter = [0, 0, 0, 0] # Red, Blue, Green, Yellow
            for card in self.cards:
                if card.color == Color.red:
                    colorsCounter[0] += 1
                elif card.color == Color.blue:
                    colorsCounter[1] += 1
                elif card.color == Color.green:
                    colorsCounter[2] += 1
                elif card.color == Color.yellow:
                    colorsCounter[3] += 1

            # Special cards have more weight
            actionsWeight = []
            for action in actionsCards:
                actionsWeight.append(0)
                if action.special is not None:
                    if action.special == Special.plusFour or action.special == Special.colorChange:
                        actionsWeight[-1] += 2
                    if action.special == Special.plusTwo:
                        actionsWeight[-1] += 1
                    if action.special == Special.reverse or action.special == Special.blockNextPlayer:
                        actionsWeight[-1] += 0.5
                ## The greater the cards of a color in the stack, the more weight it has
                ## Because is less probable that other players have a color that has been already played
                if action.color == Color.red:
                    actionsWeight[-1] += colorsCounter[0] / 25
                elif action.color == Color.blue:
                    actionsWeight[-1] += colorsCounter[1] / 25
                elif action.color == Color.green:
                    actionsWeight[-1] += colorsCounter[2] / 25
                elif action.color == Color.yellow:
                    actionsWeight[-1] += colorsCounter[3] / 25
            
            maxAction = max(actionsWeight)
            # Find index of max weight
            return actions[actionsWeight.index(maxAction)]
    
    def selectColor(self, cardStack: List) -> str:
        '''
        Returns the color of the selected card

        Note: At the moment this function only handles if self.isBot is True
        but in the future it should handle both cases and the function should return a Color
        selectColor(self, cardStack: List) -> Color

        Note: There is misleading counting here since the special cards had a random color value
        '''
        colors = ["red", "blue", "green", "yellow"]
        if self.difficulty == 0:
            return random.choice(colors)
        elif self.difficulty == 1:
            colorsCounter = [0, 0, 0, 0]
            for card in cardStack:
                if card.color == Color.red:
                    colorsCounter[0] += 1
                elif card.color == Color.blue:
                    colorsCounter[1] += 1
                elif card.color == Color.green:
                    colorsCounter[2] += 1
                elif card.color == Color.yellow:
                    colorsCounter[3] += 1
            maxColor = max(colorsCounter)
            ## Find index of max color
            return colors[colorsCounter.index(maxColor)]