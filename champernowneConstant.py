from eulerlib.operations import *


def champernowne_digit(n, x, y):
    starting_digit = 1
    if n == 1:
        return starting_digit

    num_digits_collected = 0
    current_number = 0

    while num_digits_collected < n:
        current_number += 1
        num_digits_collected += num_digits(current_number)
        print(
            f"current_number = {current_number} and num_digits_collected = {num_digits_collected}"
        )

    digits_list = get_list_of_digits(current_number)

    return digits_list[num_digits_collected - n]


i = 11
print(f"nth digit of {i} = {champernowne_digit(i)}")

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

d1 = champernowne_digit(1)
d10 = champernowne_digit(10)
d100 = champernowne_digit(100)
d1000 = champernowne_digit(1000)
d10000 = champernowne_digit(10000)
d100000 = champernowne_digit(100000)

print(f"d1 = {d1}, d10 = {d10}, d100 = {d100}, d1000 = {d1000}, d100000 = {d100000}")

answer = d1 * d10 * d100 * d1000 * d10000 * d100000

print(f"answer = {answer}")
