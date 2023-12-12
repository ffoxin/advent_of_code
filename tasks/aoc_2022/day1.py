from pathlib import Path

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()


def puzzle1() -> None:
    elves = [0]
    for line in DATA.split("\n"):
        if line:
            elves[-1] += int(line)
        else:
            if elves[-1] == 0:
                continue
            elves.append(0)

    if elves[-1] == 0:
        elves.pop(-1)

    print(max(elves))


def puzzle2() -> None:
    elves = [0]
    for line in DATA.split("\n"):
        if line:
            elves[-1] += int(line)
        else:
            if elves[-1] == 0:
                continue
            elves.append(0)

    if elves[-1] == 0:
        elves.pop(-1)

    print(sum(sorted(elves)[-3:]))


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
