from model import VisibilityCard
from model import Card
import random

class Deck:

    def __init__(self, * args):
        self.deck = []
        if args[0] != None:
            if isinstance(args[0], Deck):
                self.deck = args[0]

    def addAllCard(self:list):

        for i in range(0,5):
            self.deck.append(Card.Card(-2,VisibilityCard.VisibilityCard.hidden))
        for i in range(0, 15):
            self.deck.append(Card.Card(0, VisibilityCard.VisibilityCard.hidden))
        for i in range(0, 10):
            self.deck.append(Card.Card(-1, VisibilityCard.VisibilityCard.hidden))
            for j in range(1, 13):
                self.deck.append(Card.Card(j, VisibilityCard.VisibilityCard.hidden))

    def shuffle(self):
        random.shuffle(self.deck)

    def hit(self):
        tmp: Card
        tmp = self.deck.pop(0)
        return tmp

    def isEmpty(self):
        return self.deck.len()== 0

    def remove(self,card:Card.Card):
        self.deck.remove(card)

    def addCard(self,card:Card.Card):
        self.deck.append(card)

    def lastHit(self):
        return self.deck.pop(self.deck.len)

    def __str__(self) -> str:
        return super().__str__(self.deck)
