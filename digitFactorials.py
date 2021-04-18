""" Problem 34 """

from eulerlib.operations import get_list_of_digits, factorial

def sum_of_digit_factorials(n):
	digits = get_list_of_digits(n)
	sum = 0 
	for digit in digits:
		sum += factorial(digit)
	return sum


start_num = 145
end_num = 1000000

sum = 0 
for num in range(start_num, end_num):
	if num == sum_of_digit_factorials(num):
		sum += num
	
print(sum)

for i in range(1, 10):
	print(factorial(i))