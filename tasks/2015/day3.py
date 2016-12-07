class Position:
    def __init__(self):
        self._x = 0
        self._y = 0

    def get_pos(self):
        return self._x, self._y

    def go(self, direction):
        if direction == '<':
            self._x -= 1
        elif direction == '>':
            self._x += 1
        elif direction == 'v':
            self._y -= 1
        elif direction == '^':
            self._y += 1
        else:
            assert False, 'Wrong direction'

        return self.get_pos()


def puzzle1():
    data = 'tasks/2015/data/day3.txt'

    pos = Position()
    homes = [pos.get_pos()]
    with open(data, 'r') as f:
        path = f.read()
        for step in path:
            location = pos.go(step)
            if location not in homes:
                homes.append(location)
    print(len(homes))


def puzzle2():
    data = 'tasks/2015/data/day3.txt'

    santa = Position()
    robo = Position()
    homes = [santa.get_pos()]
    with open(data, 'r') as f:
        path = f.read()
        for index, step in enumerate(path):
            location = (santa if index % 2 == 0 else robo).go(step)
            if location not in homes:
                homes.append(location)
    print(len(homes))
