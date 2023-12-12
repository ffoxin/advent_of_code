from pathlib import Path

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()


def puzzle1() -> None:
    entries = list(filter(bool, DATA.split("\n")))
    timers = list(map(int, entries[0].split(",")))
    # print(f"Initial state: {','.join(map(str, timers))}")
    for _ in range(80):
        # prefix = f"After {i + 1:>2d} day{'s' if i else ''}: {'' if i else ' '}"

        new_count = 0
        new_timers = []
        for timer in timers:
            if timer == 0:
                new_timers.append(6)
                new_count += 1
            else:
                new_timers.append(timer - 1)
        timers = new_timers + [8] * new_count
        # print(f"{prefix}{','.join(map(str, timers))}")
    print(f"Result: {len(timers)}")
    # entries = list(map(int, filter(bool, DATA.split('\n'))))


def puzzle2() -> None:
    entries = list(filter(bool, DATA.split("\n")))
    timers = list(map(int, entries[0].split(",")))
    counts = {i: timers.count(i) for i in range(9)}

    for _ in range(256):
        new_fish = counts[0]
        counts = {count - 1: value for count, value in counts.items() if count > 0}
        counts[6] += new_fish
        counts[8] = new_fish

    print(sum(counts.values()))


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
