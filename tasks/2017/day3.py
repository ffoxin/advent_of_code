from math import sqrt

VALUE = 347991


def calc_len(value):
    sqr = int(sqrt(value))
    sq1 = sqr ** 2
    sq2 = (sqr + 1) ** 2
    mid = (sq1 + sq2 - 1) // 2
    if sqr % 2 == 0:
        y = sqr // 2
        x = -y
        if value == sq1:
            x += 1
        elif value <= mid:
            y -= value - sq1 - 1
        else:
            x += value - mid - 1
            y = -y
    else:
        x = (sqr + 1) // 2
        y = -x + 1
        if value == sq1:
            x -= 1
        elif value <= mid:
            y += value - sq1 - 1
        else:
            x -= value - mid - 1
            y = -y + 1

    return x, y


def puzzle1():
    x, y = calc_len(VALUE)
    print(abs(x) + abs(y))


def puzzle2():
    size = 20
    start = size // 2

    array = [[None] * size for _ in range(size)]
    x = y = start

    def nxt():
        if array[x - 1][y] and not array[x][y + 1]:
            return x, y + 1
        elif array[x][y - 1] and not array[x - 1][y]:
            return x - 1, y
        elif array[x + 1][y] and not array[x][y - 1]:
            return x, y - 1
        elif array[x][y + 1] and not array[x + 1][y]:
            return x + 1, y
        else:
            raise RuntimeError("Cant find next: {}:{}".format(x, y))

    current = array[x][y] = array[x + 1][y] = 1
    x += 1

    while current < VALUE:
        x, y = nxt()
        current = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i == x and j == y:
                    continue
                value = array[i][j]
                if value:
                    current += value
        array[x][y] = current

    print(current)
