import re

from main import data_path

DATA = data_path(__file__)


class Rect:
    def __init__(self, claim_id, left, top, width, height):
        self.claim_id = claim_id
        self.x1 = left
        self.y1 = top
        self.width = width
        self.height = height
        self.x2 = left + width
        self.y2 = top + height

    def __repr__(self):
        return f"{self.x1}:{self.y1} -> {self.x2}:{self.y2} - {self.width}x{self.height}"


def check_intersect(rect1: Rect, rect2: Rect):
    x5 = max(rect1.x1, rect2.x1)
    y5 = max(rect1.y1, rect2.y1)
    x6 = min(rect1.x2, rect2.x2)
    y6 = min(rect1.y2, rect2.y2)

    if x5 >= x6 or y5 >= y6:
        return None
    else:
        return Rect(None, x5, y5, x6 - x5, y6 - y5)


def puzzle1() -> None:
    with open(DATA, "r") as f:
        lines = f.readlines()

    lines = map(str.strip, lines)

    pattern = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
    claims = [Rect(*map(int, pattern.match(line).groups())) for line in lines]
    requested = set()
    intersected = set()
    for claim in claims:
        for i in range(claim.x1, claim.x2):
            for j in range(claim.y1, claim.y2):
                t = (i, j)
                if t in requested:
                    intersected.add(t)
                else:
                    requested.add(t)
    print(len(intersected))


def puzzle2() -> None:
    with open(DATA, "r") as f:
        lines = f.readlines()

    lines = map(str.strip, lines)

    pattern = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
    claims = [Rect(*map(int, pattern.match(line).groups())) for line in lines]
    requested = set()
    intersected = set()
    for claim in claims:
        for i in range(claim.x1, claim.x2):
            for j in range(claim.y1, claim.y2):
                t = (i, j)
                if t in requested:
                    intersected.add(t)
                else:
                    requested.add(t)

    for claim in claims:
        count = 0
        for i in range(claim.x1, claim.x2):
            for j in range(claim.y1, claim.y2):
                t = (i, j)
                if t in intersected:
                    count += 1
        if count == 0:
            print(claim.claim_id)
            break
