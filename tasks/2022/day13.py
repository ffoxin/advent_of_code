import enum
from itertools import zip_longest
from pathlib import Path
from typing import Iterator, Generator

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()


def parse_item(line_iter: Iterator[str]) -> Generator:
    while True:
        try:
            ch = next(line_iter)
        except StopIteration:
            break

        if ch == "[":
            items = list(parse_item(line_iter))
            yield items
        elif ch == "]":
            break
        elif ch == ",":
            continue
        else:
            token_parts = [ch]
            while True:
                try:
                    ch = next(line_iter)
                except StopIteration:
                    break
                if ch in {",", "]"}:
                    break
                token_parts.append(ch)
            token = "".join(token_parts)
            assert token.isdigit(), token
            yield int(token)
            if ch == "]":
                break


@enum.unique
class Result(enum.Enum):
    right_order = enum.auto()
    equal = enum.auto()
    not_right_order = enum.auto()


def compare_items(left, right) -> Result:
    if isinstance(left, int) and isinstance(right, int):
        print(f"{left} vs {right} ? ", end="")
        if left < right:
            result = Result.right_order
        elif left > right:
            result = Result.not_right_order
        else:
            assert left == right
            result = Result.equal
        print(result)
        return result

    print(f"{left} <= {right} ?")
    if isinstance(left, list) and isinstance(right, list):
        for left_item, right_item in zip_longest(left, right):
            if left_item is None or right_item is None:
                break
            result = compare_items(left_item, right_item)
            if result == Result.equal:
                continue
            return result
        return compare_items(len(left), len(right))
    if isinstance(left, int):
        assert isinstance(right, list)
        return compare_items([left], right)
    if isinstance(right, int):
        assert isinstance(left, list)
        return compare_items(left, [right])

    raise RuntimeError(f"Unexpected comparison: {left} <> {right}")


class Packet:
    def __init__(self, parsed_packet):
        self.packet = parsed_packet

    def __lt__(self, other):
        return compare_items(self.packet, other.packet) == Result.right_order

    def __eq__(self, other):
        return compare_items(self.packet, other.packet) == Result.equal

    def __repr__(self):
        return str(self.packet).replace(" ", "")


def puzzle1():
    entries = list(filter(bool, DATA.split("\n")))
    pairs = list(map(tuple, zip(entries[::2], entries[1::2])))
    results = []
    for index, pair in enumerate(pairs):
        parsed_left = next(parse_item(iter(pair[0])))
        left = str(parsed_left).replace(" ", "")
        parsed_right = next(parse_item(iter(pair[1])))
        right = str(parsed_right).replace(" ", "")
        assert pair[0] == left, f"\n{pair[0]}\n{left}"
        assert pair[1] == right, (pair[1], right)

        print(f"== Pair {index + 1} ==")
        print(f"- Compare {left} vs {right}")
        result = compare_items(parsed_left, parsed_right)
        if result == Result.right_order:
            results.append(index + 1)

    print(sum(results))


def puzzle2():
    entries = list(filter(bool, DATA.split("\n")))
    pairs = list(map(tuple, zip(entries[::2], entries[1::2])))
    packets = []
    for index, pair in enumerate(pairs):
        parsed_left = next(parse_item(iter(pair[0])))
        left = str(parsed_left).replace(" ", "")
        parsed_right = next(parse_item(iter(pair[1])))
        right = str(parsed_right).replace(" ", "")
        assert pair[0] == left, f"\n{pair[0]}\n{left}"
        assert pair[1] == right, (pair[1], right)
        packets.extend((Packet(parsed_left), Packet(parsed_right)))

    p2 = Packet([[2]])
    p6 = Packet([[6]])
    packets.extend((p2, p6))
    sorted_packets = sorted(packets)

    indexes = [
        index
        for index, packet in enumerate(sorted_packets, start=1)
        if packet in (p2, p6)
    ]
    assert len(indexes) == 2
    result = indexes[0] * indexes[1]

    print(result)


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
