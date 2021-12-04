import re
from collections import defaultdict
from pathlib import Path

DATA = (Path(__file__).parent / "data" / "day7.txt").read_text()

"""
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

# pattern_1 = re.compile(r'(\w+ \w+) bags contain (?:(?:(\d+ \w+ \w+) bags?(?:, )?){1,}|no other bags)\.')
pattern_1 = re.compile(r"(\w+ \w+) bags contain ([^.]+)\.")
pattern_2 = re.compile(r"\d+ (\w+ \w+) bags?")
pattern_3 = re.compile(r"(\d+ \w+ \w+) bags?")


def puzzle1():
    entries = [i for i in DATA.split("\n") if i]

    bags = {}
    for entry in entries:
        bag, inner = pattern_1.match(entry).groups()
        if inner == "no other bags":
            content = set()
        else:
            content = set([pattern_2.match(i).group(1) for i in inner.split(", ")])

        bags[bag] = content

    my_bag = "shiny gold"
    parents = {my_bag}
    while True:
        updated = False
        for bag, content in bags.items():
            if bag not in parents and parents.intersection(content):
                parents.add(bag)
                updated = True

        if not updated:
            break

    print(len(parents) - 1)


def puzzle2():
    entries = [i for i in DATA.split("\n") if i]

    bags = {}
    for entry in entries:
        bag, inner = pattern_1.match(entry).groups()
        if inner == "no other bags":
            content = {}
        else:
            content = {
                item[1]: int(item[0])
                for item in [
                    pattern_3.match(i).group(1).split(" ", maxsplit=1)
                    for i in inner.split(", ")
                ]
            }

        bags[bag] = content

    my_bag = "shiny gold"
    children = {my_bag: 1}
    count = 0
    while True:
        updated = False
        new_children = defaultdict(int)
        for name, amount in children.items():
            if bags[name]:
                for sub_name, sub_amount in bags[name].items():
                    new_children[sub_name] += amount * sub_amount
                updated = True

        if not updated:
            break
        children = dict(new_children)
        count += sum(children.values())

    print(count)


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
