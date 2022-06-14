"""python crash course chapter 10"""

# files and exceptions

# with closes the file after use
with open("pi_digits.txt") as file_object:
    contents = file_object.read()

# rstrip removes white space on the right
print(contents.rstrip())

file_path = "pi_million_digits.txt"

with open(file_path) as file_object:
    lines = file_object.readlines()

    pi_string = ""
    for line in lines:
        pi_string += line.strip()

    print(f"{pi_string[:52]}...")
    print(len(pi_string))

birthday = input("Enter your birthday in the format ddmmyy\n")
if birthday in pi_string:
    print("Your birthday is in the first million digits of pi!")
else:
    print("Nope!")

# writing to a file
file_name = "programming.txt"
with open(file_name, "w") as file_object:
    file_object.write("I love programming!")

# exceptions
# print(5/0)

try:
    print(5 / 0)
except:
    print("You can't divide by zero!")

print("Give me two numbers and I'll divide them")
print("Enter 'q' to quit")

# specifying the error
while True:
    first_number = input("What is the first number?\n")
    if first_number == "q":
        break
    try:
        int(first_number)
    except ValueError:
        print("That is not a number please try again")
        first_number = input()
    second_number = input("What is the second number?\n")
    if second_number == "q":
        break
    try:
        int(second_number)
    except ValueError:
        print("That is not a number please try again")
        second_number = input()
    break

try:
    answer = int(first_number) / int(second_number)
    print(f"{first_number} / {second_number} = {answer}")
except ZeroDivisionError:
    print("You can't divide by zero!")


def count_words(filename):
    """Count the approximate number of words in a file"""

    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        pass
        # print(f"Sorry, could not find a file called {filename}")
    else:
        words_list = contents.split()
        words_count = len(words_list)
        print(f"The file {filename} contains approximately {words_count} words.")


# count_words("alice.txt")

books = ["alice.txt", "the peppermint sparrow.txt", "little_women.txt", "moby_dick.txt"]

for book in books:
    count_words(book)

title = "alice in wonderland"
title.split()

#  storing data
#  writing to a json file
import json

numbers = [1, 2, 3, 5, 7, 11, 13]
filename = "numbers.json"
with open(filename, "w") as f:
    json.dump(numbers, f)

with open(filename) as f:
    primes = json.load(f)

print(primes)

username = input("What is your name?\n")
filename = "username.json"
with open(filename, "w") as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}")

filename = "username.json"

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")

import json

filename = "user.json"

try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    print(f"Sorry, we could not find your username")
    username = input("Please create a username\n")
    with open(filename, "w") as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}")
else:
    print(f"Welcome back, {username}!")

# Refactoring

import json


def greet_user():
    """ greet the user by name """

    filename = "user.json"

    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        print(f"Sorry, we could not find your username")
        username = input("Please create a username\n")
        with open(filename, "w") as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}")
    else:
        print(f"Welcome back, {username}!")


greet_user()

greet_user()


def get_stored_username():
    filename = "user.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    filename = "user.json"
    username = input("Please create a username\n")
    with open(filename, "w") as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}")
    return username


def greet_user():
    """ greet the user by name """
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        print(f"Sorry, we could not find your username")
        username = get_new_username()


greet_user()
