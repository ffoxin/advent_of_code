from pathlib import Path

DATA = (Path(__file__).parent / "data" / "day9.txt").read_text()


def puzzle1() -> None:
    entries = [int(i) for i in DATA.split("\n") if i]

    preamble = 25
    for i in range(len(entries)):
        if i < preamble:
            continue

        found = False
        for j in range(preamble):
            for k in range(preamble):
                if j == k:
                    continue
                if entries[i] == entries[i - j - 1] + entries[i - k - 1]:
                    found = True
                if found:
                    break
            if found:
                break
        if not found:
            print(entries[i])
            return entries[i]


def puzzle2() -> None:
    entries = [int(i) for i in DATA.split("\n") if i]

    target = puzzle1()
    start, end = 0, 1
    while True:
        s = sum(entries[start : end + 1])
        if s < target:
            end += 1
        elif s > target:
            start += 1
            if start == end:
                end += 1
        else:
            result = min(entries[start : end + 1]) + max(entries[start : end + 1])
            print(result)
            break


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
