class Card(object):
    # the init method is called every time a new object is created
    def __init__(self, color, suit, value):
        self.color = color
        self.suit = suit
        self.value = value


def define_suit(num):
    if num == 1:
        return "Hearts"
    elif num == 2:
        return "Diamonds"
    elif num == 3:
        return "Spades"
    elif num == 4:
        return "Clubs"
    else:
        return "ERROR"

def define_color(num):
    if num < 3:
        return "red"
    else:
        return "black"

def define_value(num):
    if num == 1:
        return "Ace"
    elif num < 11:
        return str(num)
    elif num == 11:
        return "Jack"
    elif num == 12:
        return "Queen"
    elif num == 13:
        return "King"
    else:
        return "ERROR"


# MAIN PROGRAM
card_attr = [0, 0, 0]
deck_dictionary = {}
for i in range(1,5):
    card_attr[0] = define_color(i)
    card_attr[1] = define_suit(i)
    for j in range(1,14):
        card_attr[2] = define_value(j)
        # print card_attr
        card_key = "card" + str(i) + "_" + str(j)
        deck_dictionary[card_key] = Card(card_attr[0], card_attr[1], card_attr[2])

print deck_dictionary['card1_12'].value
# card1 = Card('red', 'Hearts', 'Ace')
# print card1.color
# print card1.suit
# print card1.value

    


