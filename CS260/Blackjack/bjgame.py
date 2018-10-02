import bjdeck
import bjhand

class BJGame():
    """
    Maintains the information for a two-person blackjack game. Basically a deck, a hand each for the
    player and dealer, and some light state tracking.
    """
    # variables scoped to the class
    deck = bjdeck.BJDeck()
    playerHand = bjhand.BJHand(deck)
    dealerHand = bjhand.BJHand(deck)
    playerTurn = True

    def __init__(self):
        """
        Creates a new game. Calls a different function to do so, so that it can be called without having
        to create a new object.
        """
        self.newGame()
	
    def newGame(self):
        """
        Shuffle the deck, set the flag, clear the hands, and deal each actor two cards
        """
        self.deck.shuffle()
        self.playerTurn = True
        self.playerHand.clear()
        self.dealerHand.clear()
        self.playerHand.drawCard()
        self.dealerHand.drawCard()
        self.playerHand.drawCard()
        self.dealerHand.drawCard()

    def getDealerCard(self):
        """
        Get the dealer's face up card.
        """
        return self.dealerHand.cards[0]

	
    def dealerTurn(self):
        """
        Execute the dealer's turn. The dealer will draw until they either bust, or win
        (the dealer wins on a tie).
        """
        if self.playerHand.isBusted() == False:
            while self.dealerHand.isBusted() == False and \
            self.playerHand.getHandValue() > self.dealerHand.getHandValue():
                self.dealerHand.drawCard()

    def didPlayerWin(self):
        """
        Returns a boolean indicating whether the player has won (true) or lost (false)
        """
        returnVal = True
        if self.playerHand.isBusted() or \
            (self.dealerHand.isBusted() == False and \
            self.dealerHand.getHandValue() >= self.playerHand.getHandValue()):
            returnVal = False
        return returnVal

    def endPlayerTurn(self):
        """
        Called to end the player's turn. Sets a flag and calls the dealer's turn.
        """
        self.playerTurn = False
        self.dealerTurn()

    def playerDraw(self):
        """
        The player draws a card. If the player busts, his turn is forcibly ended.
        """
        self.playerHand.drawCard()
        if self.playerHand.isBusted():
            self.endPlayerTurn()
