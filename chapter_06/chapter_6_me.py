"""python crash course chapter 6"""

# dictionaries
alien_0 = {"colour": "green", "points": 5}
alien_0["colour"]

new_points = alien_0["points"]
print(f"You just earned {new_points} points")

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

# starting with an empty dictionary
alien_0 = {}
alien_0["colour"] = "green"
alien_0["points"] = 5
print(alien_0)

# modifying values in a dictionary
alien_0 = {"colour": "green"}
print(f"The alien is {alien_0['colour']}")

alien_0["colour"] = "yellow"
print(f"The alien is now {alien_0['colour']}")

alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"Original position: {alien_0['x_position']}")

# move the alien to the right
# determine how far to move the alien based on its current speed

alien_0["speed"] = "fast"

if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0["x_position"] += x_increment
print(f"The new position will be: {alien_0['x_position']}")

# removing key value pairs
print(alien_0)
del alien_0["speed"]

# dictionary of similar objects
favourite_languages = {
    "pineapple": "python",
    "apple": "swift",
    "chickpea": "r"
}

print(f"Chickpea's favourite language is: {favourite_languages['chickpea'].title()}")

#  using get() to access vaules

alien_0 = {"colour": "green", "speed": "slow"}

point_value = alien_0.get("points", "no point value assigned")
print(point_value)

# looping through a dictionary
# looping through all key value pairs

user_0 = {
    "username": "pina",
    "first_name": "pine",
    "last_name": "apple"
}

for k, v in user_0.items():
    print(f"\nKey: {k}")
    print(f"\nValue: {v}")

for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language}")

for p in favourite_languages.values():
    print(p)

friends = ["pineapple", "chickpea"]
for name in favourite_languages.keys():
    print(f"Hi {name.title()}!")

    if name in friends:
        language = favourite_languages[name]
        print(f"{name.title()}, I see you love {language}")

if "erin" not in favourite_languages.keys():
    print("Erin, please take our poll!")

# looping through a dictionaries keys in a paticular order
for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# looping through values
for language in set(favourite_languages.values()):
    print(language)

# build a set
languages = {"python", "r", "python", "c"}
languages

# nesting
# a list of dictionaries
alien_0 = {"colour": "green", "points": 1}
alien_1 = {"colour": "blue", "points": 2}
alien_2 = {"colour": "red", "points": 3}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

aliens = []

for alien_number in range(30):
    new_alien = {"colour": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien["colour"] == "green":
        alien["colour"] = "yellow"
        alien["points"] = 10
        alien["speed"] = "medium"
    elif alien["colour"] == "yellow":
        alien["colour"] = "red"
        alien["points"] = 15
        alien["speed"] = "fast"

for alien in aliens[:5]:
    print(alien)

#   print(new_alien)

# print(len(aliens))

# a list in a dictionary
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"]
}

print(f"You ordered a {pizza['crust']} crust pizza with the following toppings:")
for topping in pizza["toppings"]:
    print(topping.title())

favourite_languages = {
    "melon": ["python"],
    "peanut": ["swift", "C"],
    "lemon": ["R"],
    "rabbit": ["python", "R"]
}

for person, languages in favourite_languages.items():
    if len(languages) == 1:
        print(f"{person.title()}'s favourite language is:")
    else:
        print(f"{person.title()}'s favourite languages are:")
    for language in languages:
        print(language)
    print("\n")

# a dictionary in a dictionary

users = {
    "bear": {
        "first name": "bear",
        "last name": "grizzle",
        "location": "california"
    },
    "otter": {
        "first name": "otter",
        "last name": "ocean",
        "location": "arkansas"
    }
}

for user, info in users.items():
    print(f"\nUsername: {user}")
    full_name = f"{info['first name']} {info['last name']}"
    location = info["location"]
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
