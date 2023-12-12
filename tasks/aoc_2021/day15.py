from pathlib import Path
from typing import List, Optional
import sys

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()


def puzzle1() -> None:
    entries: List[List[int]] = [list(map(int, list(line))) for line in DATA.split("\n")]

    assert len(entries) == len(entries[0])

    size = len(entries)

    weights = {
        (0, 0): 0,
    }

    # weights = [[None] * size for _ in range(size)]

    def get_neibs(x, y):
        return [
            neib
            for neib in [
                (x + 1, y),
                (x - 1, y),
                (x, y + 1),
                (x, y - 1),
            ]
            if 0 <= x < size and 0 <= y < size
        ]

    last_visited = [(0, 0)]
    while True:
        if len(weights) == size**2:
            break

        for ver in last_visited:
            neibs = get_neibs(*ver)
            for neib in neibs:
                if neib not in weights:
                    weights[neib] = weights[ver] + 0

    def min_path(x: int, y: int) -> int:
        if weights[x][y] is None:
            if x == y == 0:
                weights[0][0] = 0
            if x == 0 and y != 0:
                weights[x][y] = min_path(x, y - 1) + entries[x][y]
            if x != 0 and y == 0:
                weights[x][y] = min_path(x - 1, y) + entries[x][y]
            if x != 0 and y != 0:
                weights[x][y] = (
                    min(
                        min_path(x - 1, y),
                        min_path(x, y - 1),
                    )
                    + entries[x][y]
                )

        return weights[x][y]

    print(min_path(size - 1, size - 1))


def puzzle22():
    print(f"max recursion: {sys.getrecursionlimit()}")
    sys.setrecursionlimit(1100)

    entries: List[List[int]] = [list(map(int, list(line))) for line in DATA.split("\n")]

    assert len(entries) == len(entries[0])

    size = len(entries)

    if True:
        for i in range(4):
            for j in range(size):
                entries.append([((k + 1) % 10 or 1) for k in entries[i * size + j]])
        for i in range(len(entries)):
            for j in range(4):
                entries[i].extend([((k + 1) % 10 or 1) for k in entries[i][-size:]])

        assert len(entries) == len(entries[0])

        size = len(entries)
        print(f"new size: {size}")

    weights: List[List[Optional[int]]] = [[None] * size for _ in range(size)]

    for i in range(size * 2 - 1):
        for j in range(i + 1):
            x = j
            y = i - j
            if not (0 <= x < size and 0 <= y < size):
                continue
            if x == y == 0:
                weights[x][y] = 0
                continue
            if x == 0:
                weights[x][y] = weights[x][y - 1] + entries[x][y]
                continue
            if y == 0:
                weights[x][y] = weights[x - 1][y] + entries[x][y]
                continue
            weights[x][y] = min(weights[x - 1][y], weights[x][y - 1]) + entries[x][y]

    print(weights[size - 1][size - 1])

    # if 0 <= i - j < size and 0 <= j < size:
    #     print(j, i - j)
    # for i in range(size):
    #     print(i)
    #     for j in range(i + 1):
    #         if i - j >= 0:
    #             print(f'{i - j}:{j}')
    # for i in range(size):
    #     print(size - 1 - i)
    #     for j in range(size - 1 - i):
    #         if i + j < size:
    #             print(f'{i + j}:{size - 1 - j}')

    # for i in chain(range(size), repeat(size - 1, size - 1)):
    #     print(i)
    #     for j in range(i + 1):

    return

    def new_min(*values):
        return min(filter(lambda x: x is not None, values))

    def min_path(x: int, y: int) -> Optional[int]:
        if x < 0 or y < 0:
            return None

        if weights[x][y] is None:
            if x == y == 0:
                weights[0][0] = 0
            # if x == 0 and y != 0:
            #     weights[x][y] = min_path(x, y - 1) + entries[x][y]
            # if x != 0 and y == 0:
            #     weights[x][y] = min_path(x - 1, y) + entries[x][y]
            # if x != 0 and y != 0:
            else:
                weights[x][y] = (
                    new_min(
                        min_path(x - 1, y),
                        min_path(x, y - 1),
                    )
                    + entries[x][y]
                )

        return weights[x][y]

    result = min_path(size - 1, size - 1)
    for i in range(size):
        print("|".join(f"{entries[i][j]}:{weights[i][j]:<4d}" for j in range(size)))
    print(result)

    # 2908 too high


def puzzle3():
    board = []
    for line in (
        (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text().splitlines()
    ):
        board.append([int(line[x]) for x in range(len(line))])
    distance = [[0] * 500 for _t in range(500)]
    queue = [[(0, 0)]] + [[] for _t in range(10000)]
    v = 0
    while distance[499][499] == 0:
        for y, x in queue[v]:
            if v > distance[y][x]:
                continue
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if y + dy >= 0 and y + dy < 500 and x + dx >= 0 and x + dx < 500:
                    dt = (
                        (
                            board[(y + dy) % 100][(x + dx) % 100]
                            + (y + dy) // 100
                            + (x + dx) // 100
                            - 1
                        )
                        % 9
                    ) + 1
                    if distance[y + dy][x + dx] == 0:
                        distance[y + dy][x + dx] = v + dt
                        queue[v + dt].append((y + dy, x + dx))
        v += 1
    print(distance[499][499])


if __name__ == "__main__":
    try:
        puzzle3()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
