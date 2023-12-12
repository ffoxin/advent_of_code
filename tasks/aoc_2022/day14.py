from pathlib import Path
from typing import List, Set, Generator
from PIL import Image, ImageDraw

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()


class Point:
    __slots__ = ("x", "y")
    min_x: int | None = None
    min_y: int | None = None
    max_x: int | None = None
    max_y: int | None = None

    @classmethod
    def from_str(cls, point_line: str) -> "Point":
        return cls(*tuple(map(int, point_line.split(","))))

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

        if self.__class__.min_x is None:
            self.__class__.min_x = self.x
        else:
            self.__class__.min_x = min(self.__class__.min_x, self.x)

        if self.__class__.max_x is None:
            self.__class__.max_x = self.x
        else:
            self.__class__.max_x = max(self.__class__.max_x, self.x)

        if self.__class__.min_y is None:
            self.__class__.min_y = self.y
        else:
            self.__class__.min_y = min(self.__class__.min_y, self.y)

        if self.__class__.max_y is None:
            self.__class__.max_y = self.y
        else:
            self.__class__.max_y = max(self.__class__.max_y, self.y)

    def is_between(self, start: "Point", end: "Point") -> bool:
        return (start.x <= self.x <= end.x or start.x >= self.x >= end.x) and (
            start.y <= self.y <= end.y or start.y >= self.y >= end.y
        )

    def is_empty(self, paths: List[List["Point"]], sands: Set["Point"]) -> bool:
        if self in sands:
            return False

        for path in paths:
            for i in range(len(path) - 1):
                start, end = path[i], path[i + 1]
                if self.is_between(start, end):
                    return False

        return True

    def __eq__(self, other: object) -> bool:
        assert isinstance(other, Point)
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return f"[{self.x}:{self.y}]"

    def get_candidates(self) -> Generator:
        yield Point(self.x, self.y + 1)
        yield Point(self.x - 1, self.y + 1)
        yield Point(self.x + 1, self.y + 1)

    def get_symbol(self, paths: List[List["Point"]], start: "Point", sands: Set["Point"]):
        if self == start:
            return "+"  # sand source
        if self in sands:
            return "o"  # piece of sand
        if not self.is_empty(paths, sands):
            return "#"  # rock
        return "."  # air


class Point2(Point):
    def is_empty2(self, rocks: Set[Point], sands: Set[Point]) -> bool:
        if self in sands:
            return False

        if self in rocks:
            return False

        return True

    def get_symbol2(self, rocks: Set["Point2"], start: "Point2", sands: Set["Point2"]):
        if self == start:
            return "+"  # sand source
        if self in sands:
            return "o"  # piece of sand
        if self in rocks:
            return "#"  # rock
        return "."  # air

    def get_candidates(self) -> Generator:
        for point in super().get_candidates():
            yield Point2(point.x, point.y)


def puzzle1() -> None:
    entries = list(filter(bool, DATA.split("\n")))
    paths = []
    for line in entries:
        points = line.split(" -> ")
        paths.append([Point.from_str(point_str) for point_str in points])

    start = Point(500, 0)
    occupied: set[Point] = set()

    min_x, max_x, min_y, max_y = Point.min_x, Point.max_x, Point.min_y, Point.max_y
    more = True
    while True:
        sand = start
        while True:
            for candidate in sand.get_candidates():
                assert min_x is not None
                assert max_x is not None
                assert min_y is not None
                assert max_y is not None
                more = (min_x <= sand.x <= max_x) and (min_y <= sand.y <= max_y)
                if not more:
                    break
                if candidate.is_empty(paths, occupied):
                    sand = candidate
                    break
            else:
                occupied.add(sand)
                break

            if not more:
                break

        if not more:
            break

    print(len(occupied))


def puzzle22():
    entries = list(filter(bool, DATA.split("\n")))
    paths = []
    for line in entries:
        points = line.split(" -> ")
        paths.append([Point.from_str(point_str) for point_str in points])

    paths.append(
        [
            Point(Point.min_x - 1000, Point.max_y + 2),
            Point(Point.max_x + 1000, Point.max_y + 2),
        ]
    )

    start = Point(500, 0)
    occupied = set()

    while True:
        if start in occupied:
            break

        sand = start
        while True:
            for candidate in sand.get_candidates():
                if candidate.is_empty(paths, occupied):
                    sand = candidate
                    break
            else:
                occupied.add(sand)
                break

        if len(occupied) % 100 == 0:
            print(len(occupied))

    min_x = min(p.x for p in occupied)
    max_x = max(p.x for p in occupied)
    min_y = min(p.y for p in occupied)
    max_y = max(p.y for p in occupied) + 1
    Path("tree.txt").write_text(
        "\n".join(
            [
                "".join(
                    Point(x, y).get_symbol(paths, start, occupied) for x in range(min_x, max_x + 1)
                )
                for y in range(min_y, max_y + 1)
            ]
        ),
        encoding="utf-8",
    )

    print(len(occupied))


