import bjcard
import random

class BJDeck():
	deck = []
	index = 0

	# constructor
	def __init__(self):
		for s in ["S", "H", "D", "C"]:
			for f in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:
				self.deck.append(bjcard.BJCard(f, s))

	# shuffling method
	def shuffle(self):
		index = 0
		newDeck = []
		while len(self.deck) > 0:
			card = self.deck[random.randint(0, len(self.deck) - 1)]
			newDeck.append(card)
			self.deck.remove(card)
		self.deck = newDeck

	# lists the cards in their current order
	def printDeck(self):
		for c in self.deck:
			print(c)

	# draw method. Shuffles if the end of the deck is reached, which resets the index
	def drawCard(self):
		if self.index >= len(self.deck) - 1:
			shuffle()
		card = self.deck[self.index]
		self.index += 1
		return card