import os
from importlib import import_module

YEAR = '2017'


def data_path(day_py):
    day_path, day = os.path.split(day_py)
    return os.path.join(day_path, 'data', os.path.splitext(day)[0] + '.txt')


def main():
    # get days path
    days_path = os.path.join(os.path.curdir, 'tasks', YEAR)
    # get solutions
    days = [i for i in os.listdir(days_path) if i.startswith('day') and os.path.splitext(i)[1] == '.py']
    # find last day
    days = sorted(days, key=lambda x: int(x[3:-3]))
    last_day = os.path.splitext(days[-1])[0]
    # create module path
    puzzle_module = f'tasks.{YEAR}.{last_day}'
    module = import_module(puzzle_module)

    if hasattr(module, 'puzzle2'):
        module.puzzle2()
    else:
        module.puzzle1()


if __name__ == '__main__':
    main()
