from main import data_path

DATA = data_path(__file__)


def puzzle1():
    with open(DATA, 'r') as f:
        lines = f.readlines()

    lines1 = [
        '0: 3',
        '1: 2',
        '4: 4',
        '6: 4',
    ]

    depth = {int(line.split(':')[0]): int(line.split(':')[1]) for line in lines}

    result = 0
    for i, d in depth.items():
        if i % (d * 2 - 2) == 0:
            result += i * d

    print(result)


def puzzle2():
    with open(DATA, 'r') as f:
        lines = f.readlines()

    lines1 = [
        '0: 3',
        '1: 2',
        '4: 4',
        '6: 4',
    ]

    depth = {int(line.split(':')[0]): int(line.split(':')[1]) for line in lines}

    found = False
    delay = 0
    while not found:
        for i, d in depth.items():
            if (i + delay) % (d * 2 - 2) == 0:
                delay += 1
                break
        else:
            found = True

    print(delay)
