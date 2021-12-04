from collections import defaultdict
from pathlib import Path

from tabulate import tabulate

DATA = (Path(__file__).parent / "data" / "day21.txt").read_text()


def puzzle1():
    entries = [i for i in DATA.split("\n") if i]

    recipes = []
    for entry in entries:
        ingred_raw, allerg_raw = entry.split(" (")
        ingred = ingred_raw.split(" ")
        allerg = allerg_raw[
            allerg_raw.find("contains") + len("contains") + 1 : -1
        ].split(", ")
        recipes.append((ingred, allerg))
        print(ingred, allerg)

    consist = defaultdict(set)
    for ingred, allerg in recipes:
        for item in allerg:
            if item not in consist:
                consist[item].update(ingred)
            else:
                consist[item].intersection_update(ingred)
                # consist[item].update(ingred)

    processed = set()
    while True:
        # updated = False
        new_processed = set()
        for item, value in consist.items():
            if len(value) == 1:
                product = list(value)[0]
                if product not in processed:
                    new_processed.add(product)
        if new_processed:
            for item, value in consist.items():
                if len(value) > 1:
                    value.difference_update(new_processed)
            processed.update(new_processed)
        else:
            break

    print(
        tabulate(
            [
                (item, len(value), ", ".join(sorted(value)))
                for item, value in consist.items()
            ],
            headers=["allerg", "len", "igreds"],
            tablefmt="psql",
        )
    )

    defined = set(list(value)[0] for key, value in consist.items() if len(value) == 1)
    print(defined)

    count = 0
    for ingred, _ in recipes:
        for item in ingred:
            if item not in defined:
                count += 1
    print(count)

    return consist


def puzzle2():
    consist = puzzle1()

    result = [
        list(consist[allerg])[0]
        for allerg in sorted(consist)
        if len(consist[allerg]) == 1
    ]

    print(",".join(result))


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
