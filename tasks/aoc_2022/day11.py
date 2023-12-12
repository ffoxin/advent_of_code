import operator
import re
from functools import reduce
from pathlib import Path
from typing import List

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()


class Monkey:
    name_pattern = re.compile(r"^Monkey (\d+):$")
    operation_pattern = re.compile(r"^ {2}Operation: new = (old|\d+) ([+*]) (old|\d+)$")
    test_pattern = re.compile(r"^ {2}Test: divisible by (\d+)$")
    true_pattern = re.compile(r"^ {4}If true: throw to monkey (\d+)$")
    false_pattern = re.compile(r"^ {4}If false: throw to monkey (\d+)$")

    ops = {
        "+": operator.add,
        "*": operator.mul,
    }

    def __init__(self, name_line: str):
        self.monkey_id = int(self.name_pattern.fullmatch(name_line).group(1))
        self.starting_items = []
        self.operation = None
        self.test_divider = None
        self.test = None
        self.test_str = None
        self.target_true = None
        self.target_false = None
        self.inspected = 0

    def add_starting_items(self, starting_items_line: str):
        self.starting_items = list(map(int, starting_items_line.split(": ")[-1].split(", ")))

    def add_operation(self, operation_line: str):
        value1, op, value2 = self.operation_pattern.fullmatch(operation_line).groups()
        assert op in self.ops, op
        op_value = self.ops[op]
        if value1 == "old" and value2 == "old":
            self.operation = lambda old: op_value(old, old)
        elif value1 == "old":
            value2 = int(value2)
            self.operation = lambda old: op_value(old, value2)
        elif value2 == "old":
            value1 = int(value1)
            self.operation = lambda old: op_value(value1, old)
        else:
            assert False, "Really? Both constants?"

    def add_test(self, test_line: str):
        divider = int(self.test_pattern.fullmatch(test_line).groups()[0])
        self.test = lambda old: (old % divider) == 0
        test_str = f"({{old}} % {divider}) == {{result}}"
        self.test_str = lambda old: test_str.format(old=old, result=old % divider)
        self.test_divider = divider

    def add_true(self, true_line: str):
        self.target_true = int(self.true_pattern.fullmatch(true_line).groups()[0])

    def add_false(self, false_line: str):
        self.target_false = int(self.false_pattern.fullmatch(false_line).groups()[0])


def read_monkeys() -> List[Monkey]:
    entries = list(filter(bool, DATA.split("\n")))

    line_iter = iter(entries)
    monkeys = []
    while True:
        try:
            line = next(line_iter)
        except StopIteration:
            break

        if line.startswith("Monkey"):
            monkeys.append(Monkey(line))
        elif line.startswith("  Starting"):
            monkeys[-1].add_starting_items(line)
        elif line.startswith("  Operation"):
            monkeys[-1].add_operation(line)
        elif line.startswith("  Test"):
            monkeys[-1].add_test(line)
        elif line.startswith("    If true"):
            monkeys[-1].add_true(line)
        elif line.startswith("    If false"):
            monkeys[-1].add_false(line)
        else:
            raise RuntimeError(f"Unexpected line: {line}")

    return monkeys


def puzzle1() -> None:
    monkeys = read_monkeys()

    for _ in range(20):
        for monkey in monkeys:
            # print(f'Monkey {monkey.monkey_id}:')
            starting_items = monkey.starting_items
            monkey.starting_items = []
            for item in starting_items:
                # print(f'  Monkey inspects an item with a worry level of {item}.')
                worry_level = monkey.operation(item)
                # print(f'    Worry level ... to {worry_level}.')
                decreased_level = worry_level // 3
                # print(f'    Monkey gets bored with item. Worry level is divided by 3 to {decreased_level}.')
                test_value = monkey.test(decreased_level)
                # print(f'    Current worry level is {"" if test_value else "not"} divisible {monkey.test_str(decreased_level)}')
                target = monkey.target_true if test_value else monkey.target_false
                # print(f'    Item with worry level {decreased_level} is thrown to monkey {target}.')
                monkeys[target].starting_items.append(decreased_level)
                monkey.inspected += 1

        # print(f'After round {step + 1}, the monkeys are holding items with these worry levels:')
        # for monkey in monkeys:
        #     print(f'Monkey {monkey.monkey_id}: {", ".join(map(str, monkey.starting_items))}')

    # for monkey in monkeys:
    #     print(f'Monkey {monkey.monkey_id} inspected items {monkey.inspected} times')

    result = operator.mul(*(list(sorted(monkey.inspected for monkey in monkeys))[-2:]))
    print(result)


def puzzle2() -> None:
    monkeys = read_monkeys()

    common_divider = reduce(operator.mul, [monkey.test_divider for monkey in monkeys], 1)

    for _ in range(10000):
        for monkey in monkeys:
            starting_items = monkey.starting_items
            monkey.starting_items = []
            for item in starting_items:
                worry_level = monkey.operation(item)
                test_value = worry_level % monkey.test_divider
                target = monkey.target_true if test_value == 0 else monkey.target_false
                monkeys[target].starting_items.append(worry_level % common_divider)
                monkey.inspected += 1

        # if (step + 1) in {1, 20} or (step + 1) % 1000 == 0:
        #     print(f'== After round {step + 1} ==')
        #     for monkey in monkeys:
        #         print(f'Monkey {monkey.monkey_id} inspected items {monkey.inspected} times')

    result = operator.mul(*(list(sorted(monkey.inspected for monkey in monkeys))[-2:]))
    print(result)


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
