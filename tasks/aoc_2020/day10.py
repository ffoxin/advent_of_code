from collections import Counter
from pathlib import Path

DATA = (Path(__file__).parent / "data" / "day10.txt").read_text()


def puzzle1() -> None:
    entries = [int(i) for i in DATA.split("\n") if i]

    entries.extend([0, max(entries) + 3])
    entries = sorted(entries)
    diffs = [entries[i] - entries[i - 1] for i in range(1, len(entries))]
    data = dict(Counter(diffs))

    print(data[1] * data[3])


def puzzle2() -> None:
    entries = [int(i) for i in DATA.split("\n") if i]

    entries.extend([0, max(entries) + 3])
    entries = sorted(entries)
    diffs = [entries[i] - entries[i - 1] for i in range(1, len(entries))]
    lengths = [1]
    for i in range(1, len(diffs)):
        if diffs[i] == diffs[i - 1] == 1:
            lengths[-1] += 1
        else:
            lengths.append(1)

    result = 1
    for i in lengths:
        if i == 1:
            continue
        if i == 2:
            result *= 2
        elif i == 3:
            result *= 4
        else:
            result *= 7 ** (i - 3)
    print(result)


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
