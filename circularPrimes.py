"""Problem 35"""

import logging
from eulerlib.operations import *

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

	"""Testing a single number"""
	number = 973333
	logging.debug("num_digits(%d) = %d", number, num_digits(number))
	logging.debug("last_digit(%d) = %d", number, last_digit(number))
	logging.debug("does_number_have_zero(%d) = %d", number, does_number_have_zero(number))
	logging.debug("rotate_number(%d) = %d", number, rotate_number(number))
	logging.debug("is_digit_even(%d) = %d", number, is_digit_even(number))
	logging.debug("is_circular_prime(%d) = %d", number, is_circular_prime(number))
	
	limit = 100
	#limit = 1000000
	result_list = []
	for number in range(10, limit):
		if is_circular_prime(number):
			result_list.append(number)

	logging.info("RESULTS: {}".format(' '.join(map(str, result_list))))
	print "ANSWER = ", len(result_list) + 4 #Add 4 as this does account for circular primes < 10    	

main()
