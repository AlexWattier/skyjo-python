from model.VisibilityCard import VisibilityCard
from model.Card import Card
import random


class Player:
    scorePlayer: int
    Player = None

    def __init__(self):
        self.handPlayer = []
        self.scorePlayer: int = 0

    def getScorePlayer(self) -> int:
        return self.scorePlayer

    def getHandPlayer(self) -> list:
        return self.handPlayer

    def adCard(self, card: Card):
        self.handPlayer.append(card)

    def scorePlayer(self):
        scorePlayer: int = 0
        handTemp = self.handPlayer.copy()
        for _ in handTemp:
            cardTmp: Card = handTemp.pop(0)
            if cardTmp.getVisibility() == VisibilityCard.nothide:
                scorePlayer = scorePlayer + cardTmp.getValue()

        self.scorePlayer = scorePlayer

    def getCard(self, index: int) -> Card:
        return self.handPlayer[index]

    def hitCardPlayer(self):
        randomNum = []
        for i in range(0, 12):
            randomNum.append(i)
        random.shuffle(randomNum)
        for j in range(0, 2):
            self.setCardVisibility(randomNum.pop())

    def setCardVisibility(self, nbCard: int):
        self.getCard(nbCard).setVisibility(VisibilityCard.nothide)

    def beats(self, player) -> bool:
        return self.scorePlayer > player.getScorePlayer()

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o)

    def __hash__(self) -> int:
        return super().__hash__()
