import operator
import re
from collections import defaultdict
from enum import unique, StrEnum, auto
from functools import reduce
from pathlib import Path

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()


@unique
class Colors(StrEnum):
    red = auto()
    green = auto()
    blue = auto()


GAME_ID_TEMPLATE = re.compile(r"Game (\d+)")
CUBES_COLOR_TEMPLATE = re.compile(r"(\d+) ([a-z]+)(?:, )?")


def puzzle1():
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
        game_id: int = int(GAME_ID_TEMPLATE.fullmatch(game).group(1))
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


def puzzle2():
    entries: list[str] = list(filter(bool, DATA.split("\n")))
    # max_cubes: dict[Colors, int] = {
    #     Colors.red: 12,
    #     Colors.green: 13,
    #     Colors.blue: 14,
    # }
    result = 0
    for line in entries:
        game: str
        sets: str
        game, sets = line.split(": ")
        # game_id: int = int(GAME_ID_TEMPLATE.fullmatch(game).group(1))
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


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
