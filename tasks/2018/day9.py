import time
from itertools import cycle

from main import data_path

DATA = data_path(__file__)


def puzzle1():
    with open(DATA, "r") as f:
        line = f.readline()

    line = line.split(" ")
    players = int(line[0])
    last = int(line[-2])

    current = 0
    circle = [0]
    marble = 0
    scores = [0] * players
    for p in cycle(range(players)):
        marble += 1
        if marble > last:
            break

        if marble % 23 == 0:
            scores[p] += marble + circle.pop(current - 7)
            current -= 7
            if current < 0:
                current += 1
            current %= len(circle)
        else:
            current = (current + 2) % len(circle)
            if current == 0:
                current = len(circle)
                circle.append(marble)
            else:
                circle.insert(current, marble)

    print(max(scores))


class Circle:
    class _Node:
        def __init__(self, value):
            self.value = value
            self.prev = None
            self.next = None

        def __repr__(self):
            return "{} <- {} -> {}".format(
                self.prev.value if self.prev else "",
                self.value,
                self.next.value if self.next else "",
            )

    def __init__(self):
        initial = self._Node(0)
        initial.next = initial
        initial.prev = initial

        self.root = initial
        self.count = 1
        self.current = self.root

    def insert_after(self, value):
        after = self.current.next

        new_node = self._Node(value)
        new_node.prev = after
        new_node.next = after.next

        after.next.prev = new_node
        after.next = new_node

        self.count += 1
        self.current = new_node

        return new_node

    def score_this(self):
        for i in range(6):
            self.current = self.current.prev

        remove = self.current.prev
        remove.prev.next = remove.next
        remove.next.prev = remove.prev

        self.count -= 1

        return remove.value

    def print(self, player):
        root = self.root
        sample = []
        for i in range(self.count):
            sample.append(root.value)
            root = root.next

        print(
            "[{}]{}".format(
                player + 1,
                "".join(
                    "({:2})".format(c)
                    if c == self.current.value
                    else " {:2} ".format(c)
                    for c in sample
                ),
            )
        )


def puzzle2():
    with open(DATA, "r") as f:
        line = f.readline()

    line = line.split(" ")
    players = int(line[0])
    last = int(line[-2]) * 100

    circle = Circle()
    marble = 0
    scores = [0] * players
    start = time.time()
    for p in cycle(range(players)):
        marble += 1
        if marble > last:
            break

        if marble % 23 == 0:
            scores[p] += marble + circle.score_this()
        else:
            circle.insert_after(marble)

    print("elapsed", time.time() - start)

    print(max(scores))
