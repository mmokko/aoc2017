from day7_input import INPUT
import re


class Node(object):
    def __init__(self, info='', children=''):
        self.name = ''
        self.weight = 0
        self._parse_name(info)
        self._children_names = [child.replace(',', '') for child in children.split()]
        self.parent = None
        self.children = list()

    def _parse_name(self, info):
        try:
            (name, weight) = info.split()
            self.name = name.replace(',', '')
            weight = re.search('\d+', weight).group()
            if weight:
                self.weight = int(weight)
        except ValueError:
            # ignore empty strings
            pass

    def is_child(self, node):
        if node.name in self._children_names:
            return True
        return False

    def add_child(self, node):
        if self.is_child(node):
            self.children.append(node)
            node.add_parent(self)

    def add_parent(self, node):
        self.parent = node


class TreeCreator(object):
    def __init__(self, programs):
        self._tree = Node()
        self._programs = programs

    def _parse_lines(self, lines):
        nodes = list()
        for line in lines:
            if '->' in line:
                (info, children) = line.split('->')
            else:
                info = line
                children = ''
            node = Node(info, children)
            nodes.append(node)
        return nodes

    def _find_root(self, nodes):
        for node in nodes:
            is_child = False
            for n in nodes:
                if n.is_child(node):
                    is_child = True
            if not is_child:
                return node

    def _parse_nodes(self, nodes):
        root = self._find_root(nodes)
        self._tree = root
        nodes.remove(root)
        while nodes:
            # get first node
            node = nodes[0]
            nodes.remove(node)
            # check if root is the parent
            root.add_child(node)
            # find parent from other nodes
            for n in nodes:
                n.add_child(node)

    def create(self):
        lines = self._programs.split('\n')
        nodes = self._parse_lines(lines)
        self._parse_nodes(nodes)

    def get_base_node(self):
        return self._tree


def main():
    tree = TreeCreator(INPUT)
    tree.create()
    print(tree.get_base_node().name)


if __name__=='__main__':
    main()
