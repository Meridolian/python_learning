

def letter_generator(nb):
    output = ""
    letters = "abcdefghijklmnopqrstuvwxyz"
    letters = list(letters)
    for letter in letters:
        output += letter * nb
    print(output)