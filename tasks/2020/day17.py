import operator
from itertools import product
from pathlib import Path
from typing import Tuple, Set, List

DATA = (Path(__file__).parent / 'data' / 'day17.txt').read_text()


def compare(pair, value):
    return (
        value if pair[0] is None else min(pair[0], value),
        value if pair[1] is None else max(pair[1], value),
    )


def get_borders(state) -> Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]:
    mx, my, mz = (None, None), (None, None), (None, None)
    for x, y, z in state:
        mx = compare(mx, x)
        my = compare(my, y)
        mz = compare(mz, z)

    return mx, my, mz


def get_borders_n(state: Set[Tuple], n: int) -> List[Tuple[int, int]]:
    extremes = [(None, None) for _ in range(n)]

    for point in state:
        for index, value in enumerate(point):
            extremes[index] = compare(extremes[index], value)

    return extremes


def print_state(state):
    mx, my, mz = get_borders(state)

    print('x =', mx, '| y =', my, '| z =', mz)
    for z in range(mz[0], mz[1] + 1):
        print('z =', z)
        for x in range(mx[0], mx[1] + 1):
            print(''.join(
                '#' if (x, y, z) in state else '.'
                for y in range(my[0], my[1] + 1)
            ))


def cycle(state):
    mx, my, mz = get_borders(state)

    new_state = set()
    for x, y, z in product(
            range(mx[0] - 1, mx[1] + 2),
            range(my[0] - 1, my[1] + 2),
            range(mz[0] - 1, mz[1] + 2),
    ):
        active_count = 0
        for dx, dy, dz in product([-1, 0, 1], repeat=3):
            if dx == dy == dz == 0:
                continue
            if (x + dx, y + dy, z + dz) in state:
                active_count += 1

        this_point = (x, y, z)
        if active_count == 3 or this_point in state and active_count == 2:
            new_state.add(this_point)

    return new_state


def cycle_n(state: Set[Tuple], n: int):
    extremes = get_borders_n(state, n)

    new_state = set()
    for this_point in product(*[
        range(m[0] - 1, m[1] + 2)
        for m in extremes
    ]):
        active_count = 0
        for dp in product([-1, 0, 1], repeat=n):
            if not any(dp):
                continue
            checkpoint = tuple(map(operator.add, this_point, dp))
            if checkpoint in state:
                active_count += 1

        if active_count == 3 or this_point in state and active_count == 2:
            new_state.add(this_point)

    return new_state


def puzzle1():
    entries = [i for i in DATA.split('\n') if i]

    state = set()
    for i, line in enumerate(entries):
        for j, item in enumerate(line):
            if item == '#':
                state.add((i, j, 0))

    for _ in range(6):
        state = cycle(state)

    print(len(state))


def puzzle2():
    entries = [i for i in DATA.split('\n') if i]

    state = set()
    for i, line in enumerate(entries):
        for j, item in enumerate(line):
            if item == '#':
                state.add((i, j, 0, 0))

    for _ in range(6):
        state = cycle_n(state, 4)

    print(len(state))


if __name__ == '__main__':
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
