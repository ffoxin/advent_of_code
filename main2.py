#!/usr/bin/env python

import sys
from importlib import import_module
from pathlib import Path
from typing import Optional, Tuple

DAY_FORMAT = 'day{}.py'
PUZZLE_FORMAT = 'puzzle{}'


def get_default_year_path(tasks_path: Path) -> Path:
    years = [
        item.name
        for item in tasks_path.iterdir()
        if item.is_dir() and item.name.isdigit()
    ]
    last_year = sorted(years)[-1]

    return tasks_path / last_year


def get_default_day_path(default_year_path: Path) -> Path:
    days = [
        item.name[3:-3]
        for item in default_year_path.iterdir()
        if item.is_file() and item.name.startswith('day') and item.name.endswith('.py')
    ]
    if days:
        days = sorted(days, key=int)
    else:
        days = ['1']

    return default_year_path / DAY_FORMAT.format(days[-1])


def to_int(value, default: int = None) -> Optional[int]:
    try:
        result = int(value)
    except ValueError:
        result = default

    return result


def parse_day(value: str) -> Tuple[Optional[int], Optional[int]]:
    if '.' in value:
        day, puzzle = value.split('.')
        day = int(day) if day else None
        puzzle = int(puzzle) or None
    else:
        day = int(value)
        puzzle = None

    return day, puzzle


def main():
    current_path = Path(__file__)
    project_dir = current_path.parent
    tasks_path = project_dir / 'tasks'
    template_path = project_dir / 'tasks' / 'template2.py'

    args = sys.argv[1:]
    year = None
    day = None
    puzzle = None

    for arg in args:
        if arg.isdigit():
            if int(arg) > 1000:
                year = arg
                continue
            else:
                day = arg
        else:
            day, puzzle = parse_day(arg)

    if year is None:
        year_path = get_default_year_path(tasks_path)
    else:
        year_path = tasks_path / year

    if day is None:
        day_path = get_default_day_path(year_path)
    else:
        day_path = year_path / DAY_FORMAT.format(day)

    data = year_path / 'data' / (day_path.stem + '.txt')

    if not data.exists():
        data.touch()

    if not day_path.exists():
        day_path.touch()
        day_path.write_text(template_path.read_text().format(str(data.name)))

    puzzle_module = str(day_path).replace('.py', '').replace('/', '.')
    module = import_module(puzzle_module)

    if puzzle:
        puzzle_id = puzzle
    else:
        puzzle_id = 2 if hasattr(module, PUZZLE_FORMAT.format(2)) else 1
    puzzle_name = PUZZLE_FORMAT.format(puzzle_id)

    print('year:', year_path)
    print('day:', day_path)
    print('puzzle:', puzzle_name)
    print('data:', data)

    getattr(module, puzzle_name)()


if __name__ == '__main__':
    main()
