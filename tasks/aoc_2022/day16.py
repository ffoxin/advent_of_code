import re
from itertools import chain
from pathlib import Path
from typing import List, Dict, Set

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()


class Valve:
    def __init__(self, name: str, rate: int, valves: List[str]):
        self.name = name
        self.rate = rate
        self.valves: List[str] = valves


line_pattern = re.compile(
    r"^Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z, ]+)$"
)


def puzzle1() -> None:
    entries = list(filter(bool, DATA.split("\n")))

    network: Dict[str, Valve] = {}
    for line in entries:
        print(line)
        name, rate_str, valves_str = line_pattern.fullmatch(line).groups()
        rate = int(rate_str)
        valves = valves_str.split(", ")
        network[name] = Valve(name, rate, valves)

    current = "AA"
    for i in range(30):
        visited: Set[str] = {current}
        far = 0
        max_rate = 0
        max_name = None
        while True:
            far += 1
            rest = 30 - i - far
            next_names = set(
                new_name
                for new_name in chain.from_iterable(network[name].valves for name in visited)
                if new_name not in visited
            )
            visited.update(next_names)
            if not next_names:
                break
            for name in next_names:
                rate = rest * network[name].rate
                if rate > max_rate:
                    max_rate = rate
                    max_name = name

        print(max_name, max_rate, far)
        break

    # entries = list(map(int, filter(bool, DATA.split('\n'))))


# def puzzle2() -> None:
#     entries = list(filter(bool, DATA.split('\n')))
#     # entries = list(map(int, filter(bool, DATA.split('\n'))))


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
