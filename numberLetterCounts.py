""" Problem 17 """

def number_letters(n):
    """ Returns the number of letters in the number exclude spaces and - """
    # print(f"number_letters called with n = {n}")
    if n == 0 : return 0
    if n == 1 : return 3
    if n == 2 : return 3
    if n == 3 : return 5
    if n == 4 : return 4
    if n == 5 : return 4
    if n == 6 : return 3
    if n == 7 : return 5
    if n == 8 : return 5
    if n == 9 : return 4
    if n == 10 : return 3
    if n == 11 : return 6
    if n == 12 : return 6
    if n == 13 : return 8
    if n == 14 : return 8
    if n == 15 : return 7
    if n == 16 : return 7
    if n == 17 : return 9
    if n == 18 : return 8
    if n == 19 : return 8
    if n == 20 : return 6
    if n == 30 : return 6
    if n == 40 : return 5
    if n == 50 : return 5
    if n == 60 : return 5
    if n == 70 : return 7
    if n == 80 : return 6
    if n == 90 : return 6
    # Add 7 for "hundred"
    if n == 100 : return number_letters(1) + 7
    if n == 200 : return number_letters(2) + 7
    if n == 300 : return number_letters(3) + 7
    if n == 400 : return number_letters(4) + 7
    if n == 500 : return number_letters(5) + 7
    if n == 600 : return number_letters(6) + 7
    if n == 700 : return number_letters(7) + 7
    if n == 800 : return number_letters(8) + 7
    if n == 900 : return number_letters(9) + 7
    if n == 1000 : return number_letters(1) + 8

    if n < 100:
        tens_digit = n // 10
        units_digit = n % 10
        return number_letters(tens_digit * 10) + number_letters(units_digit)

    if n < 1000:
        hundreds_digit = n // 100
        remainder = n%100
        if remainder < 20:
            return number_letters(hundreds_digit * 100) + 3 + number_letters(remainder)
        else :
            tens_digit = (n - (hundreds_digit*100)) // 10
            units_digit = n % 10
            return number_letters(hundreds_digit * 100) + 3 +  number_letters(tens_digit * 10) + number_letters(units_digit)

n = 110
print(f"Number of letters in {n} = {number_letters(n)}")

sum = 0
for i in range(1, 1001):
    sum += number_letters(i)

print(f"Answer = {sum}")