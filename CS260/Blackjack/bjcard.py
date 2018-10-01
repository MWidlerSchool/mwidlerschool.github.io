class BJCard():
	"""
		A class for representing a single playing card (no jokers).
	"""
	suite = "?"
	face = "?"
	value = 0
	
	# constructor
	def __init__(self, f, s):
		# set the suite
		self.suite = s
	
		# set the face
		self.face = f

		# set the value
		try:
			self.value = int(self.face)
		except:
			if self.face == "A":
				self.value = 1
			elif self.face == "J" or self.face == "Q" or self.face == "K":
				self.value = 10

	# to string
	def __str__(self):
		return str(self.face) + self.suite
	
# test method
def test():
	card = BJCard("A", "H")
	print(card, " = ", card.value)