import os
import sys
from datetime import datetime
from importlib import import_module


def data_path(day_py):
    day_path, day = os.path.split(day_py)
    return os.path.join(day_path, 'data', day.replace('.py', '.txt'))


def run(year):
    # get days path
    days_path = os.path.join(os.path.curdir, 'tasks', year)
    # get solutions
    days = {
        int(filename[3:-3]): filename[:-3]
        for filename in os.listdir(days_path)
        if filename.startswith('day') and filename.endswith('.py')
    }
    # days = [i for i in os.listdir(days_path) if i.startswith('day') and os.path.splitext(i)[1] == '.py']
    # find last day
    last_day = days[sorted(days.keys())[-1]]
    # create module path
    puzzle_module = 'tasks.{}.{}'.format(year, last_day)
    module = import_module(puzzle_module)

    if hasattr(module, 'puzzle2'):
        module.puzzle2()
    else:
        module.puzzle1()


def main():
    if len(sys.argv) > 1:
        year = sys.argv[1]
    else:
        year = str(datetime.utcnow().year)

    run(year)


if __name__ == '__main__':
    main()
