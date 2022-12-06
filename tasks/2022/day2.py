from pathlib import Path

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()

opponent = dict(zip("ABC", "RPS"))
player = dict(zip("XYZ", "RPS"))
costs = dict(zip("RPS", [1, 2, 3]))
LOSE, DRAW, WIN = 0, 3, 6
strategy = {
    "R R": DRAW,
    "R P": WIN,
    "R S": LOSE,
    "P R": LOSE,
    "P P": DRAW,
    "P S": WIN,
    "S R": WIN,
    "S P": LOSE,
    "S S": DRAW,
}


def puzzle1():
    entries = list(filter(bool, DATA.split("\n")))

    result = sum(
        strategy[f"{opponent[line[0]]} {player[line[-1]]}"] + costs[player[line[-1]]]
        for line in entries
    )
    print(result)


part2 = dict(zip("XYZ", [LOSE, DRAW, WIN]))


def puzzle2():
    entries = list(filter(bool, DATA.split("\n")))

    result = 0
    for line in entries:
        for key, value in strategy.items():
            if key[0] == opponent[line[0]] and value == part2[line[-1]]:
                result += value + costs[key[-1]]
                break
    print(result)


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
