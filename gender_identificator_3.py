def gender_identificator():
	"""Identifies a gender by last character in Latvian name."""	
	prompt=("\nIeraksti latviešu vārdu un es pateikšu vai tā ir sieviete vai vīrietis! ")
	prompt_1=("\nLai atkārtotu instrukcijas, raksti 'hint'")
	prompt_2=("\nLai izietu no programmas, raksti 'quit'\n")
	print(f"{prompt} \n{prompt_1} \n{prompt_2}")

	#flag variable
	active = True

	#program checks last character of name and according that assign gender
	while active:
		name=input()

		#converting name to lower case
		name=name.lower()

		#assigning variable to last character
		last_character=name[-1]

		#last characters in names
		man=['o','s']
		woman=['a', 'e']

		if name == 'quit':
			active = False
			x = 'Programma ir terminēta'
		elif last_character in man:
			x = f'{name.title()}, ir vīrietis!'
		elif last_character in woman:
			x = f'{name.title()}, ir sieviete!'
		elif name == 'hint':
			x = f"{prompt} \n{prompt_1} \n{prompt_2}"	 
		else:
			x = f'{name.title()}, nav latviešu vārds!'

		print(f"{x}\n")

gender_identificator()

