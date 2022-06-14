"""python crash course chapter 10"""


def get_full_name(first_name, last_name):
    return f"{first_name.title()} {last_name.title()}"


# from name_function import get_full_name

print("Enter q at any time to quit")

while True:
    first = input("Please give me a first name\n")
    if first == "q":
        break
    last = input("Please give me a last name\n")
    if last == "q":
        break

    formatted_name = get_full_name(first, last)
    print(f"Neatly formatted name is {formatted_name}\n")

# Unit Tests and Test cases

import unittest

from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()

import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """ Tests the name function """

    def test_first_last_name(self):
        """ do names like janice joplyn work """
        formatted_name = get_formatted_name("janice", "joplyn")
        self.assertEqual(formatted_name, "Janice Joplyn")


if __name__ == '__main__':
    unittest.main()
