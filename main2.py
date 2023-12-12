#!/usr/bin/env python

from importlib import import_module
from pathlib import Path
from typing import Optional, Tuple

import click

DAY_FORMAT = "day{}.py"
PUZZLE_FORMAT = "puzzle{}"


def get_default_year_path(tasks_path: Path) -> Path:
    years = [
        item.name for item in tasks_path.iterdir() if item.is_dir() and item.name.startswith("aoc_")
    ]
    last_year = sorted(years)[-1]

    return tasks_path / last_year


def get_default_day_path(default_year_path: Path) -> Path:
    days = [
        item.name[3:-3]
        for item in default_year_path.iterdir()
        if item.is_file() and item.name.startswith("day") and item.name.endswith(".py")
    ]
    if days:
        days = sorted(days, key=int)
    else:
        days = ["1"]

    return default_year_path / DAY_FORMAT.format(days[-1])


def parse_day(value: str) -> Tuple[Optional[int], Optional[int]]:
    day: Optional[int]
    puzzle: Optional[int]

    if "." in value:
        day_str, puzzle_str = value.split(".")
        day = int(day_str) if day_str else None
        puzzle = int(puzzle_str) or None
    else:
        day = int(value)
        puzzle = None

    return day, puzzle


@click.command()
@click.argument("day", type=click.IntRange(min=1, max=25), required=False)
@click.argument("year", type=click.IntRange(min=2015, max=2021), required=False)
def main(day: int, year: int):
    current_path = Path(__file__)
    project_dir = current_path.parent
    tasks_path = project_dir / "tasks"
    template_path = project_dir / "tasks" / "template2.py"

    puzzle = None

    if year is None:
        year_path = get_default_year_path(tasks_path)
    else:
        year_path = tasks_path / f"aoc_{year}"

    if day is None:
        day_path = get_default_day_path(year_path)
    else:
        day_path = year_path / DAY_FORMAT.format(day)

    data_path = year_path / "data" / (day_path.stem + ".txt")

    if not data_path.exists():
        data_path.touch()

    if not day_path.exists():
        day_path.touch()
        day_path.write_text(template_path.read_text().format(str(data_path.name)))

    day_path_relative = str(day_path)[len(str(project_dir)) + 1 :]
    puzzle_module = day_path_relative.replace(".py", "").replace("/", ".")
    click.secho(f'{"Module: ":<10s}{puzzle_module}', fg="bright_black")
    module = import_module(puzzle_module)

    if puzzle:
        puzzle_id = puzzle
    else:
        puzzle_id = 2 if hasattr(module, PUZZLE_FORMAT.format(2)) else 1
    puzzle_name = PUZZLE_FORMAT.format(puzzle_id)

    click.secho(
        f'{"Data: ":<10s}{data_path.relative_to(current_path.parent)}',
        fg="bright_black",
    )
    click.secho(f'{"Puzzle: ":<10s}{puzzle_name}', fg="green")

    getattr(module, puzzle_name)()


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
