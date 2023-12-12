from collections import Counter
from itertools import chain
from operator import itemgetter
from pathlib import Path
from typing import Dict, Iterable

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()


def puzzle1() -> None:
    entries = list(filter(bool, DATA.split("\n")))
    entries = list(map(lambda x: x.split(" | ")[1].split(), entries))

    result = sum(len(value) in {2, 3, 4, 7} for value in chain.from_iterable(entries))

    print(result)


def puzzle2() -> None:
    """
      a
    b   c
      d
    e   f
      g
    """
    entries = list(filter(bool, DATA.split("\n")))
    entries = list(map(lambda x: (x.split(" | ")[0].split(), x.split(" | ")[1].split()), entries))

    def decode(values: Iterable[str]) -> Dict[str, int]:
        result = {
            1: next(filter(lambda x: len(x) == 2, values)),
            7: next(filter(lambda x: len(x) == 3, values)),
            4: next(filter(lambda x: len(x) == 4, values)),
            8: next(filter(lambda x: len(x) == 7, values)),
        }
        counts = Counter(chain.from_iterable(values)).most_common()
        assert list(map(itemgetter(1), counts)) == [9, 8, 8, 7, 7, 6, 4]

        len_5 = list(filter(lambda x: len(x) == 5, values))
        assert len(len_5) == 3
        counts_5 = Counter(chain.from_iterable(len_5)).most_common()

        len_6 = list(filter(lambda x: len(x) == 6, values))
        assert len(len_6) == 3

        result[3] = next(filter(lambda x: sum(k in x for k, v in counts_5 if v == 2) == 2, len_5))
        result[9] = next(filter(lambda x: all(i in x for i in result[3]), len_6))
        len_6.remove(result[9])
        result[0] = next(filter(lambda x: all(i in x for i in result[7]), len_6))
        result[6] = next(filter(lambda x: x not in {result[0], result[9]}, len_6))
        result[5] = next(filter(lambda x: sum(i in result[6] for i in x) == 5, len_5))
        result[2] = next(filter(lambda x: x not in {result[3], result[5]}, len_5))
        assert len(set(result.values())) == 10

        return {"".join(sorted(v)): k for k, v in result.items()}

    total = 0
    for first, second in entries:
        decoder = decode(first)
        total += int("".join(map(str, (decoder["".join(sorted(value))] for value in second))))

    print(f"Result: {total}")


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
