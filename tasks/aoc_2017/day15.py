start_a = 883
start_b = 879
factor_a = 16807
factor_b = 48271
prod = 2147483647


def puzzle1() -> None:
    # start_a = 65
    # start_b = 8921

    a = start_a
    b = start_b
    result = 0
    for i in range(40000000):
        a = (a * factor_a) % prod
        b = (b * factor_b) % prod
        if a & 0xFFFF == b & 0xFFFF:
            result += 1

    print(result)


def puzzle2() -> None:
    # start_a = 65
    # start_b = 8921

    a = start_a
    b = start_b
    result = 0
    for i in range(5000000):
        while True:
            a = (a * factor_a) % prod
            if a % 4 == 0:
                break
        while True:
            b = (b * factor_b) % prod
            if b % 8 == 0:
                break
        if a & 0xFFFF == b & 0xFFFF:
            result += 1

    print(result)
