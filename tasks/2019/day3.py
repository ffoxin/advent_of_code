from itertools import product
from pathlib import Path

DATA = (Path(__file__).parent / "data" / "day3.txt").read_text()


def is_between(first, middle, last):
    return min(first, last) <= middle <= max(first, last)


def puzzle1():
    entries = [i for i in DATA.split("\n") if i]

    wires = []
    for entry in entries:
        moves = [(move[0], int(move[1:])) for move in entry.split(",")]
        wire = [(0, 0)]
        for move, distance in moves:
            new = wire[-1]
            if move == "U":
                new = (new[0], new[1] + distance)
            elif move == "D":
                new = (new[0], new[1] - distance)
            elif move == "R":
                new = (new[0] + distance, new[1])
            elif move == "L":
                new = (new[0] - distance, new[1])
            else:
                raise RuntimeError("Dunno this move: {} {}".format(move, distance))
            wire.append(new)
        wires.append(wire)

    man_dist = None
    ints = []
    for i, j in product(*[range(len(wire) - 1) for wire in wires]):
        w1p1, w1p2 = wires[0][i], wires[0][i + 1]
        w2p1, w2p2 = wires[1][j], wires[1][j + 1]

        # skip parallel
        if (w1p1[0] == w1p2[0]) == (w2p1[0] == w2p2[0]):
            continue

        # check 1st line is hor and 2nd line is vert
        if w1p1[0] == w1p2[0]:
            # swap if 1st line is vert - same x's
            w1p1, w1p2, w2p1, w2p2 = w2p1, w2p2, w1p1, w1p2

        if not is_between(w1p1[0], w2p1[0], w1p2[0]) or not is_between(
            w2p1[1], w1p1[1], w2p2[1]
        ):
            continue

        point = (w2p1[0], w1p1[1])
        if point == (0, 0):
            continue
        dist = sum(map(abs, point))
        if man_dist is None or dist < man_dist:
            man_dist = dist
        ints.append(point)

    print(man_dist)

    return wires, ints


def puzzle2():
    wires, ints = puzzle1()

    sums = {}
    for ix, iy in ints:
        path_len = 0
        # done = False
        for wire in wires:
            for i in range(len(wire) - 1):
                (x1, y1), (x2, y2) = wire[i], wire[i + 1]
                if (
                    x1 == ix == x2
                    and is_between(y1, iy, y2)
                    or is_between(x1, ix, x2)
                    and y1 == iy == y2
                ):
                    path_len += abs(ix - x1) + abs(iy - y1)
                    # done = True
                    break
                else:
                    path_len += abs(x2 - x1) + abs(y2 - y1)
            # if done:
            #     break

        sums[(ix, iy)] = path_len

    # for key, value in sums.items():
    #     print(key, value)
    print(min(sums.values()))


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
