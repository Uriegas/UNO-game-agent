from typing import List, Tuple

from UnoCard import UnoCard
import random


class UnoAgent:
    def __init__(self, id: int, name: str, cards: List ) -> None:
        self.id = id
        self.name = name
        self.cards = cards
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
        for card in self.cards:
            string += '\t\t' + str(card) + '\n'
        return string + "\t}\n}"
    def move(self, currentCard: UnoCard, deck: List) -> Tuple:
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
        else: ## Since there are not possible actions keep eating cards until match
            newCard = deck.pop()
            self.cards.append(newCard)

            while currentCard != newCard:
                newCard = deck.pop()
                self.cards.append(newCard)

        # Select a card according to the card
        # Remove that card from the list and return it
        return self.cards.pop(), deck