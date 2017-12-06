from enum import Enum
import copy


INPUT = 361527


class Step(Enum):
    UP = 0,
    DOWN = 1,
    LEFT = 2,
    RIGHT = 3


class Coordinates(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.value = 0

    def update(self, step):
        if step == Step.UP:
            self.y += 1
        elif step == Step.DOWN:
            self.y -= 1
        elif step == Step.LEFT:
            self.x -= 1
        elif step == Step.RIGHT:
            self.x += 1


class SpiralMemory(object):
    def __init__(self, input_val):
        self._input = input_val
        self._increment = False
        self._step_per_dir = 1
        self._step_taken_per_dir = 0
        self._current_step = Step.RIGHT
        self._coords = list()

    def _change_dir(self):
        if self._current_step == Step.RIGHT:
            self._current_step = Step.UP
        elif self._current_step == Step.LEFT:
            self._current_step = Step.DOWN
        elif self._current_step == Step.DOWN:
            self._current_step = Step.RIGHT
        elif self._current_step == Step.UP:
            self._current_step = Step.LEFT

    def _find_next_step(self, idx):
        # validate value
        if idx == 1:
            return

        if self._step_per_dir == self._step_taken_per_dir:
            self._change_dir()
            self._step_taken_per_dir = 1
            if self._increment:
                self._step_per_dir += 1
                self._increment = False
            else:
                self._increment = True
        else:
            self._step_taken_per_dir += 1

        return self._current_step

    def distance(self):
        c = Coordinates()
        for idx in range (1, self._input + 1):
            step = self._find_next_step(idx)
            c.update(step)
        return abs(c.x) + abs(c.y)

    def _get_value(self, c):
        total = 0
        if c.x == 0 and c.y == 0:
            return 1
        for coord in self._coords:
            if (coord.x == (c.x - 1) and coord.y == c.y) or \
                    (coord.x == (c.x + 1) and coord.y == c.y) or \
                    (coord.x == (c.x + 1) and coord.y == (c.y + 1)) or \
                    (coord.x == c.x and coord.y == (c.y + 1)) or \
                    (coord.x == (c.x - 1) and coord.y == (c.y + 1)) or \
                    (coord.x == (c.x - 1) and coord.y == (c.y - 1)) or \
                    (coord.x == c.x and coord.y == (c.y - 1)) or \
                    (coord.x == (c.x + 1) and coord.y == (c.y - 1)):
                    total += coord.value
        return total

    def value(self):
        idx = 0
        c = Coordinates()
        while True:
            idx += 1
            step = self._find_next_step(idx)
            c.update(step)
            c.value = self._get_value(c)
            if c.value > self._input:
                return c.value

            self._coords.append(copy.copy(c))


def main():
    sp1 = SpiralMemory(INPUT)
    print(sp1.distance())
    sp2 = SpiralMemory(INPUT)
    print(sp2.value())


if __name__=='__main__':
    main()
