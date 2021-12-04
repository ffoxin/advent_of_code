import re


class LedNet:
    _pattern = re.compile("(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)")

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._leds = [list([0 for _ in range(height)]) for _ in range(width)]

    def process1(self, instruction):
        self._process(instruction, self._on, self._off, self._toggle)

    def process2(self, instruction):
        self._process(instruction, self._on2, self._off2, self._toggle2)

    def _process(self, instruction, on, off, toggle):
        parsed = self._pattern.match(instruction)
        result = parsed.groups()
        command = result[0]
        x1, y1, x2, y2 = tuple([int(value) for value in result[1:]])

        assert x1 <= x2, "x1 > x2"
        assert y1 <= y2, "y1 > y2"

        if command == "turn on":
            f = on
        elif command == "turn off":
            f = off
        elif command == "toggle":
            f = toggle
        else:
            assert False, "Invalid command"

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                f(i, j)

    def _toggle(self, x, y):
        self._set(x, y, (self._get(x, y) + 1) % 2)

    def _on(self, x, y):
        self._set(x, y, 1)

    def _off(self, x, y):
        self._set(x, y, 0)

    def _toggle2(self, x, y):
        self._set(x, y, self._get(x, y) + 2)

    def _on2(self, x, y):
        self._set(x, y, self._get(x, y) + 1)

    def _off2(self, x, y):
        current = self._get(x, y)
        if current > 0:
            self._set(x, y, current - 1)

    def _set(self, x, y, value):
        self._leds[y][x] = value

    def _get(self, x, y):
        return self._leds[y][x]

    def print(self):
        for line in self._leds:
            print("".join(["0" if led else "." for led in line]))
        print("---")

    def sum(self):
        count = 0
        for line in self._leds:
            count += sum(line)
        return count


def puzzle1():
    data = "tasks/2015/data/day6.txt"

    leds = LedNet(1000, 1000)

    with open(data, "r") as f:
        for line in f.readlines():
            line = line.strip()
            leds.process1(line)

    print(leds.sum())


def puzzle2():
    data = "tasks/2015/data/day6.txt"

    leds = LedNet(1000, 1000)

    with open(data, "r") as f:
        for line in f.readlines():
            line = line.strip()
            leds.process2(line)

    print(leds.sum())
