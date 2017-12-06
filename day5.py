class Maze(object):
    def __init__(self, inputs):
        self._inputs = inputs
        self._steps_taken = 0
        self._idx = 0
        self.use_optional_increment = False

    def _is_out(self):
        if self._idx >= len(self._inputs):
            return True
        return False

    def _get_new_value(self, old_value):
        if self.use_optional_increment:
            if old_value >= 3:
                return old_value - 1
        return old_value + 1

    def _increment_cur_value(self):
        old_value = self._inputs[self._idx]
        new_value = self._get_new_value(old_value)
        # remove old value
        del self._inputs[self._idx]
        # add updated value
        self._inputs.insert(self._idx, new_value)

    def find_way_out(self):
        while True:
            if self._is_out():
                return self._steps_taken
            new_idx = self._inputs[self._idx]
            self._increment_cur_value()
            self._idx = new_idx + self._idx
            self._steps_taken += 1


def run_puzzle_1():
    with open("maze_input.txt", 'r') as f:
        lines = [int(value) for value in f.read().splitlines()]
    maze = Maze(lines)
    print(maze.find_way_out())


def run_puzzle_2():
    with open("maze_input.txt", 'r') as f:
        lines = [int(value) for value in f.read().splitlines()]
    maze = Maze(lines)
    maze.use_optional_increment = True
    print(maze.find_way_out())


def main():
    run_puzzle_1()
    run_puzzle_2()


if __name__=='__main__':
    main()
