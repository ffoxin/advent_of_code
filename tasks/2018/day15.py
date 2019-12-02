from operator import itemgetter

from main import data_path

DATA = data_path(__file__)


class Field:

    def __init__(self, field):
        self.width = len(field[0])
        self.height = len(field)
        walls = set()
        elfs = set()
        goblins = set()
        for y, line in enumerate(field):
            for x, ch in enumerate(line):
                if ch == '#':
                    walls.add((x, y))
                elif ch == 'E':
                    elfs.add((x, y))
                elif ch == 'G':
                    goblins.add((x, y))

        self.walls = walls
        self.elfs = elfs
        self.goblins = goblins

    def get_in_range(self, x, y):
        for xa, ya in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            yield (x + xa, y + ya)

    def find_target(self, p, targets):
        x, y = p
        in_range = set()
        for xt, yt in targets:
            for point in self.get_in_range(xt, yt):
                if point in self.walls:
                    continue
                if point in self.elfs:
                    continue
                if point in self.goblins:
                    continue
                in_range.add(point)

        points = []
        for xp, yp in in_range:
            points.append({
                'point': (xp, yp),
                'distance': abs(x - xp) + abs(y - yp),
                'x': xp,
                'y': yp,
            })

        sorted_points = sorted(points, key=itemgetter('distance', 'y', 'x'))
        closest = sorted_points[0]

        return closest

    def step(self, xf, yf, xt, yt):
        field = [[None] * self.width for _ in range(self.height)]


def puzzle1():
    with open(DATA, 'r') as f:
        lines = f.readlines()

    data = [line.strip('\n') for line in lines]
    field = Field(data)

    for elf_point in field.elfs:
        print(field.find_target(elf_point, field.goblins))

# def puzzle2():
#     pass
