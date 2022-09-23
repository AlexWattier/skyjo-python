from model import Card
from model import VisibilityCard

hidden = VisibilityCard.VisibilityCard.hidden

card = Card.Card(5, hidden)


def print_hi():
    print(card)


print_hi()