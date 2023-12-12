from main import data_path

DATA = data_path(__file__)


def puzzle1() -> None:
    with open(DATA, "r") as f:
        lines = f.readlines()

    jumps = list(map(int, lines))
    step = 0
    jumps_len = len(jumps)
    count = 0
    while step < jumps_len:
        count += 1
        nxt = jumps[step]
        jumps[step] += 1
        step += nxt
    print(count)


def puzzle2() -> None:
    with open(DATA, "r") as f:
        lines = f.readlines()

    jumps = list(map(int, lines))
    step = 0
    jumps_len = len(jumps)
    count = 0
    while step < jumps_len:
        count += 1
        nxt = jumps[step]
        jumps[step] += 1 if nxt < 3 else -1
        step += nxt
    print(count)
