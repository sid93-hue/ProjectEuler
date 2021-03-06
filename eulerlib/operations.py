def num_digits(n):
	"""Function returns the number of digits in the n i.e num_digits(589) = 3"""
	num_digits = 0
	operand = n
	while operand != 0:
		num_digits += 1
		operand = operand / 10
	return num_digits

def is_prime(n):
	"""Function returns 1 when number is prime and 0 if it is not"""
	for i in range(2, n / 2) :
		if(n % i == 0):
			return 0
	return 1

def last_digit(n):
	"""Function returns the highest digit in n i.e last_digit(589) = 5"""
	last_digit = 0
	operand = n
	while operand != 0:
		last_digit = operand % 10
		operand = operand / 10
	return last_digit

def rotate_number(n):
	"""Functions returns the rotated value of n i.e rotate_number(589) = 895"""
	operand = n
	num_digits_n = num_digits(n)
	operand = operand * 10
	operand = operand % (10 ** num_digits_n)
	operand = operand + last_digit(n)
	return operand

def does_number_have_zero(n):
	"""Function returns 1 if n has a 0 in its digits i.e does_number_have_zero(5089) == 1"""
	operand = n
	while operand != 0:
		#print "\nOperand = ", operand
		if operand % 10 == 0:
			return 1
		operand = operand/10
	return 0

def is_number_even(n):
	"""Function returns 1 if n is even"""
	if n % 2 == 0:
		return 1
	else :
		return 0

def is_digit_even(n):
	"""Function returns 1 if any of the digits of n are even i.e is digit_even(635) = 1"""
	operand = n
	while operand != 0:
		if operand % 2 == 0:
			return 1
		operand = operand / 10
	return 0