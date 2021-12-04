import re

from main import data_path

DATA = data_path(__file__)


class Point:
    def __init__(self, line):
        groups = re.match(
            r"position=< *(-?\d+), *(-?\d+)> velocity=< *(-?\d+),  *(-?\d+)>\n?", line
        ).groups()
        groups = list(map(int, groups))
        self.x = groups[0]
        self.y = groups[1]
        self.dx = groups[2]
        self.dy = groups[3]

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def undo_move(self):
        self.x -= self.dx
        self.y -= self.dy

    def __repr__(self):
        return f"<{self.x:>6}:{self.y:>6}|{self.dx:>3}:{self.dy:>3}>"


def puzzle1():
    with open(DATA, "r") as f:
        lines = f.readlines()

    points = list(map(Point, lines))

    sqr_min = None

    while True:
        for p in points:
            p.move()

        x_min = min(p.x for p in points)
        x_max = max(p.x for p in points)
        y_min = min(p.y for p in points)
        y_max = max(p.y for p in points)

        width = x_max - x_min + 1
        height = y_max - y_min + 1
        sqr = width * height

        if sqr_min and sqr > sqr_min:
            break

        sqr_min = sqr

    for p in points:
        p.undo_move()

    x_min = min(p.x for p in points)
    x_max = max(p.x for p in points)
    y_min = min(p.y for p in points)
    y_max = max(p.y for p in points)

    width = x_max - x_min + 1
    height = y_max - y_min + 1
    matrix = [["."] * width for _ in range(height)]
    for p in points:
        matrix[p.y - y_min][p.x - x_min] = "#"

    for line in matrix:
        print("".join(line))


def puzzle2():
    with open(DATA, "r") as f:
        lines = f.readlines()

    points = list(map(Point, lines))

    sqr_min = None

    seconds = 0
    while True:
        for p in points:
            p.move()

        x_min = min(p.x for p in points)
        x_max = max(p.x for p in points)
        y_min = min(p.y for p in points)
        y_max = max(p.y for p in points)

        width = x_max - x_min + 1
        height = y_max - y_min + 1
        sqr = width * height

        if sqr_min and sqr > sqr_min:
            break

        sqr_min = sqr
        seconds += 1

    print(seconds)
