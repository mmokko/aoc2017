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

    def get_weight(self):
        weight = self.weight
        for child in self.children:
            weight += child.get_weight()
        return weight

    def get_balanced_weight(self):
        weights = [child.get_weight() for child in self.children]
        return max(set(weights), key=weights.count)

    def _get_unbalanced_child(self):
        balanced_weight = self.get_balanced_weight()
        # if not all weight are the same find the unbalanced child
        if not all(child.get_weight() == self.children[0].weight for child in self.children):
            for child in self.children:
                if child.get_weight() != balanced_weight:
                    return child

    def find_unbalance_child(self):
        #if leaf then return immediately
        if not self.children:
            return
        # if node then check if any children has unbalanced nodes
        for child in self.children:
            # from node first check if any children can find the unbalanced node
            node = child.find_unbalance_child()
            if node:
                return node
        # if not all children have equal weight return node
        return self._get_unbalanced_child()


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
        parents = nodes[:]
        while nodes:
            # get first node
            node = nodes[0]
            nodes.remove(node)
            # check if root is the parent
            root.add_child(node)
            # find parent from other nodes
            for parent in parents:
                parent.add_child(node)

    def create(self):
        lines = self._programs.split('\n')
        nodes = self._parse_lines(lines)
        self._parse_nodes(nodes)

    def get_base_node(self):
        return self._tree

    def find_unbalanced_node(self):
        if self._tree:
            return self._tree.find_unbalance_child()

    def calculate_correct_weight_for_unbalanced_node(self, node):
        parent = node.parent
        balanced_weight = parent.get_balanced_weight()
        node_weight = node.get_weight()
        if node_weight > balanced_weight:
            return node.weight - (node_weight - balanced_weight)
        else:
            return node.weight + (balanced_weight + node_weight)


def main():
    tree = TreeCreator(INPUT)
    tree.create()
    print(tree.get_base_node().name)
    print(tree.calculate_correct_weight_for_unbalanced_node(tree.find_unbalanced_node()))


if __name__=='__main__':
    main()
