class Keypad:
    def __init__(self):
        self._x = 1
        self._y = 1
        self._pressed = []

    def move(self, direction):
        if direction == 'R' and self._x < 2:
            self._x += 1
        elif direction == 'L' and self._x > 0:
            self._x -= 1
        elif direction == 'D' and self._y < 2:
            self._y += 1
        elif direction == 'U' and self._y > 0:
            self._y -= 1

    def _get_digit(self):
        return self._y * 3 + self._x + 1

    def feed(self, line):
        for movement in line:
            self.move(movement)
        self._pressed.append(str(self._get_digit()))

    def get_code(self):
        return ''.join(self._pressed)


class KeyHell:
    def __init__(self):
        self._x = -2
        self._y = 0
        self._pressed = []

    # -x + 2 < abs(y)
    # x + 2 > abs(y)
    # abs(x) < y + 2
    # abs(x) < -y + 2
    def move(self, direction):
        if direction == 'R' and -self._x + 2 > abs(self._y):
            self._x += 1
        elif direction == 'L' and self._x + 2 > abs(self._y):
            self._x -= 1
        elif direction == 'D' and abs(self._x) < self._y + 2:
            self._y -= 1
        elif direction == 'U' and abs(self._x) < -self._y + 2:
            self._y += 1

    def _get_digit(self):
        if self._y == 2:
            answer = 1
        elif self._y == 1:
            answer = 3 + self._x
        elif self._y == 0:
            answer = 7 + self._x
        elif self._y == -1:
            answer = 11 + self._x
        elif self._y == -2:
            answer = 13
        else:
            assert False, 'Invalid position: x={}, y={}'.format(
                self._x,
                self._y
            )
        return hex(answer)[2].upper()

    def feed(self, line):
        for movement in line:
            self.move(movement)
        self._pressed.append(self._get_digit())

    def get_code(self):
        return ''.join(self._pressed)


def puzzle1():
    data = 'tasks/data/day2.txt'

    keypad = Keypad()
    with open(data, 'r') as f:
        for line in f.readlines():
            keypad.feed(line)

    print(keypad.get_code())


def puzzle2():
    data = 'tasks/data/day2.txt'

    keypad = KeyHell()
    with open(data, 'r') as f:
        for line in f.readlines():
            keypad.feed(line)

    print(keypad.get_code())
