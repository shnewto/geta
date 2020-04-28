import unittest
from some.name import generateName, NameType


class TestGenerateName(unittest.TestCase):

    def test_get_first_name(self):
        first_name = generateName(NameType.FIRST)
        self.assertEqual(1, len(first_name.split(" ")))

    def test_get_last_name(self):
        last_name = generateName(NameType.LAST)
        self.assertEqual(1, len(last_name.split(" ")))

    def test_get_full_name(self):
        last_name = generateName(NameType.FULL)
        self.assertEqual(2, len(last_name.split(" ")))