class SnapshotSaver:
    def __init__(
        self, rocks: Set[Point2], start: Point2, min_x: int, max_x: int, min_y: int, max_y: int
    ):
        self.rocks = rocks
        self.start = start
        self.min_x, self.max_x, self.min_y, self.max_y = min_x, max_x, min_y, max_y

    def save_snapshot(self, index: int, snapshot: Set[Point2]) -> None:
        text = "\n".join(
            [
                "".join(
                    Point2(x, y).get_symbol2(self.rocks, self.start, snapshot)
                    for x in range(self.min_x, self.max_x + 1)
                )
                for y in range(self.min_y, self.max_y + 1)
            ]
        )
        image = Image.new(
            "RGB",
            (6 * (self.max_x - self.min_x + 1), 16 * (self.max_y - self.min_y)),
            color=(15, 15, 35),
        )
        d = ImageDraw.Draw(image)
        d.multiline_text((0, 0), text, fill=(204, 204, 204))
        file_name = f"frames/frame_{index:08d}.png"
        image.save(file_name)


def puzzle2() -> None:
    entries = list(filter(bool, DATA.split("\n")))
    paths = []
    for line in entries:
        points = line.split(" -> ")
        paths.append([Point2.from_str(point_str) for point_str in points])

    start = Point2(500, 0)

    min_y, max_y = Point2.min_y, Point2.max_y + 2
    diff_y = max_y - min_y
    min_x, max_x = start.x - diff_y, start.x + diff_y

    paths.append(
        [
            Point2(min_x, max_y),
            Point2(max_x, max_y),
        ]
    )

    rocks = set()
    for path in paths:
        for i in range(len(path) - 1):
            p1, p2 = path[i], path[i + 1]
            if p1.x == p2.x:
                if p1.y > p2.y:
                    p1, p2 = p2, p1
                for y in range(p1.y, p2.y + 1):
                    rocks.add(Point2(p1.x, y))
            else:
                assert p1.y == p2.y
                if p1.x > p2.x:
                    p1, p2 = p2, p1
                for x in range(p1.x, p2.x + 1):
                    rocks.add(Point2(x, p1.y))

    print(f"rocks: {len(rocks)}")
    sands = set()

    index = 0
    snapshot_saver = SnapshotSaver(rocks, start, min_x, max_x, min_y, max_y)
    snapshot_saver.save_snapshot(index, sands)
    while True:
        if start in sands:
            break

        sand = start
        while True:
            for candidate in sand.get_candidates():
                if candidate.is_empty2(rocks, sands):
                    sand = candidate
                    index += 1
                    snapshot_saver.save_snapshot(index, sands | {sand})
                    break
            else:
                sands.add(sand)
                index += 1
                snapshot_saver.save_snapshot(index, sands)
                break

        # if len(sands) % 100 == 0:
        print(len(sands))

    #
    # min_x = min(p.x for p in sands) - 1
    # max_x = max(p.x for p in sands) + 1
    # min_y = min(p.y for p in sands)
    # max_y = max(p.y for p in sands) + 1

    # for index, snapshot in enumerate(snapshots):
    #     text = "\n".join(
    #         [
    #             "".join(
    #                 Point2(x, y).get_symbol2(rocks, start, snapshot)
    #                 for x in range(min_x, max_x + 1)
    #             )
    #             for y in range(min_y, max_y + 1)
    #         ]
    #     )
    #     image = Image.new('RGB', (6 * (max_x - min_x + 1), 16 * (max_y - min_y)), color=(15, 15, 35))
    #     d = ImageDraw.Draw(image)
    #     d.multiline_text((0, 0), text, fill=(204, 204, 204))
    #     file_name = f'frames/frame_{index:08d}.png'
    #     image.save(file_name)

    Path("tree.txt").write_text(
        "\n".join(
            [
                "".join(
                    Point2(x, y).get_symbol2(rocks, start, sands) for x in range(min_x, max_x + 1)
                )
                for y in range(min_y, max_y + 1)
            ]
        ),
        encoding="utf-8",
    )

    print(len(rocks))
    print(index)
    # print(len(snapshots))
    print(min_x, max_x, min_y, max_y)
    print(len(sands))


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
