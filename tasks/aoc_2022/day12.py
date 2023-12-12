from pathlib import Path

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()


def puzzle1() -> None:
    entries = list(filter(bool, DATA.split("\n")))

    start, end = None, None
    max_y = len(entries)
    max_x = len(entries[0])
    geo = {}
    for y, line in enumerate(entries):
        for x, ch in enumerate(line):
            if ch == "S":
                ch = "a"
                start = (x, y)
            elif ch == "E":
                ch = "z"
                end = (x, y)
            geo[(x, y)] = ord(ch) - ord("a")

    visited = {start: 0}
    currents = {start}
    while True:
        neighbors = set()
        updated = False
        for point in currents:
            assert visited[point] is not None
            x, y = point
            surrounded = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
            surrounded = [
                (sx, sy)
                for sx, sy in surrounded
                if 0 <= sx < max_x and 0 <= sy < max_y and geo[(sx, sy)] - geo[point] <= 1
            ]
            for spoint in surrounded:
                if spoint not in visited or visited[spoint] > visited[point] + 1:
                    visited[spoint] = visited[point] + 1
                    updated = True
                    neighbors.add(spoint)

        if not updated:
            break

        currents = neighbors

    print(visited[end])


def puzzle2() -> None:
    entries = list(filter(bool, DATA.split("\n")))

    start, end = None, None
    max_y = len(entries)
    max_x = len(entries[0])
    geo = {}
    starts = []
    for y, line in enumerate(entries):
        for x, ch in enumerate(line):
            if ch == "S":
                ch = "a"
            elif ch == "E":
                ch = "z"
                end = (x, y)
            geo[(x, y)] = ord(ch) - ord("a")
            if ch == "a":
                starts.append((x, y))

    results = []
    for start in starts:
        visited = {start: 0}
        currents = {start}
        while True:
            neighbors = set()
            updated = False
            for point in currents:
                assert visited[point] is not None
                x, y = point
                surrounded = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
                surrounded = [
                    (sx, sy)
                    for sx, sy in surrounded
                    if 0 <= sx < max_x and 0 <= sy < max_y and geo[(sx, sy)] - geo[point] <= 1
                ]
                for spoint in surrounded:
                    if spoint not in visited or visited[spoint] > visited[point] + 1:
                        visited[spoint] = visited[point] + 1
                        updated = True
                        neighbors.add(spoint)

            if not updated:
                break

            currents = neighbors

        if end in visited:
            results.append(visited[end])

    print(min(results))


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
