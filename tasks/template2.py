from pathlib import Path

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()


def puzzle1() -> None:
    entries = list(filter(bool, DATA.split("\n")))
    # entries = list(map(int, filtergit (bool, DATA.split('\n'))))


# def puzzle2() -> None:
#     entries = list(filter(bool, DATA.split('\n')))
#     # entries = list(map(int, filter(bool, DATA.split('\n'))))


if __name__ == "__main__":
    try:
        puzzle2()  # type: ignore [name-defined]
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
