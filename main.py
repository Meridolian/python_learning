
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


if __name__ == '__main__':
    maximum()

