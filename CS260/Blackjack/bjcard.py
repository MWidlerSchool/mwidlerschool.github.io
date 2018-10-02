class BJCard():
	"""
		A class for representing a single playing card (no jokers).
	"""
	
	# basic values of a card
	suit = "?"
	face = "?"
	value = 0
	
	# constructor
	def __init__(self, f, s):
		# set the suit
		if s == "H" or s == "S" or s == "D" or s == "C":
                    self.suit = s
		else:
                    raise Exception("Invalid suit value in bjcard.py")
                
		# set the face; checked for vaild input when the value is set
		self.face = f

		# set the value. value = face, if face is a number
		try:
			self.value = int(self.face)
		# if the face isn't a number, assign the value
		except: 
			if self.face == "A":
				self.value = 1 # 11 option handled in bjhand.py
			elif self.face == "J" or self.face == "Q" or self.face == "K":
				self.value = 10
			else: # throw an exception if the input is invalid
                            raise Exception("Invalid card value in bjcard.py")

	# to string method
	def __str__(self):
		return str(self.face) + self.suit
	
# test method
if __name__ == "__main__":
	card = BJCard("A", "H")
	print(card, "=", card.value)
	try:
            card = BJCard("10", "K")
	except:
            print("Exception caught for invalid input")