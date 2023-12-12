import re
from operator import itemgetter
from pathlib import Path

DATA = (Path(__file__).parent / "data" / "day19.txt").read_text()

raw_value = re.compile('"([ab])"')


def puzzle1() -> None:
    entries = [i for i in DATA.split("\n")]

    def process_rule(raw_rule):
        raw = raw_value.match(raw_rule)
        if raw:
            return raw.group(1)
        raw_rule = " {} ".format(raw_rule)
        if " | " in raw_rule:
            raw_rule = "({})".format(raw_rule)
        raw_rule = raw_rule.replace(" ", "  ")
        return raw_rule

    rules = {
        key: process_rule(value)
        for key, value in map(lambda x: x.split(": "), entries[0 : entries.index("")])
    }
    messages = entries[len(rules) + 1 : entries.index("", len(rules) + 1)]

    processed = set()
    rest = set()
    find_rules = re.compile(r"( (\d+) )")
    for key, value in rules.items():
        (processed if not find_rules.search(value) else rest).add(key)

    print("processed", processed)
    while rest:
        for rest_index in rest:
            rule = rules[rest_index]
            sub_rules = find_rules.findall(rule)
            if not sub_rules:
                continue
            if not all(s[1] in processed for s in sub_rules):
                continue

            print("{}: {}".format(rest_index, rules[rest_index]))
            for sub_rule, sub_index in sub_rules:
                target_sub_rule = rules[sub_index]
                print(" {} -> {}".format(sub_index, target_sub_rule))
                rule = rule.replace(sub_rule, target_sub_rule)

            print("{} => {}".format(rules[rest_index], rule))
            rules[rest_index] = rule
            processed.add(rest_index)

        rest = rest - processed

    final_rule = "^{}$".format(rules["0"].replace(" ", ""))
    print("final rule:", final_rule)
    match = re.compile(final_rule)
    result = sum(1 if match.match(m) else 0 for m in messages)
    print(result)


def puzzle2() -> None:
    entries = [i for i in DATA.split("\n")]

    def process_rule(raw_rule):
        raw = raw_value.match(raw_rule)
        if raw:
            return raw.group(1)
        raw_rule = " {} ".format(raw_rule)
        if " | " in raw_rule:
            raw_rule = "({})".format(raw_rule)
        raw_rule = raw_rule.replace(" ", "  ")
        return raw_rule

    rules = {
        key: process_rule(value)
        for key, value in map(
            lambda x: x.split(": ", 1),
            (
                entries[0 : entries.index("")]
                + [
                    # it's dirty
                    "8: 42 + ",
                    # it's even dirtier
                    "11: 42 (?: 42 (?: 42 (?: 42 31 )? 31 )? 31 )? 31",
                ]
            ),
        )
    }
    messages = entries[len(rules) + 1 : entries.index("", len(rules) + 1)]

    processed = set()
    rest = set()
    excluded = set()
    find_rules = re.compile(r"( (\d+) )")
    for key, value in rules.items():
        (processed if not find_rules.search(value) else rest).add(key)

    print("processed", processed)
    while rest - excluded:
        for rest_index in sorted(rest - excluded):
            rule = rules[rest_index]
            sub_rules = find_rules.findall(rule)
            if not sub_rules:
                continue
            sub_indexes = [s[1] for s in sub_rules]
            if rest_index in set(sub_indexes):
                excluded.add(rest_index)
                continue

            print("{}: {}".format(rest_index, rules[rest_index]))
            for sub_rule, sub_index in sub_rules:
                if sub_index in excluded:
                    continue
                target_sub_rule = rules[sub_index]
                print(" {} -> {}".format(sub_index, target_sub_rule))
                rule = rule.replace(sub_rule, target_sub_rule)

            print("{} => {}".format(rules[rest_index], rule))
            rules[rest_index] = rule
            if not (set(map(itemgetter(1), find_rules.findall(rule))) - excluded):
                processed.add(rest_index)

        rest = rest - processed

    final_rule = "^{}$".format(rules["0"].replace(" ", ""))
    print("final rule", final_rule)
    match = re.compile(final_rule)
    result = sum(1 if match.match(m) else 0 for m in messages)
    print(result)


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
