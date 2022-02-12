def armstrong_number():
	"""Check if the number is an Armstrong number."""
	while True:
		prompt=input(f"\nDo you wish to continue? (y/n) ")
		if prompt == 'y':
			print("\nProgram will check whether an n-digit integer is an "
				"Armstrong number or not.")
			
			number=int(input('Enter a number: '))

			#convert numbers to string, append to list and convert back to integer
			numbers_list=[int(x) for x in str(number)]

			#get lenght of the list to generate exponent
			order=len(numbers_list)

			cube=0
			result=0
			for num in numbers_list:
				cube = num**order
				result+=cube

			if result == number:
				print(f"{number} is an Armstrong number!")
			else:
				print(f"Sorry, {number} isn't an Armstrong number!")
		elif prompt == 'n':
			break

armstrong_number()


