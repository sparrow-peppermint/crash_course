"""python crash course chapters 3 and 4"""

# organising a list
# sorting a list permanently with the sort method
marsupials = ["possum", "wombat", "kangaroo", "koala", "angel"]
marsupials.sort()
print(marsupials)

# sort in reverse order
marsupials.sort(reverse=True)
print(marsupials)

# sorting a list temporarily with the sorted function
marsupials = ["possum", "wombat", "kangaroo", "koala", "angel"]
print("here is the original list")
print(marsupials)
print("here is the sorted list")
print(sorted(marsupials))
print("here is the original list again")
print(marsupials)

# printing a list in reverse order
marsupials.reverse()
print(marsupials)

# finding the length of a list
len(marsupials)

# avoiding index errors when working with lists
print(marsupials[-1])

# looping through an entire list
for marsupial in marsupials:
    print(f"{marsupial.title()}, nice to see you!")
    print(f"I can't wait to see you, {marsupial.upper()}.\n")

print("Thanks for coming everyone!")

# making numerical lists
# using the range function
for value in range(1, 5):
    print(value)

# using range to make a list of numbers
numbers = list(range(1, 6))
print(numbers)
even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

# simple statistics with a list of numbers
numbers = [22, 5, 76, 1, 90, 2, 56]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# list comprehensions
squares = [value ** 2 for value in range(1, 11)]
print(squares)

cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

# working with part of a list
# slicing a list
print(marsupials[-3:])
print("here are the first 3 marsupials on my list")
for marsupial in marsupials[:3]:
    print(marsupial.title())

my_foods = ["chocolate", "almonds", "cherries"]
rosemary_foods = my_foods[:]
print(f"my favourite foods are {my_foods}")
print(f"rosemary's favourite foods are {rosemary_foods}.")

my_foods.append("v energy")
rosemary_foods.append("peanut butter")
print(my_foods)
print(rosemary_foods)

# tuples
# tuple is an immutable list
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

dimensions = (400, 10)
print(dimensions)
