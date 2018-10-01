import bjdeck
import bjhand

class BJGame():
	deck = bjdeck.BJDeck()
	playerHand = bjhand.BJHand(deck)
	dealerHand = bjhand.BJHand(deck)
	playerTurn = True

	def __init__(self):
		self.newGame()
	
	def newGame(self):
		self.deck.shuffle()
		self.playerTurn = True
		self.playerHand.clear()
		self.dealerHand.clear()
		self.playerHand.drawCard()
		self.dealerHand.drawCard()
		self.playerHand.drawCard()
		self.dealerHand.drawCard()

	def getDealerCard(self):
		return self.dealerHand.cards[0]

	
	def dealerTurn(self):
		if self.playerHand.isBusted() == False:
			while self.dealerHand.isBusted() == False and \
			self.playerHand.getHandValue() > self.dealerHand.getHandValue():
				self.dealerHand.drawCard()

	def didPlayerWin(self):
		returnVal = True
		if self.playerHand.isBusted() or \
		(self.dealerHand.isBusted() == False and \
		self.dealerHand.getHandValue() >= self.playerHand.getHandValue()):
			returnVal = False
		return returnVal

	def endPlayerTurn(self):
		self.playerTurn = False
		self.dealerTurn()

	def playerDraw(self):
		self.playerHand.drawCard()
		if self.playerHand.isBusted():
			self.endPlayerTurn()