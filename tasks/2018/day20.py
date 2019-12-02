from collections import defaultdict

from main import data_path

DATA = data_path(__file__)


class Room:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None


class Link:

    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Field:

    def __init__(self):
        self.links = set()
        self.x = 0
        self.y = 0

        self.states = []

    def add_link(self, direction):
        x = self.x
        y = self.y
        if direction == 'N':
            y -= 1
        elif direction == 'S':
            y += 1
        elif direction == 'W':
            x -= 1
        elif direction == 'E':
            x += 1
        else:
            raise RuntimeError('Unknown direction: {}'.format(direction))

        self.links.add((self.x, self.y, x, y))

    def new_state(self, pos):
        self.states.append((pos, self.x, self.y))

    def restore_state(self):
        pos, self.x, self.y = self.states.pop()

        return pos

    def analyze(self, line):
        pos = 0
        while True:
            ch = line[pos]
            if ch in 'NSWE':
                self.add_link(ch)
            elif ch == '(':
                depth = 1
                end_pos = pos + 1
                while depth != 0:
                    if line[end_pos] == '(':
                        depth += 1
                    elif line[end_pos] == ')':
                        depth -= 1
                    end_pos += 1
                self.analyze()


def puzzle1():
    with open(DATA, 'r') as f:
        lines = f.readlines()

    line = lines[0].strip()[1:-1]

    max_depth = 0
    depth = 0
    for i in line:
        if i == '(':
            depth += 1
        elif i == ')':
            depth -= 1
        if depth > max_depth:
            max_depth = depth

    print(max_depth)
    return

    field = Field()
    pos = 0
    while True:
        if pos in 'NSWE':
            field.add_link(pos)
        elif pos == '(':
            field.new_state(pos)
        elif pos == ')':
            pass
        elif pos == '|':
            field.new_state(pos)



# def puzzle2():
#     pass
