from pathlib import Path

DATA = (Path(__file__).parent / "data" / "day2.txt").read_text()


def puzzle1():
    entries = list(filter(bool, DATA.split("\n")))

    class Point:
        __slots__ = ("x", "y")

        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y

        def __add__(self, other: "Point") -> "Point":
            return self.__class__(self.x + other.x, self.y + other.y)

        def __repr__(self):
            return f"<Point({self.x}, {self.y})>"

    movement = {
        "forward": lambda x: Point(x, 0),
        "down": lambda x: Point(0, x),
        "up": lambda x: Point(0, -x),
    }

    pos = Point(0, 0)
    for item in entries:
        command, value = item.split()
        pos += movement[command](int(value))

    print(pos)
    print(pos.x * pos.y)


def puzzle2():
    entries = list(filter(bool, DATA.split("\n")))

    pos, depth, aim = 0, 0, 0
    for item in entries:
        command, value = item.split()
        value = int(value)
        if command == "down":
            aim += value
        elif command == "up":
            aim -= value
        elif command == "forward":
            pos += value
            depth += aim * value
        else:
            raise RuntimeError(f"Unknown command: {command}")

    print(pos, depth, aim)
    print(pos * depth)


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
