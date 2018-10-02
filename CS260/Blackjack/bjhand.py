import bjdeck

class BJHand():
    """
    Represents a blackjack hand. Consists of two or more cards, which are dealt from the
    deck. Each hand must belong to a deck, though multiple hands can (and often should)
    belong to the same deck.
    """
    
    def __init__(self, theDeck):
        """
        Constructor. A hand must be initialized with a deck.
        """
        self.cards = [] # the bjcards which make up the hand
        self.deck = None # the deck which deals to this hand
        if isinstance (theDeck, bjdeck.BJDeck):
            self.deck = theDeck
        else:
            raise Exception("New BJHand was not initialized with a valid BJDeck.")

	
    def getHandValue(self):
        """
        Returns the blackjack value of the hand. When one or more aces are present, the hand checks
        to see if using one as an 11 instead of a 1 would be advantageous, and if true does so.
        Using two aces as 11s is never advantageous.
        """
        sum = 0
        hasAce = False
        
        # iterate throught the cards, adding their values to a sum
        for card in self.cards:
            sum += card.value
            if(card.value == 1):
                hasAce = True
        # if one or more aces are present, check if one should be an 11
        if hasAce and (10 + sum > 21) == False:
            sum += 10

        return sum
    
    
    def drawCard(self):
        """
        Draw the top card from the deck.
        """
        self.cards.append(self.deck.drawCard())


    def getHandString(self):
        """
        Returns a string representing the cards in the hand.
        """
        returnStr = ""
        for card in self.cards:
            returnStr += str(card) + " "
        return returnStr
	
	
    def clear(self):
        """
        Does what it says on the tin.
        """
        self.cards = []

    def isBusted(self):
        """
        Checks to see if this hand is over 21. Returns a boolean.
        """
        busted = False
        if self.getHandValue() > 21:
            busted = True
        return busted
	

# Testing function
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













