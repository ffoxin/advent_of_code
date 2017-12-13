from main import data_path

DATA = data_path(__file__)


class Program:
    def __init__(self, name, weight, nested=None):
        self.name = name
        self.weight = int(weight[1:-1])
        self.nested = nested or []


def puzzle1():
    with open(DATA, 'r') as f:
        lines = f.readlines()

    programs = set()
    nested = set()

    for line in lines:
        items = line.strip().split(' -> ')
        if len(items) == 1:
            program = Program(*items[0].split())
        else:
            program = Program(*items[0].split(), items[1].split(', '))

        programs.add(program.name)
        nested.update(program.nested)

    print(list(programs - nested))


def puzzle2():
    with open(DATA, 'r') as f:
        lines = f.readlines()

    programs = {}
    names = set()
    nested = set()

    for line in lines:
        items = line.strip().split(' -> ')
        if len(items) == 1:
            program = Program(*items[0].split())
        else:
            program = Program(*items[0].split(), items[1].split(', '))

        programs[program.name] = program
        names.add(program.name)
        nested.update(program.nested)

    root = list(names - nested)[0]

    def tree_sum(name):
        this = programs[name]
        this_sum = this.weight
        if this.nested:
            this_sum += sum(map(tree_sum, this.nested))
        return this_sum

    def check_tree(name):
        this = programs[name]
        if not this.nested:
            return this.weight

        nested_sums = {name: check_tree(name) for name in this.nested}
        nested_values = list(nested_sums.values())

        for name, nsum in nested_sums.items():
            if not isinstance(nsum, int):
                return nsum

        if any(value != nested_values[0] for value in nested_values):
            return {name: (nested_sums[name], programs[name].weight) for name in this.nested}

        return this.weight + sum(nested_values)

    result = check_tree(root)
    print(result)
