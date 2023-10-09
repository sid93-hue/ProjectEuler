from itertools import permutations

digits= [ i for i in range(1, 10)]
print(digits)

digits_permutation = permutations(digits)
print(type(digits_permutation))

# for j in list(digits_permutation):
#     print(j)
#     print(type(j))

print(dir(list))


def is_list_pandigital(digit_list):
    """dsfsa

    Args:
        digit_list (sfsa): sdfadf`

    Raises:
        ValueError: sfafds
    """
    sorted_in_list = digit_list.sort()
    for idx in range(len(digit_list) - 1):
        if digit_list[idx] == digit_list[idx + 1] :
            raise ValueError(f"in_list[{idx}] == in_list[{idx+1}] == {digit_list[idx]}. in_list must have unique numbers")

    # for digit in digit_list:


list1 = [1, 2, 3, 4]
print(is_list_pandigital(list1))

print(type(list1) == int)
print(type(list))