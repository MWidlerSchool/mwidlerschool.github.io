import tkinter
import bjgame

#declare constants
windowSize = "500x300"
widgetWidth = 250
widgetHeight = 75
    

class BJ_GUI(tkinter.Frame):
    
    def __init__(self, master):
        """ Initialize frame"""
        super(BJ_GUI, self).__init__(master)
        self.playerHandMessage = None
        self.dealerHandMessage = None
        self.messageBoxMessage = None
        self.game = None
        self.playersTurn = False
        self.create_widgets(master)
    
    def hitButtonPressed(self):
        if self.playersTurn and self.game != None:
            self.game.playerDraw()
        if self.game.playerHand.isBusted():
            self.playersTurn = False
            self.game.endPlayerTurn()
        self.updateScreen()
    
    def standButtonPressed(self):
        if self.playersTurn and self.game != None:
            self.playersTurn = False
            self.game.endPlayerTurn()
        self.updateScreen()
    
    def newGameButtonPressed(self):
        self.game = bjgame.BJGame()
        self.playersTurn = True
        self.updateScreen()
    
    def quitButtonPressed(self):
        self.master.destroy()
    
    def updateScreen(self):
        playerStr = "Player Hand:   "
        dealerStr = "Dealer Hand:   "
        if self.game != None:
            playerStr += self.game.playerHand.getHandString()
            if self.playersTurn:
                dealerStr += (str(self.game.getDealerCard()) + " ?")
            else:
                dealerStr += self.game.dealerHand.getHandString()
        self.playerHandMessage.set(playerStr)
        self.dealerHandMessage.set(dealerStr)
        
        messageStr = ""
        if self.game != None:
            playerTotal = self.game.playerHand.getHandValue()
            dealerTotal = self.game.dealerHand.getHandValue()
            if self.playersTurn:
                messageStr = "You have {}. Hit or stand?".format(playerTotal)
            else: # game has ended
                if self.game.playerHand.isBusted():
                    messageStr = "Busted! You have lost."
                else:
                    if self.game.dealerHand.isBusted():
                        messageStr = "The dealer busted trying to beat your {}. You win!".format(playerTotal)
                    else:
                        messageStr = "You have {}; the dealer has {}. ".format(playerTotal, dealerTotal)
                        if playerTotal > dealerTotal:
                            messageStr += "You win!"
                        elif playerTotal == dealerTotal:
                            messageStr += "Dealer wins on a tie! You have lost."
                        else:
                            messageStr += "You have lost."
        self.messageBoxMessage.set(messageStr)

    def create_widgets(self, master):
        self.playerHandMessage = tkinter.StringVar()
        self.dealerHandMessage = tkinter.StringVar()
        self.messageBoxMessage = tkinter.StringVar()
        self.playerHandMessage.set("Player Hand: ")
        self.dealerHandMessage.set("Dealer Hand: ")
        self.messageBoxMessage.set("Press 'New Game' to begin!")
        playerHandField = tkinter.Label(master, textvariable = self.playerHandMessage, anchor = "w")
        playerHandField.place(x = 0, y = 0, width = widgetWidth, height = widgetHeight)
        
        dealerHandField = tkinter.Label(master, textvariable = self.dealerHandMessage, anchor = "w")
        dealerHandField.place(x = widgetWidth, y = 0, width = widgetWidth, height = widgetHeight)
        
        hitButton = tkinter.Button(master, text = "Hit", command = self.hitButtonPressed)
        hitButton.place(x = 0, y = widgetHeight, width = widgetWidth / 2, height = widgetHeight)
        
        standButton = tkinter.Button(master, text = "Stand", command = self.standButtonPressed)
        standButton.place(x = widgetWidth / 2, y = widgetHeight, width = widgetWidth / 2, height = widgetHeight)
        
        messageField = tkinter.Label(master, textvariable = self.messageBoxMessage)
        messageField.place(x = 0, y = widgetHeight * 2, width = widgetWidth * 2, height = widgetHeight)
        
        newGameButton = tkinter.Button(master, text = "New Game", command = self.newGameButtonPressed)
        newGameButton.place(x = 0, y = widgetHeight * 3, width = widgetWidth, height = widgetHeight)
        
        quitButton = tkinter.Button(master, text = "Quit", command = self.quitButtonPressed)
        quitButton.place(x = widgetWidth, y = widgetHeight * 3, width = widgetWidth, height = widgetHeight)
  
#create and run
root=tkinter.Tk()
root.title("Blackjack")
root.geometry(windowSize)
app = BJ_GUI(master = root)
root.mainloop()

