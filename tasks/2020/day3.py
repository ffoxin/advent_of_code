from pathlib import Path

DATA = (Path(__file__).parent / 'data' / 'day3.txt').read_text()


def puzzle1():
    entries = [i for i in DATA.split('\n') if i]
    x, y = 0, 0
    x_, y_ = 3, 1
    trees = 0
    while True:
        x = (x + x_) % len(entries[0])
        y += y_
        if y == len(entries):
            break
        trees += entries[y][x] == '#'

    print(trees)


def puzzle2():
    entries = [i for i in DATA.split('\n') if i]

    traverses = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    result = 1
    for tr in traverses:
        x, y = 0, 0
        x_, y_ = tr
        trees = 0
        while True:
            x = (x + x_) % len(entries[0])
            y += y_
            if y >= len(entries):
                break
            trees += entries[y][x] == '#'

        print(trees)
        result *= trees
    print(result)


if __name__ == '__main__':
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
