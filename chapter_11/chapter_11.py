import unittest
from name_function import get_formatted_name
class NamesTestCase(unittest.TestCase):
  """ Tests the name function """

  def test_first_last_name(self):
    """ do names like janice joplyn work """
    formatted_name = get_formatted_name("janice", "joplyn")
    self.assertEqual(formatted_name, "Janice Joplyn")

  def test_first_middle_last_name(self):
    """ do names like sparrow possum peppermint work"""
    formatted_name = get_formatted_name("sparrow", "peppermint", "possum plows")
    self.assertEqual(formatted_name, "Sparrow Possum Plows Peppermint")

if __name__ == '__main__':
  unittest.main()


