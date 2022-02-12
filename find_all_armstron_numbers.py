def find_all_armstrong_numbers(start,stop):
	"""Find all Armstrong numbers in range from {start} to {stop}."""

	print(f"Armstrong numbers present in range from {start} to {stop}.")

	while start <=stop:
		#convert numbers to string, append to list and convert back to integer
		numbers_list=[int(x) for x in str(start)]

		order=len(numbers_list)

		multiplication=0
		result=0
		for num in numbers_list:
			multiplication = num**order
			result+=multiplication

		if result == start:
			print(f"{start}")
			start+=1
		else:
			start+=1

find_all_armstrong_numbers(100,100000)