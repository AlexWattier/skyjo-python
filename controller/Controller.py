import random

from model.VisibilityCard import VisibilityCard

from model.Card import Card

from model.Game import Game
from model.Player import Player
from view.View import View


class AIPlayerTwo:
    def startPlayerTwo(self, game: Game, choseDifficulte: int):
        player: Player = game.getPlayerTwo()
        valeurDiscard: int = game.lastDiscardCard().getValue()
        if choseDifficulte == 1:
            self.easyPlayerTwo(game, player, valeurDiscard)
        elif choseDifficulte == 2:
            self.hardPlayerTwo(game, player, valeurDiscard)
        game.endGame()

    def hardPlayerTwo(self, game: Game, player: Player, valeurDiscard: int):
        if valeurDiscard > 2:
            game.setClickDeck()
            intCardDeck: int = game.deckHit().getValue()
            if intCardDeck < 3:
                self.choice(game, player)
            else:
                game.deckToDiscard()
                self.returnCardPlayer(player)
                game.endTour()
        else:
            game.setClickDiscard()
            self.choice(game, player)

    def easyPlayerTwo(self, game: Game, player: Player, valeurDiscard: int):
        if valeurDiscard > 5:
            game.setClickDeck()
            intCardDeck: int = game.deckHit().getValue()
            if intCardDeck < 6:
                self.choice(game, player)
            else:
                game.deckToDiscard()
                self.returnCardPlayer(player)
                game.endTour()
        else:
            game.setClickDiscard()
            self.choice(game, player)

    def choice(self, game: Game, player: Player):
        numCard: int = self.searchCardPlayer(player)
        if numCard == -2:
            numCard = self.randomCardPlayer(player)
        game.changeCard(player, numCard)

    def randomCardPlayer(self, playerTwo: Player) -> int:
        hand: list = playerTwo.getHandPlayer().copy()
        sizeHand: int = len(hand)
        handHidden: list = []
        for i in range(0, sizeHand):
            card: Card = hand.pop()
            if card.isHidden():
                handHidden.append(card)
        random.shuffle(handHidden)
        return handHidden.pop()

    def returnCardPlayer(self, playerTwo: Player):
        numCardReturn: int = self.randomCardPlayer(playerTwo)
        playerTwo.getCard(numCardReturn).setVisibility(VisibilityCard.nothide)

    def searchCardPlayer(self, playerTwo: Player) -> int:
        hand: list = playerTwo.getHandPlayer().copy()


class Controller:
    def __init__(self, *args) -> None:
        self.game = Game()
        self.difficulte: int = args[1]
        self.movePlayer = AIPlayerTwo()
        self.view = View(args[0], args[1], self)

    def changeCard(self, player: Player, nbCard: int):
        self.game.changeCard(player, nbCard)

    def startPlayerTwo(self, game: Game):
        self.movePlayer.startPlayerTwo(game, self.difficulte)
