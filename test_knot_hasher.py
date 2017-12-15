from unittest import TestCase
from day10 import KnotHasher


class TestKnotHasher(TestCase):
    def test_hash(self):
        sut = KnotHasher(5, [3, 4, 1, 5])
        self.assertEqual(12, sut.hash())
