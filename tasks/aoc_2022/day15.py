import re
from pathlib import Path

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()

line_template = re.compile(
    r"^Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)$"
)


class Point:
    min_x = None
    max_x = None
    min_y = None
    max_y = None

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

        if self.__class__.min_x is None or self.__class__.min_x > x:
            self.__class__.min_x = x
        if self.__class__.max_x is None or self.__class__.max_x < x:
            self.__class__.max_x = x
        if self.__class__.min_y is None or self.__class__.min_y > y:
            self.__class__.min_y = y
        if self.__class__.max_y is None or self.__class__.max_y < y:
            self.__class__.max_y = y

    def __sub__(self, other: "Point") -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __repr__(self):
        return f"[{self.x}:{self.y}]"

    def __eq__(self, other: object) -> bool:
        assert isinstance(other, Point)
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


# class Line:
#     def __init__(self, start: Point, end: Point):
#         if start.x > end.x:
#             start, end = end, start
#         self.start, self.end = start, end
#         self.a = (start.y - end.y) // (start.x - end.x)
#         self.b = (start.y + end.y - self.a * (start.x + end.x)) // 2
#
#     def __mul__(self, other: 'Line') -> Optional[Point]:
#         if self.a == other.a:
#             return None
#
#         assert self.a != other.a
#         x =


def puzzle1() -> None:
    entries = list(filter(bool, DATA.split("\n")))
    sensors, beacons = [], []
    for line in entries:
        match = line_template.fullmatch(line)
        assert match is not None
        sx, sy, bx, by = map(int, match.groups())
        sensors.append(Point(sx, sy))
        beacons.append(Point(bx, by))
        distance = sensors[-1] - beacons[-1]
        Point(sx - distance, sy - distance)
        Point(sx + distance, sy + distance)

    # for y in range(Point.min_y, Point.max_y + 1):
    #     line = []
    #     for x in range(Point.min_x, Point.max_x + 1):
    #         p = Point(x, y)
    #         if p in sensors:
    #             ch = 'S'
    #         elif p in beacons:
    #             ch = 'B'
    #         else:
    #             for sensor, beacon in zip(sensors, beacons):
    #                 if sensor != Point(8, 7):
    #                     continue
    #                 max_distance = sensor - beacon
    #                 if p - sensor <= max_distance:
    #                     ch = '#'
    #                     break
    #             else:
    #                 ch = '.'
    #         line.append(ch)
    #     print(f'{y:>2d} {"".join(line)}')

    # target_y = 10
    target_y = 2000000
    sections = []
    for sensor, beacon in zip(sensors, beacons):
        distance = sensor - beacon
        min_y, max_y = sensor.y - distance, sensor.y + distance
        if min_y <= target_y <= max_y:
            diff_width = distance - abs(sensor.y - target_y)
            sections.append((sensor.x - diff_width, sensor.x + diff_width))

    print(sections)

    coverage: set[int] = set()
    for begin, end in sections:
        coverage.update(list(range(begin, end + 1)))
    for sensor in sensors:
        if sensor.y == target_y:
            coverage.discard(sensor.x)
    for beacon in beacons:
        if beacon.y == target_y:
            coverage.discard(beacon.x)

    print(Point.min_x, Point.max_x, Point.min_y, Point.max_y)
    print(len(coverage))


def puzzle2() -> None:
    entries = list(filter(bool, DATA.split("\n")))
    sensors, beacons = [], []
    for line in entries:
        match = line_template.fullmatch(line)
        assert match is not None
        sx, sy, bx, by = map(int, match.groups())
        sensors.append(Point(sx, sy))
        beacons.append(Point(bx, by))
        distance = sensors[-1] - beacons[-1]
        Point(sx - distance, sy - distance)
        Point(sx + distance, sy + distance)

    # for y in range(Point.min_y, Point.max_y + 1):
    #     line = []
    #     for x in range(Point.min_x, Point.max_x + 1):
    #         p = Point(x, y)
    #         if p in sensors:
    #             ch = 'S'
    #         elif p in beacons:
    #             ch = 'B'
    #         else:
    #             for sensor, beacon in zip(sensors, beacons):
    #                 # if sensor != Point(8, 7):
    #                 #     continue
    #                 max_distance = sensor - beacon
    #                 if p - sensor <= max_distance:
    #                     ch = '#'
    #                     break
    #             else:
    #                 ch = '.'
    #         line.append(ch)
    #     print(f'{y:>2d} {"".join(line)}')

    # target_y = 10
    # target_y = 2000000
    # sections = []
    borders = set()
    neighbours = set()
    for sensor, beacon in zip(sensors, beacons):
        # print(sensor, beacon)
        distance = sensor - beacon
        min_y, max_y = sensor.y - distance, sensor.y + distance
        for i in range(distance):
            borders.update(
                [
                    Point(sensor.x + i, min_y + i),
                    Point(sensor.x + i, max_y - i),
                    Point(sensor.x - i, min_y + i),
                    Point(sensor.x - i, max_y - i),
                ]
            )
        min_y -= 1
        max_y += 1
        for i in range(distance + 2):
            neighbours.update(
                [
                    Point(sensor.x + i, min_y + i),
                    Point(sensor.x + i, max_y - i),
                    Point(sensor.x - i, min_y + i),
                    Point(sensor.x - i, max_y - i),
                ]
            )

    print(len(borders))
    print(len(neighbours))
    #
    # for y in range(min_y, sensor.y):
    #     borders.add(Point())
    # for y in range(min_y, max_y):
    #     diff_width = distance - abs(sensor.y - y)
    #     covered.update((x, y) for x in range(sensor.x - diff_width, sensor.x + diff_width + 1))

    # if min_y <= target_y <= max_y:
    #     diff_width = distance - abs(sensor.y - target_y)
    #     sections.append((sensor.x - diff_width, sensor.x + diff_width))

    # print(len(covered))
    # print((14, 11) in covered)
    # print(sections)
    #
    # coverage = set()
    # for begin, end in sections:
    #     coverage.update(range(begin, end + 1))
    # for sensor in sensors:
    #     if sensor.y == target_y:
    #         coverage.discard(sensor.x)
    # for beacon in beacons:
    #     if beacon.y == target_y:
    #         coverage.discard(beacon.x)

    # print(Point.min_x, Point.max_x, Point.min_y, Point.max_y)
    # print(len(coverage))


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
