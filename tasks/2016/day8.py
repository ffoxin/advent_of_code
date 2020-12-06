import re


class LedNet:
    _pattern = re.compile('(rect |rotate column x=|rotate row y=)(\d+)(x| by )(\d+)')

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._leds = [list([0 for _ in range(width)]) for _ in range(height)]

    def process(self, instruction):
        self._process(instruction, self._rect, self._rotate_x, self._rotate_y)

    def _process(self, instruction, rect, rotate_x, rotate_y):
        parsed = self._pattern.match(instruction)
        result = parsed.groups()
        command = result[0]
        x, y = tuple([int(value) for value in result[1::2]])

        if command.startswith('rect'):
            f = rect
        elif command.endswith('x='):
            f = rotate_x
        elif command.endswith('y='):
            f = rotate_y
        else:
            assert False, 'Invalid command: {}'.format(command)

        f(x, y)

    def _rect(self, x, y):
        for i in range(x):
            for j in range(y):
                self._set(i, j, 1)

    def _rotate_x(self, col, shift):
        line = [self._get(col, i) for i in range(self._height)]
        for i in range(self._height):
            self._set(col, (i + shift) % self._height, line[i])

    def _rotate_y(self, row, shift):
        line = [self._get(i, row) for i in range(self._width)]
        for i in range(self._width):
            self._set((i + shift) % self._width, row, line[i])

    def _set(self, x, y, value):
        self._leds[y][x] = value

    def _get(self, x, y):
        return self._leds[y][x]

    def print(self):
        for line in self._leds:
            print(''.join(['#' if led else '.' for led in line]))
        print('---')

    def sum(self):
        count = 0
        for line in self._leds:
            count += sum(line)
        return count


def puzzle1():
    data = 'tasks/2016/data/day8.txt'

    leds = LedNet(50, 6)

    with open(data, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            leds.process(line)

    print(leds.sum())


def puzzle2():
    data = 'tasks/2016/data/day8.txt'

    leds = LedNet(50, 6)

    with open(data, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            leds.process(line)

    leds.print()
