from functools import reduce


DEFAULT_ASCII_INPUTS = [17, 31, 73, 47, 23]
ROUNDS = 64
SUB_BLOCKS = 16
BLOCK_SIZE = 16


class KnotHasher(object):
    def __init__(self, hash_size, inputs):
        self._hash = [idx for idx in range(0, hash_size)]
        self._inputs = inputs
        self._idx = 0
        self._skip = 0

    def _get_sublist(self, value):
        start = self._idx
        end = self._get_idx_end(value)
        if end > start:
            return self._hash[start : end]
        # if end wraps around combine list from start to max len + from 0 to end
        return self._hash[start : len(self._hash)] + self._hash[0 : end]

    def _get_index(self, idx):
        index = self._idx + idx
        if index > len(self._hash) - 1:
            return index - len(self._hash)
        return index

    def _hash_with_input(self, value):
        sublist = reversed(self._get_sublist(value))
        for idx, v in enumerate(sublist):
            i = self._get_index(idx)
            self._hash[i] = v

    def _get_idx_end(self, value):
        if value + self._idx < len(self._hash):
            return self._idx + value
        return (self._idx + value) % len(self._hash)

    def calc(self):
        for value in self._inputs:
            if value: # ignore zero values as they don't have effect
                self._hash_with_input(value)
                self._idx = self._get_idx_end(value + self._skip)
            self._skip += 1
        return self._hash[0] * self._hash[1]

    def _get_ascii_input(self):
        ascii_list = [ord(x) for x in self._inputs]
        return ascii_list + DEFAULT_ASCII_INPUTS

    def _get_sub_block(self, idx):
        start = idx * BLOCK_SIZE
        end = start + BLOCK_SIZE
        return self._hash[start : end]

    def _create_dense_hash(self):
        dense_hash = list()
        for idx in range(0, SUB_BLOCKS):
            block = self._get_sub_block(idx)
            dense_hash.append(reduce(lambda x, y: x ^ y, block))
        return dense_hash

    def _ascii_hash(self, dense_hash):
        return hash

    def hash(self):
        self._inputs = self._get_ascii_input()
        round = 0
        while round < ROUNDS:
            self.calc()
            round += 1
        dense_hash = self._create_dense_hash()
        return ''.join('{:02x}'.format(x) for x in dense_hash)


def puzzle1():
    puzzle_input = [106, 16, 254, 226, 55, 2, 1, 166, 177, 247, 93, 0, 255, 228, 60, 36]
    knot_hasher = KnotHasher(256, puzzle_input)
    print(knot_hasher.calc())


def puzzle2():
    puzzle_input = '106,16,254,226,55,2,1,166,177,247,93,0,255,228,60,36'
    knot_hasher = KnotHasher(256, puzzle_input)
    print(knot_hasher.hash())


def main():
    puzzle1()
    puzzle2()


if __name__== '__main__':
    main()