#!/usr/bin/env python

import sys
from importlib import import_module
from pathlib import Path
from typing import Optional

DAY_FORMAT = 'day{}.py'


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
        days = sorted(days)
    else:
        days = ['1']

    return default_year_path / DAY_FORMAT.format(days[-1])


def to_int(value, default: int = None) -> Optional[int]:
    try:
        result = int(value)
    except ValueError:
        result = default

    return result


def main():
    current_path = Path(__file__)
    project_dir = current_path.parent
    tasks_path = project_dir / 'tasks'
    template_path = project_dir / 'tasks' / 'template2.py'

    args = sys.argv[1:]
    if len(args) < 2:
        year = get_default_year_path(tasks_path)
    else:
        year = tasks_path / args[0]

    if len(args) == 0:
        day = get_default_day_path(year)
    elif len(args) == 1:
        day = year / DAY_FORMAT.format(args[0])
    else:
        day = year / DAY_FORMAT.format(args[1])

    data = year / 'data' / (day.stem + '.txt')

    print('year:', year)
    print('day:', day)
    print('data:', data)
    if not data.exists():
        data.touch()

    if not day.exists():
        day.touch()
        day.write_text(template_path.read_text().format(str(data.name)))

    puzzle_module = str(day).replace('.py', '').replace('/', '.')
    module = import_module(puzzle_module)

    if hasattr(module, 'puzzle2'):
        module.puzzle2()
    else:
        module.puzzle1()


if __name__ == '__main__':
    main()
