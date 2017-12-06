from unittest import TestCase
from day3 import SpiralMemory


class TestSpiralMemory(TestCase):
    def test_calculate_dist1(self):
        sut = SpiralMemory(1)
        self.assertEqual(0, sut.distance())

    def test_calculate_dist12(self):
        sut = SpiralMemory(12)
        self.assertEqual(3, sut.distance())

    def test_calculate_dist23(self):
        sut = SpiralMemory(23)
        self.assertEqual(2, sut.distance())

    def test_calculate_dis1024(self):
        sut = SpiralMemory(1024)
        self.assertEqual(31, sut.distance())

    def test_value6(self):
        sut = SpiralMemory(6)
        self.assertEqual(10, sut.value())

    def test_value351(self):
        sut = SpiralMemory(351)
        self.assertEqual(362, sut.value())

    def test_value806(self):
        sut = SpiralMemory(806)
        self.assertEqual(880, sut.value())

