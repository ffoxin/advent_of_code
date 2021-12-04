from main import data_path

DATA = data_path(__file__)


def puzzle1():
    with open(DATA, "r") as f:
        lines = f.readlines()

    steps = lines[0].strip().split(",")

    x = y = 0

    def dist():
        return max(abs(x), abs(y)) + ((x % 2) if y < 0 else 0)

    for step in steps:
        odd = x % 2 == 1
        if step == "n":
            y += 1
        elif step == "s":
            y -= 1
        elif step == "nw":
            if odd:
                y += 1
            x -= 1
        elif step == "ne":
            if odd:
                y += 1
            x += 1
        elif step == "sw":
            if odd:
                y -= 1
            x -= 1
        elif step == "se":
            if odd:
                y -= 1
            x += 1

    print(dist())


def puzzle2():
    with open(DATA, "r") as f:
        lines = f.readlines()

    # lines = ['ne,ne,ne']
    # lines = ['ne,ne,sw,sw']
    # lines = ['ne,ne,s,s']
    # lines = ['se,sw,se,sw,sw']
    # lines = ['se,sw']
    steps = lines[0].strip().split(",")

    x = y = 0

    def dist():
        return max(abs(x), abs(y)) + ((x % 2) if y < 0 else 0)

    max_dist = 0

    for step in steps:
        odd = x % 2 == 1
        if step == "n":
            y += 1
        elif step == "s":
            y -= 1
        elif step == "nw":
            if odd:
                y += 1
            x -= 1
        elif step == "ne":
            if odd:
                y += 1
            x += 1
        elif step == "sw":
            if odd:
                y -= 1
            x -= 1
        elif step == "se":
            if odd:
                y -= 1
            x += 1

        max_dist = max(max_dist, dist())

    print(max_dist)
