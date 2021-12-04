from main import data_path

DATA = data_path(__file__)


def puzzle1():
    with open(DATA, "r") as f:
        lines = f.readlines()

    result = 0
    for line in lines:
        values = list(map(int, line.split()))
        result += max(values) - min(values)

    print(result)


def puzzle2():
    with open(DATA, "r") as f:
        lines = f.readlines()

    result = 0
    for line in lines:
        values = list(map(int, line.split()))
        for i in range(len(values)):
            for j in range(len(values)):
                if i == j:
                    continue
                if values[i] % values[j] == 0:
                    result += values[i] // values[j]

    print(result)
