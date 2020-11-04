import math


def print_hi(name, age):
    username = input("what's your name ?")
    print("Hi " + username)


def maximum():
    a = input("Enter a number")
    b = input("Enter a number")
    c = input("Enter a number")
    number = max(a, b, c)
    print(number)


def peer_or_odd():
    number = input("Enter a number")
    if int(number) % 2 == 0:
        print("your number is peer")
    else:
        print("your number is odd")


def major_or_minor():
    age = int(input("How old are you"))
    if age >= 18:
        print("You are major")
    else:
        print("You are minor")


def first_hundred():
    for i in range(100):
        print(i)


def sum_until_number():
    n = int(input("Enter a number"))
    sum = 0
    for i in range(n):
        sum += i
    print(sum)


def sum_str():
    str = ""
    n = int(input("Enter a number"))
    for i in range(n):
        str += '!'
    print(str)


def circle():
    ray = int(input("Enter a number"))
    area = math.pi * (ray * ray)
    print("area : " + str(area))
    perimeter = ray * ray
    print("perimeter : " + str(perimeter))


def divisors():
    divisors = []
    number = int(input("Enter a number"))
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    print(divisors)


def multiplication_table():
    number = int(input("Enter a number"))
    for i in range(1, 11):
        print(number, 'x', i, '=', number * i)


def all_multiplication_tables():
    for i in range(1, 10):
        print("multiplication table of " + str(i))
        for j in range(1, 11):
            print(i, 'x', j, '=', i * j)


def rest_and_quotient():
    a = int(input("Enter a number"))
    b = int(input("Enter a number"))
    print("Rest of a / b is " + str(a % b))
    print("Quotient of a / b is + " + str(a // b))


def perfect_square():
    number = int(input("Enter a number"))
    square_root = math.sqrt(number)
    if square_root - square_root == 0:
        print("Your number is a perfect square")


def prime_number():
    number = int(input("Enter a number"))
    divisors = 0
    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            divisors += 1

    if divisors == 0:
        print("It's a prime number")
    else:
        print("It's not a prime number")


if __name__ == '__main__':
    rest_and_quotient()

