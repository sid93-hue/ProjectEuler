"""Problem 37"""

from eulerlib.operations import *

def truncated_digits_l2r(n):
	"""Returns list of truncated numbers left -> right i.e truncated_digits_l2r(3797) returns [3797, 797, 97, 7]"""
	result_list = []
	operand = n
	divisor = 1
	while divisor < n :
		divisor = divisor * 10
	while divisor != 1 :
		operand = operand % divisor
		result_list.append(operand)
		divisor = divisor // 10
	return result_list

def truncated_digits_r2l(n):
	"""Returns list of truncated numbers right -> left i.e truncated_digits_r2l(3797) returns [3797, 3797, 37, 3]"""
	result_list = []
	operand = n
	while operand != 0 :
		result_list.append(operand)
		operand = operand // 10
	return result_list

def disqualify_conditions(n):
	"""Function returns 1 if n cannot be a truncatable prime. If it returns 0 n may or may not be a truncatable prime."""
	if first_digit(n) in [1, 2, 4, 5, 6, 8, 9]: #Lowest digit
		return 1
	elif last_digit(n) in [1, 4, 6, 8, 9]: #Highest digit
		return 1
	else :
		digit_list = get_list_of_digits(n)
		for digit in digit_list:
			if digit in [4, 6, 8] :
				return 1
		return 0


def is_truncatable_prime(n):
	"""Function returns 1 if number is a truncatable prime"""
	if not disqualify_conditions(n):
		l2r = truncated_digits_l2r(n)
		for number in l2r:
			if not is_prime(number):
				return 0
		r2l = truncated_digits_r2l(n)
		for number in r2l:
			if not is_prime(number):
				return 0
		print(f'Evaluated the following number {n} as a truncatable prime!')
		return 1
	else :
		return 0

def main():

	test_number = 3797
	print(f'result_list_l2r = {truncated_digits_l2r(test_number)}')
	print(f'result_list_r2l = {truncated_digits_r2l(test_number)}')
	print(f'is_truncatable_prime = {is_truncatable_prime(test_number)}')

	truncatable_prime_list = []
	for i in range(10, 1000000):
		if is_truncatable_prime(i):
			truncatable_prime_list.append(i)

	print(f'truncatable_prime_list = {truncatable_prime_list}')

	prime_list_sum = 0
	for prime in truncatable_prime_list:
		prime_list_sum += prime
	print(f'sum of list = {prime_list_sum}')


main()