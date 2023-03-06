""" Problem 45 """


def get_triangular_numbers(n):
    """Returns list of triangle numbers upto input n. f(n) = n(n+1)/2"""
    result = []
    for i in range(1, n + 1):
        result.append((i * (i + 1)) / 2)
    return result


def get_pentagonal_numbers(n):
    """Returns list of pentagonal numbers upto input n. f(n) = n(3n-1)/2"""
    result = []
    for i in range(1, n + 1):
        result.append((i * ((3 * i) - 1)) / 2)
    return result


def get_hexagonal_numbers(n):
    """Returns list of hexagonal numbers upto input n. f(n) = n(2n-1)"""
    result = []
    for i in range(1, n + 1):
        result.append((i * (2 * i - 1)))
    return result


n = 100000

triangular_number_list = get_triangular_numbers(n)
pentagonal_number_list = get_pentagonal_numbers(n)
hexagonal_number_list = get_hexagonal_numbers(n)

for item in triangular_number_list:
    if item in pentagonal_number_list:
        if item in hexagonal_number_list:
            print(f"Found {item}!")
