from eulerlib.operations import get_list_of_digits, list2num, get_nth_prime_number
from itertools import permutations

"""
The number,1406357289, is a  to  pandigital number because it is made up of each of the digits  to  in some order, but it also has a rather interesting sub-string divisibility property.

Let  be the st digit,  be the nd digit, and so on. In this way, we note the following:

 is divisible by
 is divisible by
 is divisible by
 is divisible by
 is divisible by
 is divisible by
 is divisible by
Find the sum of all  to  pandigital numbers with this property.
"""

def is_substring_valid(starting_index:int, number:int):
    """
    Given a starting index for the substring, will check if ths substring number is dvisible by the prime number of that index.
    For example, if number = 1406357289 and starting index is 2, then 406 is divisble by 2 and this returns true
    if number = 1406357289 and starting index is 5, then 357 is divisble by 7 and this returns true
    """
    d1 = get_digit(number, starting_index)
    d2 = get_digit(number, starting_index + 1)
    d3 = get_digit(number, starting_index + 2)
    substring = list2num([d1, d2, d3])
    prime_divisor = get_nth_prime_number(starting_index - 1)
    # print(f"substring = {substring} and prime_divisor = {prime_divisor}")
    return not substring % prime_divisor

def is_valid_number(number:int):
    """
    Given a number, this will check if the divisibility rule of the problem will hold
    """
    for idx in range(2, 9):
        if not is_substring_valid(idx, number):
            return False
    return True

def get_digit(number: int, n:int):
    """
    Returns the nth digit in number
    For example, if number = 140635
    and n = 2, it will return 4
    """
    digits = get_list_of_digits(number)
    return digits[-1 * n]


digits_list = [i for i in range(0, 10)]
permutations = permutations(digits_list)
sum = 0

for permutation in permutations:
    if permutation[0] == 0: continue
    num = list2num(permutation)
    if is_valid_number(num):
        print(num)
        sum += num

print(is_valid_number(1406357289))
print(sum)