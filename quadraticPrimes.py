"""Problem 27"""
from eulerlib.operations import is_prime, get_list_of_primes


def get_prime_score(a, b):
    score = 0
    for n in range(0, b):
        if is_prime((n * n) + (a * n) + b):
            score += 1
            # print("The following is prime", (n*n) + (a*n) + b)
        else:
            break
    return score


def main():
    bound_list = get_list_of_primes(2001)
    possibilities_of_b = get_list_of_primes(1000)

    # possibilities_of_b = [41]
    for b in possibilities_of_b:
        b_score = 0
        selected_a = 0
        for a in range(-1 * 1000, 1000):
            if (1 + a + b) in bound_list:
                score = get_prime_score(a, b)
                if score > b_score:
                    b_score = score
                    selected_a = a
        print(
            "Found a match with a = ", selected_a, "and b =", b, ". Score = ", b_score
        )


main()
# print(get_prime_score(-57, 853))
