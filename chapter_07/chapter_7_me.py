"""python crash course chapter 7"""

# how the input() function works

message = input("Tell me something and I will repeat it back to you ")
print(message)

# writing clear prompts
name = input("Please enter your name: ")
print("\nHello, " + name + "!")

prompt = "If you tell us who you are, we can personalise the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

# using int() to accept numerical input

age = input("How old are you? ")
age = int(age)
age >= 18

height = input("How tall are you in inches? ")
height = int(height)

if height >= 48:
    print("You are tall enough to ride!")
else:
    print("Sorry, you are not tall enough to ride.")

# the modulo operator

number = input("What is you number? ")
number = int(number)

if number % 2 == 0:
    outcome = "even!"
else:
    outcome = "odd!"

print(f"\nYour number, {number}, is {outcome}")

# while loops

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "Tell me something and I will repeat it back to you "
prompt += "\nEnter 'quit' to end the program. "

message = input(prompt)

while message != 'quit':
    message = input()
    if message != 'quit':
        print(message)

prompt = "Tell me something and I will repeat it back to you "
prompt += "\nEnter 'quit' to end the program. "

active = True

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# using break to exit a loop

prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(f"I would love to visit {message}.")

# using continue in a loop

number = 0

while number < 10:
    number += 1
    if number % 2 == 0:
        continue

    print(number)

# avoiding infinite loops

x = 1

while x <= 5:
    print(x)
    # x += 1
    # if you omit this, it'll just run "1 forever"

# using a while loop with lists and dictionaries
# moving items from one list to another

unconfirmed_users = ["strawberry", "cherry", "blueberry"]
confirmed_users = []

while unconfirmed_users:
    user = unconfirmed_users.pop()
    confirmed_users.append(user)
    print(f"{user.title()} has been confirmed")

print(unconfirmed_users)
print(confirmed_users)

# removing all instances of specific values from a list

pets = ["dog", "cat", "rabbit", "cat", "mouse", "cat"]

print(pets)

while "cat" in pets:
    pets.remove("cat")

print(pets)

# filling a dictionary with user input

responses = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    response = input("Which party do you want to vote for?")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (Y/N) ")
    if repeat == "N":
        polling_active = False

print("\n--- Poll Results ---\n")
for name, response in responses.items():
    print(f"{name} would like to vote for {response}.")
