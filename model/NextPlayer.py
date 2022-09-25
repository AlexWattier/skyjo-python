from enum import Enum


class NextPlayer(Enum):
    PLAYERONE = ('Player_1', 1)
    PLAYERTWO = ('Player_2', 2)

    def __new__(cls, *args):
        if args[0] is not None:
            cls.num = args[0]
            if args[1] is not None:
                cls.name = args[1]
        return cls

    def getNumPlayer(self):
        return self.num

    def getNamePlayer(self):
        return f'{self.name} -> {self.name}'
