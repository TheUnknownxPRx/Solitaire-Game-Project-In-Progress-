from card import Card


class Stack:

    def __init__(self):
        self.Cards = []
        self.card_counter = 0

    def addCard(self, card):
        if card == "":
            self.Cards.append(card)
        else:
            self.Cards.append(card)
            self.card_counter += 1
        # top card is always in card counter

    def getCard(self, index):
        return self.Cards[index]

    def setCard(self, card, index):
        self.Cards[index] = card

    def getCardCounter(self):
        return self.card_counter

    def setCardCounter_min1(self):
        self.card_counter -= 1

    def setCardCounter_plus1(self):
        self.card_counter += 1

    def getColor(self):
        return self.getColor()
