""" Problem 46 """

from eulerlib.operations import is_prime, is_perfect_square, get_list_of_primes_sieve


def is_goldback(n, prime_list=None):
    """Returns True if n can be written as sum of a prime(p) + 2 * square of an intereger(s)"""

    if prime_list != None:
        this_prime_list = []
        for item in prime_list:
            if item <= n:
                this_prime_list.append(item)
            else:
                break
    else:
        this_prime_list = get_list_of_primes_sieve(n)

    result = False
    for item in this_prime_list:
        if is_perfect_square((n - item) / 2):
            result = True
            # print(f"{n} can be written as {item} + 2*{(n - item)/2}")
            break
    return result


n = 10000

prime_list = get_list_of_primes_sieve(n)

print(f"Primes generated!")

print(f"Prime List = {prime_list}")

i = 33
while i < n:
    i = i + 2
    if not is_goldback(i, prime_list):
        print(f"{i} does not satisy the goldback conjecture")


# print(is_goldback(81, prime_list))
