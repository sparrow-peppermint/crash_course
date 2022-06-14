# -*- coding: utf-8 -*-
"""python crash course chapters 1 and 2"""

message = "hello world!"

print(message)

message = "pineapples"

print(message)
"this"

name = "sparrow peppermint"

print(name.title())

print(name.upper())

print(name.lower())

first_name = "sparrow"
last_name = "peppermint"
full_name = f"{first_name} {last_name}"
print(full_name)

full_name = first_name + " " + last_name
print(full_name)

print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"

print(message)

print("python")

print("\tpython")

print("languages:\npython\nc\njavascript")

favourite_language = "python "

print(favourite_language)

favourite_language.strip()

3 ** 2

2 + 3 * 4

(2 + 3) * 4

0.1 + 0.1

3 * 0.1

3.0 * 0.1

4 / 2

universe_age = 14_000_000_000
print(universe_age)

x, y, z = 0, 5, 19
print(z)

# Say hello to everyone
print("hello")

# creating a list
bicycles = ["trek", "canodale", "peanut", "healthy"]
print(bicycles)

# accessing elements in a list
print(bicycles[-1].title())

message = f"my first bicycle was a {bicycles[2].title()}."
print(message)

# changing elements in a list
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles[0] = "sidecar"
print(motorcycles)

# appending elements to the end of a list
motorcycles.append("ducati")
print(motorcycles)

motorcycles = []
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("egg")
print(motorcycles)

# insert elements into list
motorcycles.insert(0, "ducati")
print(motorcycles[0])

# delete elements from a list
del motorcycles[0]
print(motorcycles)

#  using the pop method
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop(0)
print(f"the last motorcycle I owned was a {last_owned.title()}.")

print(motorcycles)

motorcycles = []
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("egg")

print(motorcycles)
motorcycles.remove("yamaha")
print(motorcycles)

too_expensive = "egg"
motorcycles.remove(too_expensive)
print(motorcycles)
