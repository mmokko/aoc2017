from unittest import TestCase
from day5 import Maze


class TestMaze(TestCase):
    def test_empty_maze(self):
        sut = Maze([])
        self.assertEqual(0, sut.find_way_out())

    def test_find_way_out_of_maze(self):
        sut = Maze([0, 3, 0, 1, -3])
        self.assertEqual(5, sut.find_way_out())

    def test_find_way_out_if_maze_with_optional_incr(self):
        sut = Maze([0, 3, 0, 1, -3])
        sut.use_optional_increment = True
        self.assertEqual(10, sut.find_way_out())
