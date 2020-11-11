import math
import re
import random
import string


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
    for i in s:
        print(i)


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


# Exercise 18
def string_contains_char():
    char_positions = []
    s = input("Enter a sentence or a word")
    for i in range(len(s)):
        if s[i] == "a":
            char_positions.append(i + 1)
    if len(char_positions) > 0:
        for i in range(len(char_positions)):
            print("The char 'a' is at the position " + str(char_positions[i]))
    else:
        print("There's not 'a' in your sentence")


# Exercise 19
def array_length_and_list_char():
    array = ["laptop", "iphone", "tablet"]
    for i in range(len(array)):
        output = ""
        for j in range(len(array[i])):
            output += array[i][j] + " "
        output += "--> length = " + str(len(array[i]))
        print(output)


# Exercise 20
def split_first_and_last_char():
    s = input("Enter a sentence or a word")
    first_char = s[0]
    last_char = s[len(s) - 1]
    s.replace(first_char, last_char)
    print(s)


# Exercise 21
def vowels_in_string():
    s = "anticonstitutionellement"
    vowels = re.findall(r"[aeiouy]", s)
    print("The string '" + s + "' contains " + str(len(vowels)) + " vowels")


# Exercise 22
def first_word_in_string():
    s = "Python est un merveilleux langage de programmation"
    print("The first word of your string is '" + str(s.split(' ')[0]) + "'")


# Exercise 23
def file_extension_string():
    filename = str(input("Enter a file name"))
    print("The extension of your file is ." + filename.split('.', len(filename))[1])
    # work


# Exercise 24
def palindrome_string():
    s = str(input("Enter a word"))
    if s == s[::-1]:
        print("Your word is a palindrome !")
    else:
        print("Your word is not a palindrome")


# Exercise 25
def reverse_string():
    s = str(input("Enter a word"))
    print(s[::-1])


# Exercise 26
def get_words_beginning_by(first_char):
    s = str(input("Enter a sentence"))
    words = s.split(' ')
    output = ""
    for word in words:
        if word[0] == str(first_char):
            output += word + " "
    print("Here words beginning by " + first_char + " --> " + output)


# Exercise 27
def longest_word():
    s = str(input("Enter a sentence"))
    words = s.split(' ')
    print("The longest word in your sentence is " + max(words, key=len))


# Exercise 28
def is_empty():
    # case list
    array = ["1", "2"]
    if len(array) < 1:
        print("Your array is empty")
    else:
        print("Your array is not empty and his length is " + str(len(array)))

    # case string
    s = str(input("Enter a string"))
    if len(s) < 1:
        print("Your string is empty")
    else:
        print("Your string is not empty and her length is " + str(len(s)))


# Exercise 29
def remove_list_duplicates():
    array = [1, 1, 2, 6, 8, 9, 3, 3, 4, 5, 2]
    print(list(set(array)))


# Exercise 30
def compare_lists():
    a = [1, 5, 3, 9]
    b = [3, 6, 8, 7]
    print(set(a) & set(b))


# Exercise 31
def peer_and_odd_in_list():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    peers = []
    odds = []
    for i in array:
        if i % 2 == 0:
            peers.append(i)
        else:
            odds.append(i)
    print("peers --> " + str(peers))
    print("odds --> " + str(odds))


# Exercise 32
def shuffle_list():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(array)
    print(array)


# Exercise 33
def peers_index_in_string():
    s = str(input("Enter a sentence"))
    peers = []
    for i in range(len(s)):
        if i % 2 == 0:
            peers.append(s[i])
    print(peers)


# Exercise 34
def get_great_notes():
    notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]
    great_notes = []
    for note in notes:
        if note >= 10:
            great_notes.append(note)
    print(great_notes)


# Exercise 35
def occurrence_words():
    s = str(input("Enter a sentence"))
    words = s.split(' ')
    occurrences = {}
    for x in words:
        if x.lower() not in occurrences.keys():
            occurrences[x.lower()] = 1
        else:
            occurrences[x.lower()] = occurrences[x.lower()] + 1
    print(occurrences)


# Exercise 36
def remove_duplicate_spaces():
    s = "Hi, my name  is  Meridolian"
    s = ' '.join(s.split())
    print(s)


# Exercise 37
def match_words():
    s1 = "hi, my name is Meridolian"
    s2 = "Hello I'm Meridolian"
    words1 = s1.split(' ')
    words2 = s2.split(' ')
    output = set(words1) & set(words2)
    print(output)


# Exercise 38
def split_first_last_words():
    s = "Python est un langage de programmation"
    words = s.split(' ')
    output = ""
    for i in range(len(words)):
        if i == 0:
            output += words[len(words) - 1] + " "
        elif i == len(words) - 1:
            output += words[0]
        else:
            output += words[i] + " "
    print(output)


# Exercise 39
def count_words():
    s = str(input("Enter a sentence"))
    words = re.sub('['+string.punctuation+']', '', s).split()
    print(len(words))


# Exercise 41
def divided_numbers(number_list, n):
    output = []
    for i in number_list:
        if i % n == 0:
            output.append(i)
    return output

# Exercise 42
def number_occurences(l, x):
    output = 0
    for i in l:
        if i == x:
            output += 1
    return output


# Exercise 43
def insert_stars(s):
    chars = list(s)
    output = ""
    for i in range(len(chars)):
        if i == 0:
            output += chars[i]
        else:
            output += "*" + chars[i]
    return output


# Exercise 44
def all_upper(l):
    output = []
    for i in range(len(l)):
        output.append(l[i].upper())
    return output

# Exercise 45
def char_lower_or_upper(s):
    lowers = 0
    uppers = 0
    for char in s:
        if char.islower():
            lowers += 1
        elif char.isupper():
            uppers += 1
    return lowers, uppers


# Exercise 46
def ten_base_number(n):
    result = set([])
    while (n > 0):
        result |= {n % 10}
        n = n // 10
    return result


# Exercise 47
def words_matches(text1, text2):
    words1 = text1.split(' ')
    words2 = text2.split(' ')
    result = set(words1) & set(words2)
    print(result)


if __name__ == '__main__':
    text1 = "Python est un langage de programmation"
    text2 = "Python est orienté objet"
    words_matches(text1, text2)

