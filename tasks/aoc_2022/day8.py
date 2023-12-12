from itertools import product
from pathlib import Path

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()


def puzzle1() -> None:
    entries = list(filter(bool, DATA.split("\n")))
    forest = [list(map(int, line)) for line in entries]

    result = 2 * (len(forest) + len(forest[0])) - 4
    for y, x in product(
        range(1, len(forest) - 1),
        range(1, len(forest[0]) - 1),
    ):
        value = forest[y][x]
        if (
            all(forest[y][i] < value for i in range(x))
            or all(forest[y][i] < value for i in range(x + 1, len(forest[0])))
            or all(forest[i][x] < value for i in range(y))
            or all(forest[i][x] < value for i in range(y + 1, len(forest)))
        ):
            result += 1

    print(result)


def puzzle2() -> None:
    entries = list(filter(bool, DATA.split("\n")))
    forest = [list(map(int, line)) for line in entries]

    max_score = 0
    for y, x in product(
        range(1, len(forest) - 1),
        range(1, len(forest[0]) - 1),
    ):
        value = forest[y][x]
        score = 1

        for i in range(x - 1, -1, -1):
            if forest[y][i] >= value:
                score *= x - i
                break
        else:
            score *= x - i

        for i in range(x + 1, len(forest[0])):
            if forest[y][i] >= value:
                score *= i - x
                break
        else:
            score *= i - x

        for i in range(y - 1, -1, -1):
            if forest[i][x] >= value:
                score *= y - i
                break
        else:
            score *= y - i

        for i in range(y + 1, len(forest)):
            if forest[i][x] >= value:
                score *= i - y
                break
        else:
            score *= i - y

        print(f"[{x}, {y}] -> {score}")
        max_score = max(score, max_score)

    print(max_score)


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
