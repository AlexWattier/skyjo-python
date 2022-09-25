from model import Deck
from model import Card
from model import VisibilityCard
from model import NextPlayer
from model import Player
from model import LevelStatus


class Game:
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
        self.initGame()

    def isDeckBlock(self):
        return self.deckBlock

    def setDeckBlock(self):
        self.deckBlock = True

    def refreshScore(self):
        self.playerOne.scorePlayer()
        self.playerTwo.scorePlayer()

    def lastDiscardCard(self):
        return self.discardDeck.lastHit()

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

    def registerObserver(self, observer):
        self.observers.append(observer)

    def notifyObserver(self, *args):
        if args[0] is not None:
            self.update(args[0])
        else:
            self.update(args[0])

    def deckEmpty(self) -> bool:
        return self.deck.isEmpty()

    def initGame(self):
        self.startShuffle()
        self.giveCards()
        self.hitInitCard()
        self.refreshScore()
        self.whoStart()

    def whoStart(self):
        if self.playerTwo.beats(self.playerOne):
            self.playerTour()

    def startShuffle(self):
        self.deck.shuffle()

    def giveCards(self):
        for i in range(0, 12):
            self.playerOne.adCard(self.giveOneCard())
            self.playerTwo.adCard(self.giveOneCard())

    def giveOneCard(self) -> Card.Card:
        return self.deck.hit()

    def hitInitCard(self):
        self.playerOne.hitCardPlayer()
        self.playerTwo.hitCardPlayer()

    def giveDiscardCard(self):
        card: Card.Card = self.giveOneCard()
        self.discardDeck.addCard(card)
        self.setDiscardDeck(self.discardDeck)

    def setDiscardDeck(self, discardDeck: Deck.Deck):
        self.discardDeck = discardDeck

    def getDeck(self) -> Deck.Deck:
        return self.deck

    def getPlayerOne(self) -> Player.Player:
        return self.playerOne

    def getPlayerTwo(self) -> Player.Player:
        return self.playerTwo

    def playerTour(self):
        if self.tourPlayer == NextPlayer.NextPlayer.PLAYERONE:
            self.tourPlayer = NextPlayer.NextPlayer.PLAYERTWO
        elif self.tourPlayer == NextPlayer.NextPlayer.PLAYERTWO:
            self.tourPlayer = NextPlayer.NextPlayer.PLAYERONE

    def showCard(self, player, nbCard):
        player.setCardVisibility(nbCard)

    def getDiscardToDeck(self) -> bool:
        return self.discardToDeck

    def setDiscardToDeck(self, discardToDeck: bool):
        self.discardToDeck = discardToDeck

    def endPlayer(self, players):
        for i in range(0, len(players.getHandPlayer())):
            if players.getCard(i).isHidden():
                return False
        return True

    def winner(self) -> LevelStatus.LevelStatus:
        if self.playerOne.beats(self.playerTwo):
            return LevelStatus.LevelStatus.FAIL
        if self.playerTwo.beats(self.playerOne):
            return LevelStatus.LevelStatus.WIN
        return LevelStatus.LevelStatus.IN_PROGRESS

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o)

    def __hash__(self) -> int:
        return super().__hash__()

    def update(self, param):
        pass
