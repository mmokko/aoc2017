INPUT = [5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 6]


def _create_banks(input_values):
    banks = dict()
    for idx, val in enumerate(input_values):
        banks[idx] = val
    return banks


class Memory(object):
    def __init__(self, input_values, iterations=1):
        self._banks = _create_banks(input_values)
        self._seen_banks = list()
        self._iterations = iterations
        self._iteration = 0
        self._steps = 0

    def _bank_to_process(self):
        bank = 0
        # find the bank with the most blocks
        for idx, blocks in self._banks.items():
            if idx == 0:
                bank = idx
            else:
                if blocks > self._banks[bank]:
                    bank = idx
        return bank

    def _find_next_bank(self, bank):
        banks = len(self._banks)
        next_bank = bank + 1 if bank + 1 < banks else 0
        return next_bank

    def _reallocate_bank(self, bank):
        blocks = self._banks[bank]
        # reset selected bank
        self._banks[bank] = 0
        # reallocate free blocks evenly to banks
        for idx in range(blocks):
            next_bank = self._find_next_bank(bank)
            self._banks[next_bank] += 1
            bank = next_bank

    def _store(self):
        # store only if no iterations found yet
        if self._iteration == 0:
            blocks_for_banks = list(self._banks.values())
            self._seen_banks.append(blocks_for_banks)

    def _reset_seen_banks(self):
        # reset only if first iteration found
        if self._iteration == 0:
            self._steps = 0
            self._seen_banks = list()
            # store current bank as the only one that is searched
            self._store()

    def _iterations_reached(self):
        if self._iterations == self._iteration + 1:
            return True
        else:
            # reset steps and only compare against found match
            self._reset_seen_banks()
        self._iteration += 1
        return False

    def _found_match(self):
        current = list(self._banks.values())
        for seen_bank in self._seen_banks:
            if current == seen_bank and self._iterations_reached():
                return True
        return False

    def reallocate(self):
        while not self._found_match():
            self._steps += 1
            self._store()
            bank = self._bank_to_process()
            self._reallocate_bank(bank)
        return self._steps


def puzzle1():
    memory = Memory(INPUT)
    print(memory.reallocate())


def puzzle2():
    memory = Memory(INPUT, 2)
    print(memory.reallocate())


def main():
    puzzle1()
    puzzle2()


if __name__=='__main__':
    main()
