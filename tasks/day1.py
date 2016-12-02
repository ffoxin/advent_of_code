class Point:
    # Directions:
    # 0 - North
    # 1 - East
    # 2 - South
    # 3 - West
    def __init__(self):
        self._x = 0
        self._y = 0
        self._direction = 0
        self._visited = [(0, 0)]
        self._first_revisited = None

    def feed(self, step):
        turn = step[0]
        distance = int(step[1:])

        if turn == 'R':
            self._direction += 1
        elif turn == 'L':
            self._direction -= 1
        else:
            assert False, 'Wrong turn'
        self._direction %= 4

        if self._direction == 0:
            visited = [(self._x, self._y + i + 1) for i in range(distance)]
            self._y += distance
        elif self._direction == 1:
            visited = [(self._x + i + 1, self._y) for i in range(distance)]
            self._x += distance
        elif self._direction == 2:
            visited = [(self._x, self._y - i - 1) for i in range(distance)]
            self._y -= distance
        elif self._direction == 3:
            visited = [(self._x - i - 1, self._y) for i in range(distance)]
            self._x -= distance
        else:
            assert False, 'Invalid direction'

        self._update_visits(visited)

    def _update_visits(self, visited):
        if not self._first_revisited:
            for point in visited:
                if point in self._visited and self._first_revisited is None:
                    self._first_revisited = abs(point[0]) + abs(point[1])
                    break
            self._visited += visited

    def sum(self):
        return abs(self._x) + abs(self._y)

    def _get_point(self):
        return self._x, self._y

    def get_twice_visited_distance(self):
        return self._first_revisited


way = 'R1, R1, R3, R1, R1, L2, R5, L2, R5, R1, R4, L2, R3, L3, R4, L5, R4, R4, R1, L5, L4, R5, R3, L1, R4, R3, ' \
      'L2, L1, R3, L4, R3, L2, R5, R190, R3, R5, L5, L1, R54, L3, L4, L1, R4, R1, R3, L1, L1, R2, L2, R2, R5, ' \
      'L3, R4, R76, L3, R4, R191, R5, R5, L5, L4, L5, L3, R1, R3, R2, L2, L2, L4, L5, L4, R5, R4, R4, R2, R3, ' \
      'R4, L3, L2, R5, R3, L2, L1, R2, L3, R2, L1, L1, R1, L3, R5, L5, L1, L2, R5, R3, L3, R3, R5, R2, R5, R5, ' \
      'L5, L5, R2, L3, L5, L2, L1, R2, R2, L2, R2, L3, L2, R3, L5, R4, L4, L5, R3, L4, R1, R3, R2, R4, L2, L3, ' \
      'R2, L5, R5, R4, L2, R4, L1, L3, L1, L3, R1, R2, R1, L5, R5, R3, L3, L3, L2, R4, R2, L5, L1, L1, L5, L4, ' \
      'L1, L1, R1 '


def puzzle1():
    position = Point()
    for step in way.split(', '):
        position.feed(step)

    print(position.sum())


def puzzle2():
    position = Point()
    for step in way.split(', '):
        position.feed(step)

    answer = position.get_twice_visited_distance()

    if answer is None:
        print('No twice visited location found')
    else:
        print(answer)
