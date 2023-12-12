from dataclasses import dataclass
from pathlib import Path
from typing import List

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()

open_token = set("([{<")
close_token = set(")]}>")
chunk_map = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}
error_weight = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
completion_weight = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


@dataclass
class Result:
    is_valid: bool
    weight: int


def calculate_completion(stack: List[str]) -> int:
    result = 0
    for char in reversed(stack):
        result = result * 5 + completion_weight[chunk_map[char]]

    return result


def check_line(line) -> Result:
    stack = []
    for char in line:
        if char in open_token:
            stack.append(char)
        elif char in close_token:
            expected = chunk_map[stack[-1]]
            if char == expected:
                stack.pop(-1)
            else:
                return Result(
                    False,
                    error_weight[char],
                )

    return Result(
        True,
        calculate_completion(stack),
    )


def puzzle1() -> None:
    entries = list(filter(bool, DATA.split("\n")))

    result = sum(map(lambda x: x.weight if not x.is_valid else 0, map(check_line, entries)))
    print(f"Result: {result}")


def puzzle2() -> None:
    entries = list(filter(bool, DATA.split("\n")))

    scores = sorted(
        filter(bool, map(lambda x: x.weight if x.is_valid else 0, map(check_line, entries)))
    )
    result = scores[len(scores) // 2]

    print(f"Result: {result}")


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
