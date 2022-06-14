"""python crash course chapter 8"""


# functions
def greet_user():
    """display a simple greeting"""
    print("hello")


greet_user()


# passing information to a function

def greet_user(username):
    """display a simple greeting"""
    username = str(username)
    print(f"hello, {username.title()}")


greet_user("dr wampa")


# positional arguments

def describe_pet(animal_type, pet_name):
    """display info about a pet"""
    animal_type = str(animal_type)
    if animal_type[0] in ["a", "e", "i", "o", "u"]:
        print(f"I have an {animal_type}.")
    else:
        print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet("possum", "piña")

describe_pet("dog", "loki")

describe_pet("anaconda", "pie")

describe_pet(pet_name="fred", animal_type="cat")


# default values

def describe_pet(pet_name, animal_type="dog"):
    """display info about a pet"""
    animal_type = str(animal_type)
    if animal_type[0] in ["a", "e", "i", "o", "u"]:
        print(f"I have an {animal_type}.")
    else:
        print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name="carl", animal_type="emu")


# return values

def get_formatted_name(first_name, last_name):
    """Return a full name neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name("jimmy", "hendrix")
print(musician)


def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a full name neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name("possum", "plows", "mistletoe")
print(musician)


# returning a dictionary

def build_person(first_name, last_name):
    """return a dictionary of information about a person"""
    person = {"first": first_name, "last": last_name}
    return person


musician = build_person("jimmy", "hendrix")
print(musician)


def build_person(first_name, last_name, age=None):
    """return a dictionary of information about a person"""
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person


musician = build_person("jimmy", "hendrix", 44)
print(musician)


# using a fuction with a while loop


def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a full name neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print("Please tell me your name: ")
    print("Enter 'q' any time to quit.")
    f_name = input("First name: ")
    if f_name == "q":
        break
    l_name = input("Last name: ")
    if l_name == "q":
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello, {formatted_name}")


def greet_users(names):
    """ Print a simple greeting to each user in a list """
    for name in names:
        print(f"Hello {name.title()}!")


usernames = ["frog", "rabbit", "onion"]

greet_users(usernames)

# modifying a list in a function
# start with some designs that need to be printed

unprinted_designs = ["phone case", "robot pendant", "dice"]
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}.")
    completed_models.append(current_design)

print("The following models have been printed:")
for model in completed_models:
    print(model)


def printing(unprinted, completed):
    while unprinted:
        current_design = unprinted.pop()
        print(f"Printing model: {current_design}.")
        completed.append(current_design)


def show_completed(completed):
    print("The following models have been printed:")
    for model in completed:
        print(model)


unprinted_designs = ["phone case", "robot pendant", "dice"]
completed_models = []

printing(unprinted_designs[:], completed_models)
show_completed(completed_models)

print(unprinted_designs)


# passing an arbitrary number of arguments
def make_pizza(*toppings):
    """ print the list of toppings that are being requested """
    print("Making a pizza with the folling toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza("pepperoni")
make_pizza("mushrooms", "spinach", "olives")


#  mixing positional and arbitrary arguments

def make_pizza(size, *toppings):
    """ print the list of toppings that are being requested """
    print(f'Making a {size}" pizza with the following toppings:')
    for topping in toppings:
        print(f"- {topping}")


make_pizza(10, "mushrooms", "tomatoes")


# using arbitrary key word arguments

def build_profile(first, last, **user_info):
    """ build a dictionary containing everything we know about a user"""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = build_profile("Possum", "Plows",
                             location="Auckland",
                             age=28)

print(user_profile)


# storing you fuctions in modules
# refer to module_testing

# styling functions
# make sure you have descriptive names
# doc string should describe what function does well

#def function_name(parameter_0, parameter_1="default value"):
