from itertools import permutations

from eulerlib.operations import is_prime


def pan_digital_prime(digits):
    """
    Returns the largest pan_digital_prime number of n digits
    """
    digits_list = [i for i in range(1, digits + 1)]
    permutations_list = list(permutations(digits_list))
    highest_prime = 0
    for item in permutations_list:
        test_value = list2num(item)
        print(f"Testing item = {item} and test_value = {test_value}")
        if is_prime(test_value) and test_value > highest_prime:
            highest_prime = test_value

    print(highest_prime)


def list2num(in_list):
    return_value = 0
    for number in in_list:
        return_value = (return_value * 10) + number
    return return_value


a = [1, 3, 4, 3]

print(f"list2num of a = {list2num(a)}")

pan_digital_prime(7)
