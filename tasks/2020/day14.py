import re
from enum import unique, Enum, auto
from itertools import product
from pathlib import Path
from typing import Iterable

DATA = (Path(__file__).parent / "data" / "day14.txt").read_text()


@unique
class Cmd(Enum):
    MASK = auto()
    MEM = auto()


mask_pattern = re.compile(r"mask = ([01X]{36})")
mem_pattern = re.compile(r"mem\[(\d+)\] = (\d+)")


def puzzle1():
    entries = [i for i in DATA.split("\n") if i]

    code = []
    for entry in entries:
        cmd, value = entry.split(" = ")
        if cmd.startswith("mask"):
            code.append(
                (
                    Cmd.MASK,
                    (
                        sum(
                            0 if bit == "0" else 2**index
                            for index, bit in enumerate(reversed(value))
                        ),
                        sum(
                            2**index if bit == "1" else 0
                            for index, bit in enumerate(reversed(value))
                        ),
                    ),
                )
            )
        elif cmd.startswith("mem"):
            addr, value = mem_pattern.match(entry).groups()
            code.append(
                (
                    Cmd.MEM,
                    tuple(
                        map(
                            int,
                            (
                                addr,
                                value,
                            ),
                        )
                    ),
                )
            )
        else:
            raise RuntimeError("unparsed entry: {}".format(entry))

    and_, or_ = None, None
    memory = {}
    for op, args in code:
        if op == Cmd.MASK:
            and_, or_ = args
        elif op == Cmd.MEM:
            addr, value = args
            memory[addr] = value & and_ | or_

    print(sum(memory.values()))


def puzzle2():
    entries = [i for i in DATA.split("\n") if i]

    def replace_multiple(source, old: str, new: Iterable[str]):
        source = source.replace("0", ".").replace(
            "1", "-"
        )  # this needs for correct submasks
        for n in new:
            source = source.replace(old, n, 1)
        return source

    code = []
    for entry in entries:
        cmd, value = entry.split(" = ")
        if cmd.startswith("mask"):
            code.append(
                (
                    Cmd.MASK,
                    (
                        (
                            sum(
                                0 if bit == "X" else 2**index
                                for index, bit in enumerate(reversed(value))
                            ),
                            sum(
                                2**index if bit == "1" else 0
                                for index, bit in enumerate(reversed(value))
                            ),
                        ),
                        [
                            (
                                sum(
                                    0 if bit == "0" else 2**index
                                    for index, bit in enumerate(
                                        reversed(replace_multiple(value, "X", seq))
                                    )
                                ),
                                sum(
                                    2**index if bit == "1" else 0
                                    for index, bit in enumerate(
                                        reversed(replace_multiple(value, "X", seq))
                                    )
                                ),
                            )
                            for seq in product("01", repeat=value.count("X"))
                        ],
                    ),
                )
            )
        elif cmd.startswith("mem"):
            addr, value = mem_pattern.match(entry).groups()
            code.append(
                (
                    Cmd.MEM,
                    tuple(
                        map(
                            int,
                            (
                                addr,
                                value,
                            ),
                        )
                    ),
                )
            )
        else:
            raise RuntimeError("unparsed entry: {}".format(entry))

    def print_it(val):
        return "".join(
            reversed(list(map(str, (int(bool((2**i) & val)) for i in range(36)))))
        )

    and_, or_, pairs = None, None, None
    memory = {}
    for op, args in code:
        if op == Cmd.MASK:
            (and_, or_), pairs = args
        elif op == Cmd.MEM:
            addr, value = args
            addr = addr & and_ | or_
            for the_and, the_or in pairs:
                one_addr = addr & the_and | the_or
                memory[one_addr] = value

    print(sum(memory.values()))


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
