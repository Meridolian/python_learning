

def luckyNumber(nb):
    number = nb
    while number > 10:
        digits = list(str(number))
        number = 0
        print(digits)
        for digit in digits:
            number += int(digit) * int(digit)

    print(number)
    if number == 1:
        print("Your number is a lucky number")
    else:
        print("Your number is not a lucky number")
