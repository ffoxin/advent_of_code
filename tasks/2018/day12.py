from collections import deque
from copy import copy

from main import data_path

DATA = data_path(__file__)


class Rule:
    def __init__(self, line):
        start, end = line.split(" => ")
        self.start = start
        self.end = end

    def check(self, state, pos):
        if pos < 2:
            return "."
        elif pos + 3 > len(state):
            return "."
        elif state[pos - 2 : pos + 3] == self.start:
            return self.end
        else:
            return None


def puzzle1():
    with open(DATA, "r") as f:
        lines = f.readlines()

    lines = list(map(str.strip, lines))
    initial = lines[0].split(": ")[1]
    rules = list(map(Rule, lines[2:]))

    start = 0
    for i in range(20):
        if not initial.startswith("....."):
            initial = "....." + initial
            start -= 5
        if not initial.endswith("....."):
            initial += "....."

        state = []
        for j in range(len(initial)):
            check = None
            for rule in rules:
                check = rule.check(initial, j)
                if check is not None:
                    break
            if check is not None:
                state.append(check)
            else:
                state.append(".")

        initial = "".join(state)

    result = 0
    for p in initial:
        if p == "#":
            result += start
        start += 1
    print(result)


def puzzle2():
    with open(DATA, "r") as f:
        lines = f.readlines()

    lines = list(map(str.strip, lines))
    initial = lines[0].split(": ")[1]
    rules = list(map(Rule, lines[2:]))

    start = 0
    prev = None
    prev_start = 0
    step = 0
    while True:
        # normalize start
        pot_start = 0
        while True:
            if initial[pot_start] == "#":
                break
            pot_start += 1

        if pot_start < 5:
            initial = "." * (5 - pot_start) + initial
            start -= 5 - pot_start
        elif pot_start > 5:
            initial = initial[pot_start - 5 :]
            start += pot_start - 5

        # normalize end
        pot_end = 0
        while True:
            if initial[-1 - pot_end] == "#":
                break
            pot_end += 1

        if pot_end < 5:
            initial += "." * (5 - pot_end)
        elif pot_end > 5:
            initial = initial[: pot_end - 5]

        if prev == initial:
            break
        else:
            prev = initial
            prev_start = start

        state = []
        for j in range(len(initial)):
            check = None
            for rule in rules:
                check = rule.check(initial, j)
                if check is not None:
                    break
            if check is not None:
                state.append(check)
            else:
                state.append(".")

        initial = "".join(state)
        step += 1

    start = start + (50000000000 - step) * (start - prev_start)
    result = 0
    for p in initial:
        if p == "#":
            result += start
        start += 1
    print(result)
