import bjdeck
import bjhand

class BJHand():
	cards = []
	deck = None

	def __init__(self, theDeck):
		self.deck = theDeck

	
	def getHandValue(self):
		val = 0
		hasAce = False
		for card in self.cards:
			val += card.value
			if(card.value == 1):
				hasAce = True
		if hasAce and (10 + val > 21) == False:
			val += 10

		return val

	def drawCard(self):
		self.cards.append(self.deck.drawCard())

	def getHandString(self):
		returnStr = ""
		for card in self.cards:
			returnStr += str(card) + " "
		return returnStr
	
	def clear(self):
		self.cards = []

	def isBusted(self):
		busted = False
		if self.getHandValue() > 21:
			busted = True
		return busted
	

if __name__ == "__main__":
	deck = bjdeck.BJDeck()
	hand = BJHand(deck)
	deck.shuffle()
	for i in range(5):
		hand.drawCard()
		printVal = hand.getHandString()
		printVal += ", Total = " + str(hand.getHandValue())
		printVal += ", Busted = " + str(hand.isBusted())
		print(printVal)













