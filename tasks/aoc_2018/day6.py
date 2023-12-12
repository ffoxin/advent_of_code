from collections import defaultdict

from main import data_path

DATA = data_path(__file__)


class Cell:
    def __init__(self):
        self.parent = None
        self.distance = -1


def puzzle1() -> None:
    with open(DATA, "r") as f:
        lines = f.readlines()

    lines = [tuple(map(int, item.split(","))) for item in lines]

    width = max([i[0] for i in lines]) + 2
    height = max([i[1] for i in lines]) + 2

    items = defaultdict(list)
    inner = set(lines)
    for i in range(width):
        for j in range(height):
            distances = defaultdict(list)
            for x, y in lines:
                distances[abs(i - x) + abs(j - y)].append((x, y))
            min_dist = min(distances)
            if len(distances[min_dist]) == 1:
                point = distances[min_dist][0]
                items[point].append((i, j))
                if i == 0 or j == 0 or i == width - 1 or j == height - 1:
                    inner.discard(point)

    result = max([len(cells) for point, cells in items.items() if point in inner])

    print(result)


def puzzle2() -> None:
    with open(DATA, "r") as f:
        lines = f.readlines()

    lines = [tuple(map(int, item.split(","))) for item in lines]

    width = max([i[0] for i in lines]) + 2
    height = max([i[1] for i in lines]) + 2

    count = 0
    for i in range(width):
        for j in range(height):
            if sum([abs(i - x) + abs(j - y) for x, y in lines]) < 10000:
                count += 1

    print(count)
