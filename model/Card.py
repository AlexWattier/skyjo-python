import string

from model.VisibilityCard import VisibilityCard


class Card:

    def __init__(self, *args):
        if isinstance(args[0], int):
            self.value = args[0]
            self.visibility = args[1]
        elif isinstance(args[0], Card):
            tmp: Card = args[0]
            self.value = tmp.getValue()
            self.visibility = tmp.getVisibility()

    def getValue(self) -> int:
        return self.value

    def getVisibility(self) -> VisibilityCard:
        return self.visibility

    def setVisibility(self, visibility: VisibilityCard):
        self.visibility = visibility

    def isHidden(self) -> bool:
        return self.getVisibility() == 0

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o)

    def __str__(self) -> str:
        mot: string
        mot = "{ " + str(self.value) + "," + str(self.visibility.name) + "}"
        return mot
