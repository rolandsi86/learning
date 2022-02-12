from random import randint

def number_list():
	"""Generate the list of 3 random numbers."""
	number_list=[]
	for num in range(3):
		num=randint(1,100)
		number_list.append(num)
	return number_list

def assign_to_variables():
	"""Assign values to variables."""
	numbers = number_list()
	print(f"Number list: {numbers}")
	num_1=numbers[0]
	num_2=numbers[1]
	num_3=numbers[2]
	return num_1,num_2,num_3

def find_largest_number():
	"""Find the largest number among 3 random numbers."""
	num_1,num_2,num_3=assign_to_variables()
	
	if num_1 > num_2 and num_1 > num_3:
			largest=num_1
	elif num_2 > num_1 and num_2 > num_3:
			largest=num_2
	else:
		largest=num_3
	print(f"The largest number is [{largest}]")

find_largest_number()
