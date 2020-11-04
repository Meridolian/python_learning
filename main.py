
def print_hi(name, age):
    print username
    username = input("what's your name ?")
    print("Hi " + username)

    
def exo3():
    a = input("Enter a number")
    b = input("Enter a number")
    number = max(a, b)
    print(number)


def exo4() :
    peer_or_odd = input("Enter a number")
    if int(peer_or_odd) % 2 == 0:
        print("your number is peer")
    else:
        print("your number is odd")


if __name__ == '__main__':
    print_hi('Meridolian', '22')

