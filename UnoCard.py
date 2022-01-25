from Utilities import *;

class UnoCard:
    def __init__(self, number: int, color: Color, special: Special ) -> None:
        self.color = color
        self.number = number
        self.special = special
    def setColor(self, color: Color) -> None:
        self.color = color
    def __eq__(self, __o: object) -> bool:
        ## If card is of the same color or same number or is special or is None is eligable
        ## TODO: Check this logic later
        if (__o is None) or (__o.color is not None and __o.color == self.color) or (__o.number is not None and __o.number == self.number) or (__o.special is not None and __o.special == self.special) or (self.special == Special.colorChange or self.special == Special.plusFour):
            return True
        return False
    def __str__(self) -> str:
        return  "UnoCard{ color: " + self.color.name + ((",\tnumber: " + str(self.number)) if self.number != None else "") + ((",\tspecial: " + self.special.name) if self.special != None else "") + " }"