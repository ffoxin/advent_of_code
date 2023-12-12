from collections import defaultdict

from main import data_path

DATA = data_path(__file__)


def puzzle1() -> None:
    with open(DATA, "r") as f:
        lines = f.readlines()

    field = [list(line.strip("\n")) for line in lines]

    temp = [[None] * len(line) for line in field]

    def check(x, y):
        counts = {
            ".": 0,
            "|": 0,
            "#": 0,
        }
        for xi in range(max(0, x - 1), min(len(field), x + 2)):
            for yi in range(max(0, y - 1), min(len(field[0]), y + 2)):
                if xi == x and yi == y:
                    continue
                counts[field[xi][yi]] += 1

        if field[x][y] == "." and counts["|"] >= 3:
            return "|"
        elif field[x][y] == "|" and counts["#"] >= 3:
            return "#"
        elif field[x][y] == "#":
            if counts["|"] >= 1 and counts["#"] >= 1:
                return "#"
            else:
                return "."

        return field[x][y]

    def print_field():
        print("-" * len(field))
        for line in field:
            print("".join(line))
        print("-" * len(field))

    print_field()
    for i in range(10):
        for j in range(len(field)):
            for k in range(len(field[j])):
                temp[j][k] = check(j, k)

        field, temp = temp, field
    print_field()

    result = defaultdict(int)
    for line in field:
        for ch in line:
            result[ch] += 1

    print(result["|"] * result["#"])


def puzzle2() -> None:
    with open(DATA, "r") as f:
        lines = f.readlines()

    field = [list(line.strip("\n")) for line in lines]

    temp = [[None] * len(line) for line in field]

    def check(x, y):
        counts = {
            ".": 0,
            "|": 0,
            "#": 0,
        }
        for xi in range(max(0, x - 1), min(len(field), x + 2)):
            for yi in range(max(0, y - 1), min(len(field[0]), y + 2)):
                if xi == x and yi == y:
                    continue
                counts[field[xi][yi]] += 1

        if field[x][y] == "." and counts["|"] >= 3:
            return "|"
        elif field[x][y] == "|" and counts["#"] >= 3:
            return "#"
        elif field[x][y] == "#":
            if counts["|"] >= 1 and counts["#"] >= 1:
                return "#"
            else:
                return "."

        return field[x][y]

    history = {}
    second = 0
    while True:
        for j in range(len(field)):
            for k in range(len(field[j])):
                temp[j][k] = check(j, k)
        second += 1

        field, temp = temp, field

        mark = "".join("".join(line) for line in field)
        if mark in history:
            second = history[mark]
            print("start repeating from", second)
            break
        else:
            history[mark] = second

    print("history", len(history))
    print("second", second)

    history_repeat = {}
    for key, value in history.items():
        if value >= second:
            history_repeat[key] = value - second

    result_second = (1000000000 - (second - 0)) % len(history_repeat)
    result_mark = [key for key, value in history_repeat.items() if value == result_second][0]

    print("history_repeat", len(history_repeat))
    print("result_second", result_second)
    print(result_mark)

    result = result_mark.count("|") * result_mark.count("#")

    print(result)
