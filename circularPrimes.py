import logging

def is_prime(n):
	"""Function returns 1 when number is prime and 0 if it is not"""
	for i in range(2, n / 2) :
		if(n % i == 0):
			return 0
	return 1

def num_digits(n):
	"""Function returns the number of digits in the n i.e num_digits(589) = 3"""
	num_digits = 0
	operand = n
	while operand != 0:
		num_digits += 1
		operand = operand / 10
	return num_digits

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


def disqualify_conditions(n):
	"""Function returns 1 if n cannot be a circular prime. If it returns 0 n may or may not be a circular prime."""
	if does_number_have_zero(n):
		return 1
	if is_number_even(n):
		return 1
	if is_digit_even(n):
		return 1
	if not is_prime(n):
		return 1
	return 0

def is_circular_prime(n):
	"""Function return 1 if number is circular prime and 0 other wise"""
	if disqualify_conditions(n):
		return 0
	else :
		logging.info("is_circular_prime : Testing candidate = %d ...", n)
		operand = n
		operand_digits = num_digits(n)
		for i in range(0, operand_digits):
			logging.debug("is_circular_prime : Testing operand = %d ...", operand)
			if is_prime(operand):
				operand = rotate_number(operand)
			else :
				logging.debug("is_circular_prime : operand = %d is NOT Prime. Exiting function...", operand)
				return 0
		return 1


def main():
	print "Running circularPrimes.py... \n"
	logging.basicConfig(level=logging.INFO)
	#logging.basicConfig(level=logging.DEBUG)
	
	
	number = 973333
	logging.debug("num_digits(%d) = %d", number, num_digits(number))
	logging.debug("last_digit(%d) = %d", number, last_digit(number))
	logging.debug("does_number_have_zero(%d) = %d", number, does_number_have_zero(number))
	logging.debug("rotate_number(%d) = %d", number, rotate_number(number))
	logging.debug("is_digit_even(%d) = %d", number, is_digit_even(number))
	logging.debug("is_circular_prime(%d) = %d", number, is_circular_prime(number))
	
	#limit = 100
	limit = 1000000
	result_list = []
	for number in range(10, limit):
		if is_circular_prime(number):
			result_list.append(number)

	logging.info("RESULTS: {}".format(' '.join(map(str, result_list))))
	print "ANSWER = ", len(result_list) + 4 #Add 4 as this does account for circular primes < 10
    	

main()
