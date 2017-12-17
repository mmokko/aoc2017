from unittest import TestCase
from day11 import HexFinder


class TestHexFinder(TestCase):
    def test_steps_to_origo1(self):
        sut = HexFinder('ne,ne,ne')
        sut.travel()
        self.assertEqual(3, sut.steps_to_origo())

    def test_steps_to_origo1(self):
        sut = HexFinder('ne,ne,sw,sw')
        sut.travel()
        self.assertEqual(0, sut.steps_to_origo())

    def test_steps_to_origo1(self):
        sut = HexFinder('ne,ne,s,s')
        sut.travel()
        self.assertEqual(2, sut.steps_to_origo())

    def test_steps_to_origo1(self):
        sut = HexFinder('se,sw,se,sw,sw')
        sut.travel()
        self.assertEqual(5, sut.steps_to_origo())
