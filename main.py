import math

def print_hi(name, age):
    username = input("what's your name ?")
    print("Hi " + username)


# Exercise 3
def maximum():
    a = input("Enter a number")
    b = input("Enter a number")
    c = input("Enter a number")
    number = max(a, b, c)
    print(number)


# Exercise 4
def peer_or_odd():
    number = input("Enter a number")
    if int(number) % 2 == 0:
        print("your number is peer")
    else:
        print("your number is odd")


# Exercise 5
def major_or_minor():
    age = int(input("How old are you"))
    if age >= 18:
        print("You are major")
    else:
        print("You are minor")


# Exercise 6
def first_hundred():
    for i in range(100):
        print(i)


# Exercise 7
def sum_until_number():
    n = int(input("Enter a number"))
    sum = 0
    for i in range(n):
        sum += i
    print(sum)


# Exercise 8
def sum_str():
    str = ""
    n = int(input("Enter a number"))
    for i in range(n):
        str += '!'
    print(str)


# Exercise 9
def circle():
    ray = int(input("Enter a number"))
    area = math.pi * (ray * ray)
    print("area : " + str(area))
    perimeter = ray * ray
    print("perimeter : " + str(perimeter))


# Exercise 10
def divisors():
    divisors = []
    number = int(input("Enter a number"))
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    print(divisors)


# Exercise 11
def multiplication_table():
    number = int(input("Enter a number"))
    for i in range(1, 11):
        print(number, 'x', i, '=', number * i)


# Exercise 12
def all_multiplication_tables():
    for i in range(1, 10):
        print("multiplication table of " + str(i))
        for j in range(1, 11):
            print(i, 'x', j, '=', i * j)


# Exercise 13
def rest_and_quotient():
    a = int(input("Enter a number"))
    b = int(input("Enter a number"))
    print("Rest of a / b is " + str(a % b))
    print("Quotient of a / b is + " + str(a // b))


# Exercise 14
def perfect_square():
    number = int(input("Enter a number"))
    square_root = math.sqrt(number)
    if square_root - square_root == 0:
        print("Your number is a perfect square")


# Exercise 15
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


# Exercise 16
def char_in_string():
    s = "PYTHON"
    for i in range(len(s)):
        print(s[i])


# Exercise 17
def char_iteration():
    iteration = []
    s = "itescia.fr"
    for i in range(len(s)):
        if len(iteration) < 1:
            iteration.append([s[i], 1])
        else:
            new_char = True
            for j in range(len(iteration)):
                if s[i] == iteration[j][0]:
                    iteration[j][1] += 1
                    new_char = False
            if new_char:
                iteration.append([s[i], 1])
    print(iteration)


if __name__ == '__main__':
    char_iteration()

