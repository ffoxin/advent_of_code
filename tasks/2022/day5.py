import re
from collections import deque
from operator import itemgetter
from pathlib import Path

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()

move_pattern = re.compile(r"move (\d+) from (\d+) to (\d+)")


def puzzle1():
    entries = list(DATA.split("\n"))

    split_line_index = entries.index("")
    num_stacks = list(map(int, entries[split_line_index - 1].split()))[-1]
    stacks = [deque() for _ in range(num_stacks)]
    for line in entries[: split_line_index - 1]:
        start = 0
        while True:
            next_crate = line.find("[", start)
            if next_crate == -1:
                break
            start = next_crate + 1
            stack_index = next_crate // 4
            stacks[stack_index].appendleft(line[next_crate + 1])

    for line in entries[split_line_index + 1 :]:
        if not line:
            continue
        amount, source, dest = map(int, move_pattern.match(line).groups())
        for _ in range(amount):
            stacks[dest - 1].append(stacks[source - 1].pop())

    print("".join(map(itemgetter(-1), stacks)))


def puzzle2():
    entries = list(DATA.split("\n"))

    split_line_index = entries.index("")
    num_stacks = list(map(int, entries[split_line_index - 1].split()))[-1]
    stacks = [deque() for _ in range(num_stacks)]
    for line in entries[: split_line_index - 1]:
        start = 0
        while True:
            next_crate = line.find("[", start)
            if next_crate == -1:
                break
            start = next_crate + 1
            stack_index = next_crate // 4
            stacks[stack_index].appendleft(line[next_crate + 1])

    for line in entries[split_line_index + 1 :]:
        if not line:
            continue
        amount, source, dest = map(int, move_pattern.match(line).groups())
        dst_len = len(stacks[dest - 1])
        for _ in range(amount):
            stacks[dest - 1].insert(dst_len, stacks[source - 1].pop())

    print("".join(map(itemgetter(-1), stacks)))


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
