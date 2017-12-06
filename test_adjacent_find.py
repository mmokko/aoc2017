from unittest import TestCase
from day1 import adjacent_find


class TestAdjacentFind(TestCase):
    def test_inputs(self):
        self.assertEqual(3, adjacent_find('1122'))
        self.assertEqual(4, adjacent_find('1111'))
        self.assertEqual(0, adjacent_find('1234'))
        self.assertEqual(9, adjacent_find('91212129'))
