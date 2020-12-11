from itertools import product
from pathlib import Path

DATA = (Path(__file__).parent / 'data' / 'day11.txt').read_text()


def puzzle1():
    entries = [i for i in DATA.split('\n') if i]
    width = len(entries[0])
    height = len(entries)

    def check(row, column):
        count = 0
        for r, c in product(
                range(row - 1, row + 2),
                range(column - 1, column + 2)
        ):
            if r < 0 or c < 0 or r >= height or c >= width or (r == row and c == column):
                continue
            count += entries[r][c] == '#'
        return count

    while True:
        # print('\n'.join(entries) + '\n=====')
        next_step = ['' for _ in range(height)]
        for i in range(height):
            for j in range(width):
                occupied = check(i, j)
                current = entries[i][j]
                if current == 'L' and occupied == 0:
                    seat = '#'
                elif current == '#' and occupied >= 4:
                    seat = 'L'
                else:
                    seat = entries[i][j]
                next_step[i] += seat

        if next_step == entries:
            break
        entries = next_step

    print(sum(line.count('#') for line in entries))


def puzzle2():
    entries = [i for i in DATA.split('\n') if i]
    width = len(entries[0])
    height = len(entries)

    def check(row, column):
        count = 0
        for ir, ic in product([-1, 0, 1], repeat=2):
            if ir == ic == 0:
                continue
            height_target = height if ir > 0 else -1
            width_target = width if ic > 0 else -1
            r, c = row, column
            while True:
                r += ir
                c += ic
                if r == height_target or c == width_target:
                    break
                if entries[r][c] == 'L':
                    break
                if entries[r][c] == '#':
                    count += 1
                    break

        return count

    while True:
        # print('\n'.join(entries) + '\n=====')
        next_step = ['' for _ in range(height)]
        for i in range(height):
            for j in range(width):
                occupied = check(i, j)
                current = entries[i][j]
                if current == 'L' and occupied == 0:
                    seat = '#'
                elif current == '#' and occupied >= 5:
                    seat = 'L'
                else:
                    seat = entries[i][j]
                next_step[i] += seat

        if next_step == entries:
            break
        entries = next_step

    print(sum(line.count('#') for line in entries))


if __name__ == '__main__':
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
