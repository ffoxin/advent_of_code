from functools import reduce
from itertools import product, chain
from operator import xor

DATA = "jzgqcdpd"

LEN = 256


def knot_hash(s):
    lengths = list(map(ord, s.strip()))
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
    hash_str = "".join(map(lambda x: format(x, "02x"), hash_int))

    return hash_str


translate = {str(i): format(i, "04b") for i in range(10)}
translate.update(
    {chr(ch): format(ch - ord("a") + 10, "04b") for ch in range(ord("a"), ord("f") + 1)}
)


def hash2bin(s):
    return "".join(translate[ch] for ch in s)


def puzzle1() -> None:
    result = 0
    for i in range(128):
        s = f"{DATA}-{i}"
        result += hash2bin(knot_hash(s)).count("1")

    print(result)


def puzzle2() -> None:
    # DATA = 'flqrgnkx'
    limit = 0

    disk = []
    for i in range(limit or 128):
        result = f"{DATA}-{i}"
        disk.append(list(hash2bin(knot_hash(result))))

    def mark(x, y):
        if disk[x][y] != "1":
            return 0

        added = {(x, y)}
        while added:
            next_add = set()
            for x1, y1 in added:
                disk[x1][y1] = "#"
                next_add.update(
                    {
                        (x2, y2)
                        for (x2, y2) in (
                            (x1 + 1, y1),
                            (x1 - 1, y1),
                            (x1, y1 + 1),
                            (x1, y1 - 1),
                        )
                        if 0 <= x2 < 128 and 0 <= y2 < 128 and disk[x2][y2] == "1"
                    }
                )

            added = next_add

        return 1

    result = 0
    for i in range(len(disk)):
        for j in range(len(disk[i])):
            result += mark(i, j)
    for i in disk:
        print(i)

    print(result)
