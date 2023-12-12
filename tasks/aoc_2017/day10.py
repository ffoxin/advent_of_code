from functools import reduce
from itertools import chain, product
from operator import xor

from main import data_path

DATA = data_path(__file__)

LEN = 256


def puzzle1() -> None:
    with open(DATA, "r") as f:
        lines = f.readlines()

    lengths = list(map(int, lines[0].strip().split(",")))

    array = list(range(LEN))
    current = 0
    skip = 0

    # array = [0, 1, 2, 3, 4]
    # lengths = [3, 4, 1, 5]
    # LEN = len(array)

    for length in lengths:
        start = current
        end = current + length
        if end < LEN:
            selected = list(reversed(array[start:end]))
            array = list(chain(array[:start], selected, array[end:]))
        else:
            end %= LEN
            selected = list(reversed(array[start:] + array[:end]))

            array = list(chain(selected[LEN - start :], array[end:start], selected[: LEN - start]))

        current += length + skip
        current %= LEN
        skip += 1

    print(array[0] * array[1])


def puzzle2() -> None:
    with open(DATA, "r") as f:
        lines = f.readlines()

    # lines = ['']
    # lines = ['AoC 2017']

    lengths = list(map(ord, lines[0].strip()))
    lengths += [17, 31, 73, 47, 23]

    array = list(range(LEN))
    current = 0
    skip = 0

    # array = [0, 1, 2, 3, 4]
    # lengths = [3, 4, 1, 5]
    # LEN = len(array)

    for _, length in product(range(64), lengths):
        start = current
        end = current + length
        if end < LEN:
            selected = list(reversed(array[start:end]))
            array = list(chain(array[:start], selected, array[end:]))
        else:
            end %= LEN
            selected = list(reversed(array[start:] + array[:end]))

            array = list(chain(selected[LEN - start :], array[end:start], selected[: LEN - start]))

        current += length + skip
        current %= LEN
        skip += 1

    hash_int = [reduce(xor, array[i : i + 16]) for i in range(0, 256, 16)]
    hash_str = "".join(map(lambda x: hex(x)[2:], hash_int))

    print(hash_str)
