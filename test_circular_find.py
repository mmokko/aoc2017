from unittest import TestCase
from day1 import circular_find


class TestCircularFind(TestCase):
    def test_inputs(self):
        self.assertEqual(6, circular_find('1212'))
        self.assertEqual(0, circular_find('1221'))
        self.assertEqual(4, circular_find('123425'))
        self.assertEqual(12, circular_find('123123'))
        self.assertEqual(4, circular_find('12131415'))
