def fibonacci_sequence(threshold):
	"""Prints fibonnaci sequence"""
	result, num_1 = 0 , 0
	num_2 = num_1+1
	print(f"--- Treshold set up to {threshold:,} ---")

	while result <= threshold-num_1:

		result = num_1 + num_2
		print(f"{num_1:,} + {num_2:,} = {result:,}")
		num_1 = num_2
		num_2 = result

fibonacci_sequence(250000)
	