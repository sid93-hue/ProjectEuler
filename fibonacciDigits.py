"""Problem 25"""

from eulerlib.operations import num_digits


def main():
    F1 = 1
    F2 = 1
    n = 2

    while num_digits(F1) < 1000:
        F1 = F2 + F1
        F2 = F1 + F2
        n += 2

    print("num_digits of F1 = ", num_digits(F1))
    print("num_digits of F2 = ", num_digits(F2))
    print("Answer = ", n - 1, "or", n - 2)


main()
