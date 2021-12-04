import re
from pathlib import Path

DATA = (Path(__file__).parent / "data" / "day4.txt").read_text()


def puzzle1():
    entries = [i for i in DATA.split("\n")]
    required = frozenset(
        [
            "byr",
            "iyr",
            "eyr",
            "hgt",
            "hcl",
            "ecl",
            "pid",
        ]
    )  # 'cid' - optional
    passport_fields = set()
    valid_count = 0

    for entry in entries:
        if entry == "":
            if passport_fields and passport_fields.issuperset(required):
                valid_count += 1
            passport_fields = set()
            continue

        keys = [i.split(":")[0] for i in entry.split(" ") if i]
        passport_fields.update(keys)

    print(valid_count)


def puzzle2():
    entries = [i for i in DATA.split("\n")]
    required = frozenset(
        [
            "byr",
            "iyr",
            "eyr",
            "hgt",
            "hcl",
            "ecl",
            "pid",
        ]
    )  # 'cid' - optional
    passport_data = {}
    valid_count = 0
    color_match = re.compile("#[0-9a-f]{6}")

    for entry in entries:
        if entry == "":
            if passport_data and required.issubset(passport_data):
                is_valid = True
                byr: str = passport_data["byr"]
                if not (byr.isdigit() and 1920 <= int(byr) <= 2002):
                    is_valid = False
                iyr: str = passport_data["iyr"]
                if not (iyr.isdigit() and 2010 <= int(iyr) <= 2020):
                    is_valid = False
                eyr: str = passport_data["eyr"]
                if not (eyr.isdigit() and 2020 <= int(eyr) <= 2030):
                    is_valid = False
                hgt: str = passport_data["hgt"]
                if not hgt[-2:] in ("cm", "in"):
                    is_valid = False
                if hgt.endswith("cm") and not (
                    hgt[:-2].isdigit() and 150 <= int(hgt[:-2]) <= 193
                ):
                    is_valid = False
                if hgt.endswith("in") and not (
                    hgt[:-2].isdigit() and 59 <= int(hgt[:-2]) <= 76
                ):
                    is_valid = False
                hcl: str = passport_data["hcl"]
                if not color_match.match(hcl):
                    is_valid = False
                ecl: str = passport_data["ecl"]
                if ecl not in "amb blu brn gry grn hzl oth".split(" "):
                    is_valid = False
                pid: str = passport_data["pid"]
                if not (pid.isdigit() and len(pid) == 9):
                    is_valid = False

                if is_valid:
                    valid_count += 1
            passport_data = {}
            continue

        passport_data.update(dict(i.split(":") for i in entry.split(" ") if i))

    print(valid_count)


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
