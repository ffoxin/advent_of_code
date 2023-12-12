from main import data_path

DATA = data_path(__file__)


def puzzle1() -> None:
    with open(DATA, "r") as f:
        data = f.read().strip()

    array = list(map(int, list(data)))
    length = len(array)
    result = 0
    for i in range(length):
        if array[i] == array[(i + 1) % length]:
            result += array[i]

    print(result)


def puzzle2() -> None:
    with open(DATA, "r") as f:
        data = f.read().strip()

    array = list(map(int, list(data)))
    length = len(array)
    half_len = length // 2
    result = 0
    for i in range(length):
        if array[i] == array[(i + half_len) % length]:
            result += array[i]

    print(result)
