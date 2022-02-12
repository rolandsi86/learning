class IncomeTax:
	"""Income tax calculator."""
	def __init__ (self, income=0):
		self.income = income

	def calculation(self):
		"""Calculates income tax based on income amount.
		Example: 10000*0% + 10000*10%  + 25000*20% = $6000."""
		
		#20% tax
		if self.income > 20_000:
			tax = ((self.income - 20_000)*0.20)+1000
		#10% tax
		elif self.income > 10_000:
			tax = (self.income-10_000)*0.1
		#no tax on first 10_000 $
		else:
			tax = 0
		return tax

	def annoncement(self):
		"""Final annoncement to tax payer."""
		if self.calculation() > 0:
			print(f"Income tax is {self.calculation():,} $")
		else:
			print(f"Dou to the fact that your income was {self.income:,} "
				"$ tax isn't apliciable.")

