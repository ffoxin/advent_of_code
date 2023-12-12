from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()


def puzzle1() -> None:
    entries = list(filter(bool, DATA.split("\n")))
    polymer: str = entries[0]
    pairs: Dict[str, str] = dict(map(lambda x: x.split(" -> "), entries[1:]))

    def process(template: str, insertions: Dict[str, str]) -> str:
        new_template = []
        for i in range(len(template) - 1):
            new_template.extend([template[i], insertions[template[i : i + 2]]])
        new_template.append(template[-1])
        return "".join(new_template)

    for _ in range(10):
        polymer = process(polymer, pairs)
    counter = Counter(polymer).most_common()
    print(f"Result: {counter[0][1] - counter[-1][1]}")


def puzzle2() -> None:
    entries = list(filter(bool, DATA.split("\n")))
    template: str = entries[0]
    pairs: Dict[str, str] = dict(map(lambda x: x.split(" -> "), entries[1:]))

    first, last = None, None
    polymer: Dict[str, int] = defaultdict(int)
    for i in range(len(template) - 1):
        if i == 0:
            first = template[i : i + 2]
        elif i == len(template) - 2:
            last = template[i : i + 2]
        polymer[template[i : i + 2]] += 1

    def process():
        first_local, last_local = None, None
        new_polymer = defaultdict(int)
        for pair, count in polymer.items():
            if pair == first:
                first_local = pair[0] + pairs[pair]
            elif pair == last:
                last_local = pairs[pair] + pair[1]
            new_polymer[pair[0] + pairs[pair]] += count
            new_polymer[pairs[pair] + pair[1]] += count
        return new_polymer, first_local, last_local

    for i in range(40):
        polymer, first, last = process()

    counter = Counter()
    counter[first[0]] += 1
    counter[last[1]] += 1
    for pair, count in polymer.items():
        counter[pair[0]] += count
        counter[pair[1]] += count
    counter = counter.most_common()
    print(f"Result: {(counter[0][1] - counter[-1][1]) // 2}")


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
