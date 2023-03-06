"""Problem 30"""


def digits(n):
    output_list = []
    temp = n

    while temp != 0:
        output_list.append(temp % 10)
        temp = int(temp / 10)

    output_list.reverse()

    return output_list


def is_sum_of_powers_of_5(n):
    result = False
    sum_of_digits = 0

    digits_list = digits(n)

    for digit in digits_list:
        sum_of_digits += digit**5

    if sum_of_digits == n:
        result = True

    return result


def main():
    answer = 0
    for n in range(2, 999999):
        if is_sum_of_powers_of_5(n):
            print("The following can be written as the sum of powers of 5 : ", n)
            answer += n

    print("Answer = ", answer)


main()
