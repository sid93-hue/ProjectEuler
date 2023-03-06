import sys


def num_digits(n):
    """
    Function returns the number of digits in the n i.e num_digits(589) = 3
    """
    output = 1
    number = n
    # Use // to get around number overflow issue
    # https://stackoverflow.com/questions/27946595/how-to-manage-division-of-huge-numbers-in-python
    while int(number // 10) != 0:
        output += 1
        number = int(number // 10)
    return output


def get_list_of_digits(n):
    """
    Return list containing digits of the number
    """
    output_list = []
    operand = n
    while operand != 0:
        digit = operand % 10
        output_list.append(digit)
        operand = operand // 10
    # print(output_list)
    return output_list


def last_digit(n):
    """
    Function returns the highest digit in n i.e last_digit(589) = 5
    """
    last_digit = 0
    operand = n
    while operand != 0:
        last_digit = operand % 10
        operand = operand // 10
    return last_digit


def first_digit(n):
    """
    Function returns the lowest digit in n i.e first_digit(589) = 9
    """
    return n % 10


def does_number_have_zero(n):
    """
    Function returns 1 if n has a 0 in its digits i.e does_number_have_zero(5089) == 1
    """
    operand = n
    while operand != 0:
        # print "\nOperand = ", operand
        if operand % 10 == 0:
            return 1
        operand = operand // 10
    return 0


def is_number_even(n):
    """
    Function returns 1 if n is even
    """
    if n % 2 == 0:
        return 1
    else:
        return 0


def is_digit_even(n):
    """
    Function returns 1 if any of the digits of n are even i.e is digit_even(635) = 1
    """
    operand = n
    while operand != 0:
        if operand % 2 == 0:
            return 1
        operand = operand // 10
    return 0


def is_prime(n):
    """
    Function returns 1 when number is prime and 0 if it is not
    """
    limit = (n ** (1 / 2)) + 1
    # print("is_prime(" + n + ") : limit = " + limit)
    for i in range(2, int(limit)):
        if n % i == 0:
            return False
    return True


def get_list_of_primes_sieve(n):
    """
    Returns list of prime numbers <=n using optimized sieve method
    """
    return_list = [i for i in range(2, n + 1)]
    iteration_list = [i for i in range(2, n + 1)]
    for item in iteration_list:
        if item % 2 == 0:
            return_list.remove(item)
        elif item % 3 == 0:
            return_list.remove(item)
        elif item % 5 == 0:
            return_list.remove(item)
        elif item % 7 == 0:
            return_list.remove(item)
        elif not is_prime(item):
            return_list.remove(item)
    return_list = [2, 3, 5, 7] + return_list
    return return_list


def get_list_of_primes(n):
    """
    Function returns list of primes <= n
    """
    output_list = []
    for i in range(2, n + 1):
        if is_prime(i):
            output_list.append(i)
    return output_list


def rotate_number(n):
    """
    Functions returns the rotated value of n i.e rotate_number(589) = 895
    """
    operand = n
    num_digits_n = num_digits(n)
    operand = operand * 10
    operand = operand % (10**num_digits_n)
    operand = operand + last_digit(n)
    return operand


def is_perfect_square(n):
    """
    Returns True is number is perfect square. False otherwise
    """
    if (int(n ** (1 / 2))) ** 2 == n:
        return True
    else:
        return False


def is_right_triangle(a, b, c):
    """
    Returns True if a,b,c form the sides of a right triangle
    """
    if (a**2) + (b**2) == (c**2):
        return True
    else:
        return False


def factorial(n):
    """
    Returns factorial of n
    """
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 6
    if n == 4:
        return 24
    if n == 5:
        return 120
    if n == 6:
        return 720
    if n == 7:
        return 5040
    if n == 8:
        return 40320
    if n == 9:
        return 362880
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


def py_version():
    print("Python version")
    print(sys.version)
    print("Version info.")
    print(sys.version_info)
