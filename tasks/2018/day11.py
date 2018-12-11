import sys


def get_power(x, y, serial):
    rack_id = x + 10
    power = rack_id * y
    power += serial
    power *= rack_id
    power = power // 100 % 10
    power -= 5

    return power


def puzzle1():
    serial = 5468
    grid = [[None] * 300 for _ in range(300)]

    for y in range(300):
        for x in range(300):
            grid[x][y] = get_power(x + 1, y + 1, serial)

    max_power = None
    point = ()
    for x in range(300 - 2):
        for y in range(300 - 2):
            power = sum((
                grid[i][j]
                for i in range(x, x + 3)
                for j in range(y, y + 3)
            ))
            if max_power is None or power > max_power:
                max_power = power
                point = (x + 1, y + 1)

    print(','.join(map(str, point)))


def puzzle2():
    serial = 5468
    grid = [[None] * 300 for _ in range(300)]

    for y in range(300):
        for x in range(300):
            grid[x][y] = get_power(x + 1, y + 1, serial)

    max_sum = - sys.maxsize - 1
    max_x = 0
    max_y = 0
    max_size = 0
    repo = {}
    for size in range(1, 300 + 1):
        for i in range(300 - size):
            for j in range(300 - size):
                if size > 2:
                    current = (
                            repo[(i, j, size - 1)] +
                            repo[(i + 1, j + 1, size - 1)] -
                            repo[(i + 1, j + 1, size - 2)] +
                            grid[i + size - 1][j] +
                            grid[i][j + size - 1]
                    )
                else:
                    current = sum(
                        grid[x][y]
                        for x in range(i, i + size)
                        for y in range(j, j + size)
                    )
                repo[(i, j, size)] = current
                if current > max_sum:
                    max_sum = current
                    max_x = i
                    max_y = j
                    max_size = size

        print(size)

    print('{},{},{}'.format(max_x + 1, max_y + 1, max_size))
