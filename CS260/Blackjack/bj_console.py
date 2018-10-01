from bjgame import BJGame

class BJGameConsole():
    """
    Run blackjack in the console in text.
    """
    game = BJGame()
    
    def getInput(self):
    	returnVal = None
    	# stay in loop until valid input is given
    	while(returnVal == None):
    		selection = input("Would you like to [d]raw or [s]tand?")
    		if selection == "d":
    			returnVal = "Draw"
    		elif selection == "s":
    			returnVal = "Stand"
    	return returnVal

    def turnAtom(self):
    	dealerCard = str(self.game.getDealerCard())
    	playerHand = self.game.playerHand.getHandString()
    	playerTotal = self.game.playerHand.getHandValue()
    	print("The dealer is showing {}. You are holding {} ({}).".format(dealerCard, playerHand, playerTotal))
    	pCommand = self.getInput()
    	print("") # line for readability
    	if pCommand == "Draw":
    		self.game.playerDraw()
    	if pCommand == "Stand" or self.game.playerHand.isBusted():
    		self.game.endPlayerTurn()

    def endGame(self):
    	pHand = self.game.playerHand.getHandString()
    	dHand = self.game.dealerHand.getHandString()
    	pVal = self.game.playerHand.getHandValue()
    	dVal = self.game.dealerHand.getHandValue()
    	victoryStr = "You have lost."
    	if self.game.didPlayerWin():
    		victoryStr = "You win!"
    		
    	print("Your hand: {}({})\nDealer's hand: {}({})\n{}\n\n".format(
            pHand, pVal, dHand, dVal, victoryStr))


    def gameLoop(self):
    	print("Welcome to blackjack!")
    	while True:
    		self.game.newGame()
    		while self.game.playerTurn:
    			self.turnAtom()
    		self.endGame()

consoleGame = BJGameConsole()
consoleGame.gameLoop()