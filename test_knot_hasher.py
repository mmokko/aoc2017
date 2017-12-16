from unittest import TestCase
from day10 import KnotHasher


class TestKnotHasher(TestCase):
    def test_calc(self):
        sut = KnotHasher(5, [3, 4, 1, 5])
        self.assertEqual(12, sut.calc())

    def test_hash1(self):
        sut = KnotHasher(256, '')
        self.assertEqual('a2582a3a0e66e6e86e3812dcb672a272', sut.hash())

    def test_hash2(self):
        sut = KnotHasher(256, 'AoC 2017')
        self.assertEqual('33efeb34ea91902bb2f59c9920caa6cd', sut.hash())

    def test_hash3(self):
        sut = KnotHasher(256, '1,2,3')
        self.assertEqual('3efbe78a8d82f29979031a4aa0b16a9d', sut.hash())

    def test_hash4(self):
        sut = KnotHasher(256, '1,2,4')
        self.assertEqual('63960835bcdc130f0b66d7ff4f6a5a8e', sut.hash())
