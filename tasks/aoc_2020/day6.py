from pathlib import Path

DATA = (Path(__file__).parent / "data" / "day6.txt").read_text()


def puzzle1() -> None:
    entries = [i for i in DATA.split("\n")]
    groups = [set()]
    for entry in entries:
        if not entry:
            if groups[-1]:
                groups.append(set())
            continue

        groups[-1].update(entry)

    print(sum(map(len, groups)))


def puzzle2() -> None:
    entries = [i for i in DATA.split("\n")]
    groups = [[]]
    for entry in entries:
        if not entry:
            if groups[-1]:
                groups.append([])
            continue
        groups[-1].append(entry)

    print(sum(len(set.intersection(*map(set, group))) for group in groups if group))


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
