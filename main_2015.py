import os
from importlib import import_module


def main():
    for item in sorted(os.listdir('tasks/2015'),
                       key=lambda name: int(name[3:name.index('.')]) if name[:3] == 'day' else 0):
        module, _ = os.path.splitext(item)
        if module.startswith('day') and module not in ['day4', 'day6', 'day9', 'day10', 'day11']:
            module_name = 'tasks.2015.{}'.format(module)
            module = import_module(module_name)

            module.puzzle1()
            module.puzzle2()


if __name__ == '__main__':
    main()
