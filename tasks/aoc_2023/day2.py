import operator
import re
from collections import defaultdict
from enum import unique, StrEnum, auto
from functools import reduce
from pathlib import Path

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()


# pylint: disable=invalid-name
@unique
class Colors(StrEnum):
    red = auto()
    green = auto()
    blue = auto()


GAME_ID_TEMPLATE = re.compile(r"Game (\d+)")
CUBES_COLOR_TEMPLATE = re.compile(r"(\d+) ([a-z]+)(?:, )?")


def puzzle1() -> None:
    entries: list[str] = list(filter(bool, DATA.split("\n")))
    max_cubes: dict[Colors, int] = {
        Colors.red: 12,
        Colors.green: 13,
        Colors.blue: 14,
    }
    result = 0
    for line in entries:
        game: str
        sets: str
        game, sets = line.split(": ")
        match = GAME_ID_TEMPLATE.fullmatch(game)
        assert match is not None
        game_id: int = int(match.group(1))
        steps: list[str] = sets.split("; ")
        is_valid: bool = True
        step: str
        for step in steps:
            cubes: list[tuple[str, str]] = CUBES_COLOR_TEMPLATE.findall(step)
            for count, color in cubes:
                cube_count: int = int(count)
                cube_color: Colors = Colors(color)
                if max_cubes[cube_color] < cube_count:
                    is_valid = False
                    break
            if not is_valid:
                break
        if is_valid:
            result += game_id

    print(result)


def puzzle2() -> None:
    entries: list[str] = list(filter(bool, DATA.split("\n")))
    result = 0
    for line in entries:
        sets: str
        _, sets = line.split(": ")
        steps: list[str] = sets.split("; ")
        step: str
        min_cubes: dict[Colors, int] = defaultdict(int)
        for step in steps:
            cubes: list[tuple[str, str]] = CUBES_COLOR_TEMPLATE.findall(step)
            for count, color in cubes:
                cube_count: int = int(count)
                cube_color: Colors = Colors(color)
                if min_cubes[cube_color] < cube_count:
                    min_cubes[cube_color] = cube_count
        result += reduce(operator.mul, min_cubes.values(), 1)

    print(result)


# pylint: disable=duplicate-code
if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
