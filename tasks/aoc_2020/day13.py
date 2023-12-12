from pathlib import Path

DATA = (Path(__file__).parent / "data" / "day13.txt").read_text()


def puzzle1() -> None:
    entries = [i for i in DATA.split("\n") if i]

    timestamp = int(entries[0])
    buses = [int(i) for i in entries[1].split(",") if i != "x"]

    bus_found = None
    bus_wait = None
    for bus in buses:
        before = timestamp % bus
        wait = bus - before
        if before == 0 or bus_wait is None or wait < bus_wait:
            bus_found = bus
            bus_wait = 0 if before == 0 else wait

    if bus_found is None:
        print("Nothing found")

    print(bus_found, bus_wait)
    print(bus_found * bus_wait)


def puzzle2() -> None:
    entries = [i for i in DATA.split("\n") if i]

    buses = [(int(bus), index) for index, bus in enumerate(entries[1].split(",")) if bus != "x"]
    for index, (bus, delay) in enumerate(buses):
        buses[index] = (bus, bus - delay)

    def get_inverted(a, b):
        for i in range(b):
            if (a * i) % b == 1:
                return i

    r = []
    for bus1, _ in buses:
        r.append([])
        for bus2, _ in buses:
            r[-1].append(get_inverted(bus1, bus2))
        print(r[-1])

    x = []
    for i in range(len(buses)):
        x.append(buses[i][1])
        for j in range(i):
            x[i] = r[j][i] * (x[i] - x[j])
            x[i] %= buses[i][0]
            if x[i] < 0:
                x[i] += buses[i][0]

    result = 0
    for index in range(len(buses)):
        value = x[index]
        for i in range(index):
            value *= buses[i][0]
        result += value
    print(result)


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
