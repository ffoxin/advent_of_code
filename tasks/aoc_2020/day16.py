from pathlib import Path

DATA = (Path(__file__).parent / "data" / "day16.txt").read_text()


def puzzle1() -> None:
    entries = [i for i in DATA.split("\n") if i]

    rules = [
        tuple(tuple(map(int, pair.split("-"))) for pair in entry.split(": ")[1].split(" or "))
        for entry in entries[: entries.index("your ticket:")]
    ]
    nearby = [
        tuple(map(int, entry.split(",")))
        for entry in entries[entries.index("nearby tickets:") + 1 :]
    ]

    invalid_sum = 0
    for ticket in nearby:
        for value in ticket:
            for (rule1_from, rule1_to), (rule2_from, rule2_to) in rules:
                if rule1_from <= value <= rule1_to or rule2_from <= value <= rule2_to:
                    break
            else:
                invalid_sum += value

    print(invalid_sum)


def puzzle2() -> None:
    entries = [i for i in DATA.split("\n") if i]

    class Rule:
        def __init__(self, line):
            self.name, rest = line.split(": ")
            self.ranges = tuple(tuple(map(int, pair.split("-"))) for pair in rest.split(" or "))

        def is_valid(self, val):
            (rule1_from, rule1_to), (rule2_from, rule2_to) = self.ranges
            return rule1_from <= val <= rule1_to or rule2_from <= val <= rule2_to

    rules = {
        rule.name: rule
        for rule in [Rule(entry) for entry in entries[: entries.index("your ticket:")]]
    }

    my_ticket = tuple(map(int, entries[entries.index("your ticket:") + 1].split(",")))
    nearby = [
        tuple(map(int, entry.split(",")))
        for entry in entries[entries.index("nearby tickets:") + 1 :]
    ]

    allowed_fields = [
        set([name for name, rule in rules.items() if rule.is_valid(field)]) for field in my_ticket
    ]

    validated_tickets = []
    for ticket in nearby:
        is_valid = True
        for value in ticket:
            for rule in rules.values():
                if rule.is_valid(value):
                    break
            else:
                is_valid = False
                break
        if is_valid:
            validated_tickets.append(ticket)

    for ticket in validated_tickets:
        for index, value in enumerate(ticket):
            for name, rule in rules.items():
                if name in allowed_fields[index] and not rule.is_valid(value):
                    allowed_fields[index].remove(name)

    while True:
        changed = False
        for index, s in enumerate(allowed_fields):
            if len(s) == 1:
                item = list(s)[0]
                for i in range(len(allowed_fields)):
                    if i == index:
                        continue
                    if item in allowed_fields[i]:
                        allowed_fields[i].remove(item)
                        changed = True
        if not changed:
            break

    result = 1
    for index, s in enumerate(allowed_fields):
        item = list(s)[0]
        if not item.startswith("departure"):
            continue
        result *= my_ticket[index]

    print(result)
    # for s in allowed_fields:
    #     print(len(s), s)


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
