from itertools import cycle

from main import data_path

DATA = data_path(__file__)


def puzzle1():
    with open(DATA, "r") as f:
        frequency = sum(map(int, f.readlines()))
    print(frequency)


def puzzle2():
    with open(DATA, "r") as f:
        changes = list(map(int, f.readlines()))

    frequency = 0
    steps = set()
    for i in cycle(changes):
        steps.add(frequency)
        frequency += i
        if frequency in steps:
            break

    print(frequency)
