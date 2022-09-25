from model import Deck
from model import Card
from model import VisibilityCard
from model import NextPlayer
from model import Player
from model import LevelStatus


class Game():
    def __init__(self) -> None:
        self.deck = Deck.Deck()
        self.deck.addAllCard()
        self.discardDeck = Deck.Deck()
        self.playerOne = Player.Player()
        self.playerTwo = Player.Player()
        self.observers = []
        self.tourPlayer = NextPlayer.NextPlayer.PLAYERONE
        self.clickDeck = False
        self.clickDiscard = False
        self.discardToDeck = False
        self.deckBlock = False
        self.init()

    def isDeckBlock(self):
        return self.deckBlock

    def setDeckBlock(self):
        self.deckBlock = True

    def refreshScore(self):
        self.playerOne.scorePlayer()
        self.playerTwo.scorePlayer()

    def lastDiscardCard(self):
        last: int = len(self.discardDeck) - 1
        return self.discardDeck.lastHit(last)

    def deckHit(self):
        return self.deck.hit()

    def getTourPlayer(self):
        return self.tourPlayer

    def getTourValue(self):
        return self.tourPlayer.getNamePlayer()

    def changeCard(self, player, nbCard):
        if self.clickDeck:
            cardTemp: Card.Card = self.deck.hit()
            self.showCard(player, nbCard)
            self.discardDeck.addCard(player.getCard(nbCard))
            player.getHandPlayer().insert(nbCard, cardTemp)
            self.showCard(player, nbCard)
            self.clickDeck = False
        elif self.clickDiscard:
            cardTemp: Card.Card = self.discardDeck.lastHit()
            self.showCard(player, nbCard)
            self.discardDeck.addCard(player.getCard(nbCard))
            player.getHandPlayer().insert(nbCard, cardTemp)
            self.showCard(player, nbCard)
            self.clickDiscard = False
        self.endTour()

    def setClickDeck(self):
        self.clickDeck = not self.clickDeck

    def getDeckClick(self):
        return self.clickDeck

    def getDiscardClick(self):
        return self.clickDiscard

    def setClickDiscard(self):
        self.clickDiscard = not self.clickDiscard

    def deckToDiscard(self):
        if self.clickDeck:
            cardTemp: Card.Card = self.deck.hit()
            self.discardDeck.addCard(cardTemp)
            self.clickDeck = False
            self.clickDiscard = False
            self.discardToDeck = True

    def endTour(self):
        self.playerTour()
        self.deckBlock = False
        self.notifyObserver()

    def endGame(self):
        if self.endPlayer(self.playerOne) or self.endPlayer(self.playerTwo):
            self.returnAllCard(self.playerOne)
            self.returnAllCard(self.playerTwo)
            self.refreshScore()
            return self.winner()
        return LevelStatus.LevelStatus.IN_PROGRESS

    def returnAllCard(self, player):
        for i in range(0, len(player.getHandPlayer())):
            card: Card.Card = player.getCard(i)
            if card.isHidden():
                card.setVisibility(VisibilityCard.VisibilityCard.nothide)

    def registerObserver(self,observer):
        self.observers.append(observer)

    def notifyObserver(self,* args):
        if args[0] != None:
            self.update(args[0])
        else:
            self.update(args[0])

    def deckEmpty(self)->bool:
        return self.deck.isEmpty()

    def initGame(self):
        self.startShuffle()
        self.giveCards()
        self.hitInitCard()
        self.refreshScore()
        self.whoStart()

    def whoStart(self):
        self.playerTwo.beats(self.playerOne)

    def showCard(self, player, nbCard):
        pass

    def playerTour(self):
        pass

    def endPlayer(self, playerOne):
        pass

    def winner(self):
        pass

    def update(self, param):
        pass

    def startShuffle(self):
        pass
