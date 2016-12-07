import os
from importlib import import_module


def main():
    for item in sorted(os.listdir('tasks/2015')):
        if item.startswith('day') and not item.startswith('day4') and not item.startswith('day6'):
            module, _ = os.path.splitext(item)
            module_name = 'tasks.2015.{}'.format(module)
            module = import_module(module_name)

            module.puzzle1()
            module.puzzle2()


if __name__ == '__main__':
    main()
