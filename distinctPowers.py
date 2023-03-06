"""Problem 29"""


def main():
    output_list = []

    for a in range(2, 100 + 1):
        for b in range(2, 100 + 1):
            result = a**b
            if result not in output_list:
                output_list.append(result)

    print(len(output_list))


main()
