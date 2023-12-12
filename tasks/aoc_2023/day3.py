from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()


@dataclass
class Point:
    line_index: int
    start: int


@dataclass
class Number(Point):
    # line_index: int
    # start: int
    stop: int
    value: int


def puzzle1() -> None:
    entries: list[str] = list(filter(bool, DATA.split("\n")))
    numbers: list[Number] = []
    symbols: dict[int, list[Point]] = defaultdict(list)
    line_index: int
    line: str
    for line_index, line in enumerate(entries):
        for char_index, char in enumerate(line):
            if char == ".":
                continue
            if char.isdigit():
                if (
                    not numbers
                    or numbers[-1].line_index != line_index
                    or numbers[-1].stop != char_index
                ):
                    numbers.append(
                        Number(
                            line_index=line_index,
                            start=char_index,
                            stop=char_index + 1,
                            value=int(char),
                        )
                    )
                else:
                    numbers[-1].stop += 1
                    numbers[-1].value = numbers[-1].value * 10 + int(char)
                    assert numbers[-1].stop == char_index + 1
            else:
                symbols[line_index].append(
                    Point(
                        line_index=line_index,
                        start=char_index,
                    )
                )

    result = 0
    number: Number
    for number in numbers:
        is_part_number: bool = False
        for line_index in range(max(number.line_index - 1, 0), number.line_index + 2):
            for symbol in symbols[line_index]:
                if number.start - 1 <= symbol.start <= number.stop:
                    is_part_number = True
                    break
            if is_part_number:
                break
        if is_part_number:
            result += number.value

    print(result)


def puzzle2() -> None:
    entries: list[str] = list(filter(bool, DATA.split("\n")))
    numbers: list[Number] = []
    symbols: dict[int, list[Point]] = defaultdict(list)
    line_index: int
    line: str
    for line_index, line in enumerate(entries):
        for char_index, char in enumerate(line):
            if char == ".":
                continue
            if char.isdigit():
                if (
                    not numbers
                    or numbers[-1].line_index != line_index
                    or numbers[-1].stop != char_index
                ):
                    numbers.append(
                        Number(
                            line_index=line_index,
                            start=char_index,
                            stop=char_index + 1,
                            value=int(char),
                        )
                    )
                else:
                    numbers[-1].stop += 1
                    numbers[-1].value = numbers[-1].value * 10 + int(char)
                    assert numbers[-1].stop == char_index + 1
            else:
                symbols[line_index].append(
                    Point(
                        line_index=line_index,
                        start=char_index,
                    )
                )

    result = 0
    number: Number
    for number in numbers:
        is_part_number: bool = False
        for line_index in range(max(number.line_index - 1, 0), number.line_index + 2):
            for symbol in symbols[line_index]:
                if number.start - 1 <= symbol.start <= number.stop:
                    is_part_number = True
                    break
            if is_part_number:
                break
        if is_part_number:
            result += number.value

    print(result)


# pylint: disable=duplicate-code
if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
