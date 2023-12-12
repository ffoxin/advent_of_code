import operator
import re
from collections import defaultdict, Counter
from itertools import product, combinations
from pathlib import Path
from typing import Dict, Tuple, List, Callable

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()

scanner_template = re.compile(r"--- scanner (\d+) ---")
beacon_template = re.compile(r"(-?\d+),(-?\d+),?(-?\d+)?")


def coord_samples() -> List[Tuple[Callable, Callable]]:
    rotators = [
        lambda t: (t[0], t[1], t[2]),
        lambda t: (t[2], t[0], t[1]),
        lambda t: (t[1], t[2], t[0]),
    ]
    signs = [
        lambda t: (
            t[0] * (-1 or i & (1 << 0)),
            t[1] * (-1 or i & (1 << 1)),
            t[2] * (-1 or i & (1 << 2)),
        )
        for i in range(8)
    ]

    return list(product(rotators, signs))


samples = coord_samples()


def puzzle1() -> None:
    entries = list(filter(bool, DATA.split("\n")))
    scanners = defaultdict(set)
    scanner_id = None
    for line in entries:
        if line.startswith("---"):
            scanner_id = int(scanner_template.fullmatch(line).group(1))
        else:
            assert scanner_id is not None
            beacon = tuple(
                map(
                    int,
                    map(
                        lambda x: 0 if x is None else x,
                        beacon_template.fullmatch(line).groups(),
                    ),
                )
            )
            scanners[scanner_id].add(beacon)

    diffs: Dict[List[Dict[Tuple[int, int, int], int]]] = {}
    for scanner_id, beacons in scanners.items():
        scanner_diffs = []
        for rotator, sign in samples:
            counter = Counter()
            for beacon_1, beacon_2 in combinations(map(rotator, map(sign, beacons)), 2):
                counter.update(
                    [
                        tuple(map(operator.sub, beacon_1, beacon_2)),
                        tuple(map(operator.sub, beacon_2, beacon_1)),
                    ]
                )
            scanner_diffs.append(dict(counter.most_common()))
        diffs[scanner_id] = scanner_diffs

    for scanner_1, scanner_2 in combinations(diffs, 2):
        for diffs_1, diffs_2 in product(diffs[scanner_1], diffs[scanner_2]):
            common_diffs = set(diffs_1) & set(diffs_2)
            common_sum = sum(min(diffs_1[diff], diffs_2[diff]) for diff in common_diffs)
            assert common_sum % 2 == 0
            print(f"{scanner_1}:{scanner_2} -> {common_sum // 2}")
    print(scanners)
    print(diffs)


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
