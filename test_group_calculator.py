from unittest import TestCase
import day9


class TestGroupCalculator(TestCase):
    def test_calculate_groups(self):
        self.assertEqual(1, day9.calc('{}'))
        self.assertEqual(6, day9.calc('{{{}}}'))
        self.assertEqual(5, day9.calc('{{},{}}'))
        self.assertEqual(16, day9.calc('{{{},{},{{}}}}'))
        self.assertEqual(1, day9.calc('{<a>,<a>,<a>,<a>}'))
        self.assertEqual(9, day9.calc('{{<ab>},{<ab>},{<ab>},{<ab>}}'))
        self.assertEqual(9, day9.calc('{{<!!>},{<!!>},{<!!>},{<!!>}}'))
        self.assertEqual(3, day9.calc('{{<a!>},{<a!>},{<a!>},{<ab>}}'))

    def test_calculate_garbage(self):
        self.assertEqual(0, day9.calc_carbage('{}'))
        self.assertEqual(17, day9.calc_carbage('<random characters>'))
        self.assertEqual(3, day9.calc_carbage('<<<<>'))
        self.assertEqual(2, day9.calc_carbage('<{!>}>'))
        self.assertEqual(0, day9.calc_carbage('<!!>'))
        self.assertEqual(0, day9.calc_carbage('<!!!>>'))
        self.assertEqual(10, day9.calc_carbage('<{o"i!a,<{i<a>'))
