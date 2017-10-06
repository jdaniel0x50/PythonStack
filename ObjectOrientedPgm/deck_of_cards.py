class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        if self.value == 1:
            self.value = "Ace"
        elif self.value == 11:
            self.value = "Jack"
        elif self.value == 12:
            self.value = "Queen"
        elif self.value == 13:
            self.value = "King"

class Deck(object):
    def __init__(self):
        self.cards = []
        suit_list = ["hearts", "diamonds", "spades", "clubs"]
        for suit in suit_list:
            for number in range(1,14):
                new_card = Card(number, suit)
                self.cards.append(new_card)

my_deck = Deck()
for card in my_deck.cards:
    print "This is the " + str(card.value) + " of " + card.suit



