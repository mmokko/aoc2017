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
        return self._idx + value - len(self._hash)

    def hash(self):
        for value in self._inputs:
            if value: # ignore zero values as they don't have effect
                self._hash_with_input(value)
                self._idx = self._get_idx_end(value + self._skip)
            self._skip += 1
        return self._hash[0] * self._hash[1]


def main():
    puzzle_input = [106, 16, 254, 226, 55, 2, 1, 166, 177, 247, 93, 0, 255, 228, 60, 36]
    knot_hasher = KnotHasher(256, puzzle_input)
    print(knot_hasher.hash())


if __name__== '__main__':
    main()