from pathlib import Path

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()


def puzzle1() -> None:
    entries = list(filter(bool, DATA.split("\n")))

    length = 4
    for stream in entries:
        for i in range(len(stream) - length + 1):
            if len(set(stream[i : i + length])) != length:
                continue
            print(i + length)
            break


def puzzle2() -> None:
    entries = list(filter(bool, DATA.split("\n")))

    length = 14
    for stream in entries:
        for i in range(len(stream) - length + 1):
            if len(set(stream[i : i + length])) != length:
                continue
            print(i + length)
            break


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
