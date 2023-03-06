"""Problem 23"""


def is_abundant(input_number):
    result = False
    if sum_of_divisors(input_number) > input_number:
        result = True
    return result


def sum_of_divisors(input_number):
    output_sum = 1
    for divisor in range(2, int(input_number / 2) + 2):
        if input_number % divisor == 0:
            output_sum += divisor

    return output_sum


def list_of_abundant_numbers():
    abundant_numbers = []
    for i in range(12, 28124):
        if is_abundant(i):
            abundant_numbers.append(i)

    return abundant_numbers


def is_sum_of_2_elements_in_list(i, input_list):
    result = False
    for item in input_list:
        if (i - item) in input_list:
            result = True
            # print("i = ", i, "can be expressed as the sum of", i - item, "and", item)
            break
    return result


def main():
    print("Starting program...")

    abundant_numbers = list_of_abundant_numbers()

    # for i in range(0, len(abundant_numbers)) :
    #    print(abundant_numbers[i])
    output_sum = 0

    for i in range(1, 28124):
        if is_sum_of_2_elements_in_list(i, abundant_numbers) == False:
            output_sum += i
            # print(i, "cannot be expressed as the sum of two abundant numbers")

    print(output_sum)


main()
