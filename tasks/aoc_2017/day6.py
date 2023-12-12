from main import data_path

DATA = data_path(__file__)


def puzzle1() -> None:
    with open(DATA, "r") as f:
        lines = f.readlines()

    memory = list(map(int, lines[0].split()))
    memory_size = len(memory)

    def realloc(index):
        value = memory[index]
        memory[index] = 0
        if value >= memory_size:
            adding = value // memory_size
            for i in range(memory_size):
                memory[i] += adding
        rest = value % memory_size
        for i in range(rest):
            index += 1
            index %= memory_size
            memory[index] += 1

    seen = set()
    while True:
        snapshot = ",".join(map(str, memory))
        if snapshot in seen:
            break
        seen.add(snapshot)
        realloc(memory.index(max(memory)))
    print(len(seen))


def puzzle2() -> None:
    with open(DATA, "r") as f:
        lines = f.readlines()

    memory = list(map(int, lines[0].split()))
    memory_size = len(memory)

    def realloc(index):
        value = memory[index]
        memory[index] = 0
        if value >= memory_size:
            adding = value // memory_size
            for i in range(memory_size):
                memory[i] += adding
        rest = value % memory_size
        for i in range(rest):
            index += 1
            index %= memory_size
            memory[index] += 1

    seen = set()
    while True:
        snapshot = ",".join(map(str, memory))
        if snapshot in seen:
            break
        seen.add(snapshot)
        realloc(memory.index(max(memory)))

    again = set()
    while True:
        snapshot = ",".join(map(str, memory))
        if snapshot in again:
            break
        again.add(snapshot)
        realloc(memory.index(max(memory)))

    print(len(again))
