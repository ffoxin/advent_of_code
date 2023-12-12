from pathlib import Path
from typing import Union, Tuple

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()


class Pair:
    def __init__(
        self, l_value: Union[int, "Pair"], r_value: Union[int, "Pair"], depth: int
    ) -> None:
        self.l_value = l_value
        self.r_value = r_value
        self.depth = depth
        self.parent = None

        self._update_parent()
        self._update_depth(depth)

    @staticmethod
    def make_expected(data: str, expected: str, offset: int) -> str:
        return f'Expected "{expected}", found "{data[max(offset - 9, 0):offset]}_{data[offset]}_{data[min(len(data), offset + 1):min(len(data), offset + 10)]}"'

    @classmethod
    def parse_part(cls, data: str, offset: int, depth: int) -> Tuple[Union["Pair", int], int]:
        if data[offset] == "[":
            value, offset = cls.parse_pair(data, offset, depth + 1)
        elif data[offset].isdigit():
            begin = offset
            while data[offset].isdigit():
                offset += 1
            value = int(data[begin:offset])
        else:
            raise RuntimeError(cls.make_expected(data, "<unexpected>", offset))

        return value, offset

    @classmethod
    def parse_pair(cls, data: str, offset: int, depth: int) -> Tuple["Pair", int]:
        assert data[offset] == "[", cls.make_expected(data, "[", offset)

        l_value, offset = cls.parse_part(data, offset + 1, depth)

        assert data[offset] == ",", cls.make_expected(data, ",", offset)

        r_value, offset = cls.parse_part(data, offset + 1, depth)

        assert data[offset] == "]", cls.make_expected(data, "]", offset)

        return Pair(l_value, r_value, depth), offset + 1

    def _update_depth(self, depth: int) -> None:
        self.depth = depth
        if isinstance(self.l_value, Pair):
            self.l_value._update_depth(depth + 1)
        if isinstance(self.r_value, Pair):
            self.r_value._update_depth(depth + 1)

    def _update_parent(self) -> None:
        if isinstance(self.l_value, Pair):
            self.l_value.parent = self
        if isinstance(self.r_value, Pair):
            self.r_value.parent = self

    def reduce(self) -> None:
        if self.depth == 4:
            self.explode()
            return

        if isinstance(self.l_value, Pair):
            self.l_value.reduce()
        if isinstance(self.r_value, Pair):
            self.r_value.reduce()

    def explode(self):
        assert self.depth == 4

        target = self
        if target.parent.l_value == target:
            while target.parent and target.parent.l_value == target:
                target = target.parent
            target = target.parent.l_value
            while isinstance(target, Pair):
                target = target.r_value
            print(f"left explosion: {target}")

        # target = self
        # prev_target = None
        # while target.parent and target.parent.l_value == target:
        #     print(f'target parent: {repr(target.parent)}')
        #     prev_target = target
        #     target = target.parent
        # if prev_target == target.l_value:
        #     print(f'Unable to find left neib')
        #     return
        # target = target.l_value
        # while isinstance(target, Pair):
        #     target = target.r_value
        # print(f'left explosion: {target}')

    def __add__(self, other: "Pair") -> "Pair":
        return Pair(self, other, 0)

    def __repr__(self):
        return f"[{{{self.depth}}}{repr(self.l_value)},{repr(self.r_value)}]"

    def __str__(self):
        return f"[{str(self.l_value)},{str(self.r_value)}]"


NodeOrNumber = Union[int, "Node"]


class Node:
    def __init__(
        self,
        left: NodeOrNumber = None,
        right: NodeOrNumber = None,
        parent: "Node" = None,
    ):
        self.left = None
        self.right = None
        self.parent = None


class Tree:
    def __init__(self, root: Node):
        self.root = root

    @classmethod
    def parse_node(cls, line: str, start) -> Tuple[int, NodeOrNumber]:
        if line[start] == "[":
            end, node = cls.parse_node(line, start + 1)
        else:
            end = line.find(",", start)
            node = int(line[start:end])

        return end + 1, node

    @classmethod
    def parse_line(cls, line: str, start=0) -> Tuple[int, NodeOrNumber]:
        while start < len(line):
            char = line[start]
            if char == "[":
                start, left = cls.parse_node(line, start)
                assert line[start] == ","
                start, right = cls.parse_node(line, start)
                return start + 1, Node(left, right)
            else:
                raise RuntimeError(f"Unexpected: {line[start]}, {line[start - 5:start + 6]}")

                # index, left, right = cls.parse(line, index + 1)
                # if node is None:
                #     node = Node(left, right)
                # char = line[index]
                # if char == ']':
                #     return


def puzzle1() -> None:
    entries = list(filter(bool, DATA.split("\n")))
    pairs = [Pair.parse_pair(line, offset=0, depth=0)[0] for line in entries]
    for pair in pairs:
        print(repr(pair))

    total = sum(pairs[1:], pairs[0])
    print(repr(total))
    print(total)
    total.reduce()
    # for pair in pairs[1:]:
    #     total += pairs

    # pairs = [Pair.parse_pair(line, offset=0, depth=0) for line in entries]
    # for pair in pairs:
    #     print(repr(pair))


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
