def puzzle1():
    data = 'tasks/2015/data/day1.txt'

    with open(data, 'r') as f:
        path = f.read()
    floor = path.count('(') - path.count(')')

    print(floor)


def puzzle2():
    data = 'tasks/2015/data/day1.txt'

    with open(data, 'r') as f:
        path = f.read()
    floor = 0
    for index, move in enumerate(path):
        floor += 1 if move == '(' else -1
        if floor == -1:
            print(index + 1)
            return
