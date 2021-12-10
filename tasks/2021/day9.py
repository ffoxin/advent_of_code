from itertools import product
from pathlib import Path

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()


def puzzle1():
    entries = list(
        map(lambda x: list(map(int, list(x))), filter(bool, DATA.split("\n")))
    )

    max_row = len(entries)
    max_col = len(entries[0])

    def is_low(row: int, col: int) -> bool:
        value = entries[row][col]
        for r, c in (
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1),
        ):
            if r < 0 or r >= max_row or c < 0 or c >= max_col:
                continue
            if value >= entries[r][c]:
                return False
        return True

    lows = []
    for rr, cc in product(range(max_row), range(max_col)):
        if is_low(rr, cc):
            lows.append(entries[rr][cc])

    print(lows)
    print(f"Result: {sum(lows) + len(lows)}")


def puzzle2():
    entries = list(
        map(lambda x: list(map(int, list(x))), filter(bool, DATA.split("\n")))
    )

    max_row = len(entries)
    max_col = len(entries[0])

    def is_low(row: int, col: int) -> bool:
        value = entries[row][col]
        for r, c in (
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1),
        ):
            if r < 0 or r >= max_row or c < 0 or c >= max_col:
                continue
            if value >= entries[r][c]:
                return False
        return True

    lows = []
    for rr, cc in product(range(max_row), range(max_col)):
        if is_low(rr, cc):
            lows.append((rr, cc))

    basins = []
    for rr, cc in lows:
        points = {(rr, cc)}
        while True:
            new_points = set()
            for point_r, point_c in points:
                for rn, cn in (
                    (point_r - 1, point_c),
                    (point_r + 1, point_c),
                    (point_r, point_c - 1),
                    (point_r, point_c + 1),
                ):
                    if rn < 0 or rn >= max_row or cn < 0 or cn >= max_col:
                        continue
                    if entries[rn][cn] != 9:
                        new_points.add((rn, cn))
            if not (new_points - points):
                break
            points.update(new_points)
        basins.append(points)

    unique = []
    for basin in basins:
        is_unique = True
        for u in unique:
            if basin & u:
                is_unique = False
                break
        if is_unique:
            unique.append(basin)

    sizes = sorted(list(map(len, unique)))
    print(f"Result: {sizes[-1] * sizes[-2] * sizes[-3]}")


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
