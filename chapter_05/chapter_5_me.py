"""python crash course chapter 5"""

colours = ["red", "green", "blue", "purple", "black", "yellow", "orange"]

for colour in colours:
    if colour == "yellow":
        print(colour.upper())
    else:
        print(colour.title())

car = "Audi"
car.lower() == "audi"
print(car)

# checking for inequality
requested_topping = "mushrooms"
if requested_topping != "anchovies":
    print("Hold the anchovies!")

# numerical comparisons
age = 18
age == 18

answer = 17
if answer != 42:
    print("incorrect answer")

age = 19
age < 21
age <= 21
age > 21
age >= 21

# checking multiple conditions
age_0 = 21
age_1 = 18
(age_0 >= 21) and (age_1 >= 21)

(age_0 >= 21) or (age_1 >= 21)

requested_toppings = ["mushrooms", "onions", "pineapple"]

"pepper" in requested_toppings

# checking whether a value is not in a list
banned_users = ["andrew", "miles", "wes"]
user = "maude"

if user not in banned_users:
    print(f"{user.title()}, you can post a response")

# boolean experssions
game_active = True
can_edit = False

# simple if statements
age = 17
if age >= 18:
    print("You're old enough to vote")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote")
    print("Register to vote when you turn 18")

#  the if, elif, else chain
age = 6
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 60:
    price = 35
elif age >= 60:
    price = 40
# else:
#   price = 40

print(f"Your admission cost is ${price}.")

# testing multiple conditions

if "mushrooms" in requested_toppings:
    print("adding mushrooms")
if "pepperoni" in requested_toppings:
    print("adding pepperoni")
if "onions" in requested_toppings:
    print("adding onions")

print("\nFinished Making Your Pizza!")

# checking for special items

for topping in requested_toppings:
    if topping == "onions":
        print("Sorry we're out of Onions")
    else:
        print(f"adding {topping}")

print("\nFinished making your Pizza!")

# checking that a list is not empty

requested_toppings = []

if requested_toppings:
    for topping in requested_toppings:
        print("Adding " + topping)
    print("Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# using multiple lists
available_toppings = ["mushrooms", "spinach", "tomatoes", "olives", "pineapple"]
requested_toppings = ["spinach", "baccon", "chicken", "tomatoes"]

for topping in requested_toppings:
    if topping in available_toppings:
        print("Adding " + topping)
    else:
        print(f"Sorry, {topping} is not available")

print("Finished Making your pizza")
