from enum import Enum


class NextPlayer(Enum):
    PLAYERONE = ('Player_1', 1)
    PLAYERTWO = ('Player_2', 2)

    def __new__(self, *args):
        if args[0] is not None:
            self.num = args[0]
            if args[1] is not None:
                self.name = args[1]
        return self

    def getNumPlayer(self):
        return self.num

    def getNamePlayer(self):
        return f'{self.name} -> {self.name}'
