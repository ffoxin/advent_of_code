import re
from itertools import product
from pathlib import Path

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()

pattern = re.compile(r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)")


def puzzle1() -> None:
    entries = DATA.strip()
    x_min, x_max, y_min, y_max = tuple(map(int, pattern.match(entries).groups()))
    print(x_min, x_max, y_min, y_max)

    best_y = 0
    for x_vel, y_vel in product(range(x_max), range(abs(y_min))):
        x, y = 0, 0
        max_y = 0

        while True:
            x += x_vel
            y += y_vel
            max_y = max(max_y, y)

            if x_vel > 0:
                x_vel -= 1
            elif x_vel < 0:
                x_vel += 1
            y_vel -= 1

            if x > x_max or y < y_min:
                break
            if x_min <= x <= x_max and y_min <= y <= y_max:
                best_y = max(best_y, max_y)
                break

    print(f"Result: {best_y}")


def puzzle2() -> None:
    entries = DATA.strip()
    x_min, x_max, y_min, y_max = tuple(map(int, pattern.match(entries).groups()))
    print(x_min, x_max, y_min, y_max)

    shots_in_target = 0
    for x_vel, y_vel in product(range(1, x_max + 1), range(y_min, abs(y_min) + 1)):
        x, y = 0, 0

        while True:
            x += x_vel
            y += y_vel

            if x_vel > 0:
                x_vel -= 1
            elif x_vel < 0:
                x_vel += 1
            y_vel -= 1

            if x > x_max or y < y_min:
                break
            if x_min <= x <= x_max and y_min <= y <= y_max:
                shots_in_target += 1
                break

    print(f"Result: {shots_in_target}")


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
