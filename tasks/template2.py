from pathlib import Path

DATA = (Path(__file__).parent / 'data' / '{}').read_text()


def puzzle1():
    entries = [i for i in DATA.split('\n') if i]


# def puzzle2():
#     entries = [i for i in DATA.split('\n') if i]


if __name__ == '__main__':
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
