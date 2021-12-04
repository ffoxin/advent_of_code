from collections import deque, defaultdict, Counter
from pathlib import Path

DATA = (Path(__file__).parent / "data" / "day15.txt").read_text()


def puzzle1():
    entries = [i for i in DATA.split("\n") if i]

    numbers = list(map(int, entries[0].split(",")))

    def iterable_rfind(it, target):
        for index, value in enumerate(reversed(it)):
            if value == target:
                return len(it) - 1 - index

    while len(numbers) < 2020:
        last = numbers[-1]
        count = numbers.count(last)
        if count == 1:
            numbers.append(0)
        else:
            numbers.append(len(numbers) - 1 - iterable_rfind(numbers[:-1], last))

    print(numbers[-1])


def puzzle2():
    entries = [i for i in DATA.split("\n") if i]

    target_index = 30000000
    numbers = [0 for i in range(target_index)]
    start_numbers = list(map(int, entries[0].split(",")))
    lasts = {}

    def update_lasts(value, position):
        if value in lasts:
            lasts[value] = (position, lasts[value][0])
        else:
            lasts[value] = (position, None)

    for index, i in enumerate(start_numbers):
        numbers[index] = i
        update_lasts(i, index)

    answer = start_numbers[-1]
    for i in range(len(start_numbers), target_index):
        if lasts[answer][1] is None:
            answer = 0
        else:
            pair = lasts[answer]
            answer = pair[0] - pair[1]

        update_lasts(answer, i)

    print(answer)


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
