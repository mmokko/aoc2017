from unittest import TestCase
from day2 import CheckSumCalculator


class TestCheckSumCalculator(TestCase):
    def test_calculate_diff(self):
        cs = '''5 1 9 5
        7 5 3
        2 4 6 8'''
        self.csc = CheckSumCalculator(cs)
        self.assertEqual(18, self.csc.calculate_diff())

    def test_calculate_div(self):
        cs = '''5 9 2 8
        9 4 7 3
        3 8 6 5'''
        self.csc = CheckSumCalculator(cs)
        self.assertEqual(9, self.csc.calculate_div())
