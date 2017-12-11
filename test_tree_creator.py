from unittest import TestCase
from day7 import TreeCreator


INPUT = '''pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)'''


class TestTreeCreator(TestCase):
    def test_create_tree(self):
        sut = TreeCreator(INPUT)
        sut.create()
        self.assertEqual('tknk', sut.get_base_node().name)

    def test_find_unbalanced_node(self):
        sut = TreeCreator(INPUT)
        sut.create()
        self.assertEqual('ugml', sut.find_unbalanced_node().name)
        self.assertEqual(60, sut.calculate_correct_weight_for_unbalanced_node(sut.find_unbalanced_node()))
