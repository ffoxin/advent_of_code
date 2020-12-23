import operator
from itertools import chain
from pathlib import Path

DATA = (Path(__file__).parent / 'data' / 'day23.txt').read_text()


def puzzle1():
    entries = [i for i in DATA.split('\n') if i]
    steps = int(entries[0])
    cups = list(map(int, entries[1]))
    for _ in range(steps):
        current = cups[0]
        picked = cups[1:4]
        rest = cups[4:] + cups[:1]
        while True:
            current -= 1
            if current == 0:
                current = max(rest)
            if current not in rest:
                continue
            index = rest.index(current)
            break
        cups = rest[:index + 1] + picked + rest[index + 1:]
        print(cups)

    index = cups.index(1)
    print(''.join(map(str, cups[index + 1:] + cups[:index])))

    # print(cups)


class Cup:
    def __init__(self, value):
        self.value = value
        self.next = None


class Game:
    def __init__(self):
        self.top = None
        self.bot = None

    def add(self, cup: Cup):
        if self.top is None:
            self.top = self.bot = cup
        else:
            self.bot.next = cup
            self.bot = cup


def puzzle2():
    entries = [i for i in DATA.split('\n') if i]
    steps = int(entries[0])
    limit = int(entries[1])
    cups = list(map(int, entries[2]))
    # map: cup -> next
    game = {
        cups[i]: cups[(i + 1) % len(cups)]
        for i in range(len(cups))
    }
    if limit > len(cups):
        mac_cup = max(cups)
        game[cups[-1]] = mac_cup + 1
        for i in range(max(cups) + 1, limit + 1):
            game[i] = i + 1
        game[limit] = cups[0]

    print('cups: {}'.format(len(game)))

    current = cups[0]

    print('-'*40)
    for _ in range(steps):
        picked = (game[current], game[game[current]], game[game[game[current]]])
        dest = current
        while True:
            dest -= 1
            if dest == 0:
                dest = limit
            if dest not in picked:
                break
        game[current] = game[picked[2]]
        game[picked[2]] = game[dest]
        game[dest] = picked[0]
        current = game[current]

    pair = (game[1], game[game[1]])
    print(pair)
    print(operator.mul(*pair))


if __name__ == '__main__':
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
