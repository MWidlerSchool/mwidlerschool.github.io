import bjcard
import random

class BJDeck():
    """
    A class representing a deck of playing cards, initially ordered.
    Cards are dealt by an index value which moves through the list; shuffling reorders the list
    and resets the index.
    """
    
    
    def __init__(self):
        """
        Creates a new deck.
        """
        self.deck = []
        self.index = 0
        for s in ["S", "H", "D", "C"]:
            for f in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:
                self.deck.append(bjcard.BJCard(f, s))

    
    def shuffle(self):
        """
        Reorders the list of cards and resets the index.
        """
        self.index = 0
        newDeck = []
        while len(self.deck) > 0:
            card = self.deck[random.randint(0, len(self.deck) - 1)]
            newDeck.append(card)
            self.deck.remove(card)
        self.deck = newDeck
    		
	
    def drawCard(self):
        """
        Draws the top card, increments the index, and reshuffles if necessary.
        Note: This means it is possible to draw the same card twice, in extremely rare cases.
        """
        if self.index >= len(self.deck) - 1:
            self.shuffle()
        card = self.deck[self.index]
        self.index += 1
        return card

    
    def printDeck(self):
        """
        Test function. Prints out the deck to the console.
        """
        for c in self.deck:
            print(c)
            
# test method
if __name__ == "__main__":
	deck = BJDeck()
	deck.shuffle()
	deck.printDeck()
	
	for i in range(200):
            deck.drawCard()