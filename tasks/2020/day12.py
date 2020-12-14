from pathlib import Path

DATA = (Path(__file__).parent / 'data' / 'day12.txt').read_text()


def puzzle1():
    entries = [i for i in DATA.split('\n') if i]

    direction = 0
    x, y = 0, 0
    cmds = {
        'N': lambda val: (0, val, 0),
        'S': lambda val: (0, -val, 0),
        'E': lambda val: (val, 0, 0),
        'W': lambda val: (-val, 0, 0),
        'L': lambda degrees: (0, 0, -degrees),
        'R': lambda degrees: (0, 0, degrees),
        'F': lambda val: {
            0: (val, 0, 0),
            90: (0, -val, 0),
            180: (-val, 0, 0),
            270: (0, val, 0),
        }[direction],
    }
    for entry in entries:
        cmd = entry[0]
        param = int(entry[1:])
        dx, dy, dd = cmds[cmd](param)
        x += dx
        y += dy
        direction = (direction + dd) % 360

    print(sum(map(abs, [x, y])))


def puzzle2():
    entries = [i for i in DATA.split('\n') if i]

    x, y = 0, 0
    wx, wy = 10, 1
    cmds = {
        'N': lambda val: (0, 0, 0, val),
        'S': lambda val: (0, 0, 0, -val),
        'E': lambda val: (0, 0, val, 0),
        'W': lambda val: (0, 0, -val, 0),
        'L': lambda degrees: {
            0: (0, 0, 0, 0),
            90: (0, 0, -wx - wy, -wy + wx),
            180: (0, 0, -2 * wx, -2 * wy),
            270: (0, 0, -wx + wy, -wy - wx),
        }[degrees % 360],
        'R': lambda degrees: {
            0: (0, 0, 0, 0),
            90: (0, 0, -wx + wy, -wy - wx),
            180: (0, 0, -2 * wx, -2 * wy),
            270: (0, 0, -wx - wy, -wy + wx),
        }[degrees % 360],
        'F': lambda val: (wx * val, wy * val, 0, 0),
    }
    for entry in entries:
        cmd = entry[0]
        param = int(entry[1:])
        dx, dy, dwx, dwy = cmds[cmd](param)
        x += dx
        y += dy
        wx += dwx
        wy += dwy
        # print(x, y, wx, wy)

    print(x, y)
    print(sum(map(abs, [x, y])))


if __name__ == '__main__':
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
