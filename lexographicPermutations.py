""" Problem 24: Lexographic Permutations"""

from eulerlib.operations import factorial

def lexographic_digit(n, p):
    """n = number of digits, p the order of the lexographic number"""
    n_fact = factorial(n);
    index = p//n_fact
    remainder = p - (index * n_fact)
    #print(f"index = {index}, remainder = {remainder}")
    return index, remainder;

n = 9
p = 1000000

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
i = len(digits)
p = 1000000
while i >= 2:
    i = i - 1
    index, p = lexographic_digit(i, p)
    print(f"digit = {digits[index]}")
    del digits[index]
    print(f"digits left = {digits}")
    