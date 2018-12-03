from collections import Counter

from main import data_path

DATA = data_path(__file__)


def puzzle1():
    with open(DATA, 'r') as f:
        lines = f.readlines()

    lines = map(str.strip, lines)
    lines = map(Counter, lines)
    lines = map(Counter.values, lines)
    lines = map(set, lines)
    lines = list(lines)

    match2 = 0
    match3 = 0
    for line in lines:
        if 2 in line:
            match2 += 1
        if 3 in line:
            match3 += 1

    print(match2 * match3)


def puzzle2():
    with open(DATA, 'r') as f:
        lines = f.readlines()

    lines = map(str.strip, lines)
    lines = list(lines)
    # lines = sorted(lines)
    counts = map(Counter, lines)
    counts = map(Counter.keys, counts)
    counts = map(set, counts)
    counts = list(counts)

    for i in range(len(counts) - 1):
        a = counts[i]
        for j in range(i + 1, len(counts)):
            b = counts[j]
            if len(a & b) >= len(a) - 1:
                diff = 0
                common = ''
                for ca, cb in zip(lines[i], lines[j]):
                    if ca != cb:
                        diff += 1
                    else:
                        common += ca
                    if diff > 1:
                        break
                else:
                    print(lines[i])
                    print(lines[j])
                    print(common)
