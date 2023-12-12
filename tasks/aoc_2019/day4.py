from collections import Counter


RANGE = (172851, 675869)


def puzzle1() -> None:
    start, end = RANGE

    def check(value):
        value_str = str(value)

        count = Counter(value_str)
        if count.most_common(1)[0][1] == 1:
            return False

        for j in range(len(value_str) - 1):
            if value_str[j] > value_str[j + 1]:
                return False

        return True

    assert check(111111)
    assert not check(223450)
    assert not check(123789)

    total = 0
    for i in range(start, end + 1):
        if check(i):
            total += 1

    print(total)


def puzzle2() -> None:
    # 1305 - too high

    start, end = RANGE

    def check(value):
        value_str = str(value)

        count = Counter(value_str)
        if not any(cnt == 2 for _, cnt in count.most_common()):
            return False

        for j in range(len(value_str) - 1):
            if value_str[j] > value_str[j + 1]:
                return False

        return True

    assert check(112233)
    assert not check(123444)
    assert check(111122)

    total = 0
    for i in range(start, end + 1):
        if check(i):
            total += 1

    print(total)
