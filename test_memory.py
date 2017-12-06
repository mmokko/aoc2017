from unittest import TestCase
from day6 import Memory


class TestMemory(TestCase):
    def test_reallocate(self):
        input_values = [0, 2, 7, 0]
        sut = Memory(input_values)
        self.assertEqual(5, sut.reallocate())

    def test_reallocate_with_iteration_2(self):
        input_values = [0, 2, 7, 0]
        sut = Memory(input_values, 2)
        self.assertEqual(4, sut.reallocate())
