from pathlib import Path

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()


def puzzle1():
    entries = list(filter(bool, DATA.split("\n")))
    entries = list(map(int, entries[0].split(",")))

    min_pos = min(entries)
    max_pos = max(entries)
    min_cost, pos = None, None

    for i in range(min_pos, max_pos + 1):
        cost = sum(abs(i - item) for item in entries)
        if min_cost is None or cost < min_cost:
            min_cost = cost
            pos = i

    print(f"Min cost: {min_cost} (pos={pos})")

    # entries = list(map(int, filter(bool, DATA.split('\n'))))


def puzzle2():
    entries = list(filter(bool, DATA.split("\n")))
    entries = list(map(int, entries[0].split(",")))

    min_pos = min(entries)
    max_pos = max(entries)
    min_cost, pos = None, None

    costs = {0: 0}
    for i in range(1, max_pos - min_pos + 1):
        costs[i] = i + costs[i - 1]

    for i in range(min_pos, max_pos + 1):
        cost = sum(costs[abs(i - item)] for item in entries)
        if min_cost is None or cost < min_cost:
            min_cost = cost
            pos = i

    print(f"Min cost: {min_cost} (pos={pos})")


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
