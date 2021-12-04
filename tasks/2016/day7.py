def has_pattern(line):
    for i in range(len(line) - 3):
        sub = line[i : i + 4]
        if sub[0] == sub[3] and sub[1] == sub[2] and sub[0] != sub[1]:
            return True


def get_bab_patterns(part):
    ssls = []
    for i in range(len(part) - 2):
        sub = part[i : i + 3]
        if sub[0] == sub[2] and sub[0] != sub[1]:
            ssls.append(sub[1] + sub[0] + sub[1])
    return ssls


def is_support_ssl(part, ssls):
    return any(map(part.count, ssls))


def puzzle1():
    data = "tasks/data/day7.txt"

    count = 0
    with open(data, "r") as f:
        for line in f.readlines():
            line = line.strip()
            line = line.replace("[", "]")
            parts = line.split("]")

            is_valid = True
            if any(map(has_pattern, parts[1::2])):
                is_valid = False
            if is_valid:
                if any(map(has_pattern, parts[::2])):
                    count += 1

    print(count)


def puzzle2():
    data = "tasks/data/day7.txt"

    count = 0
    with open(data, "r") as f:
        for line in f.readlines():
            line = line.strip()
            line = line.replace("[", "]")
            parts = line.split("]")

            ssls = []
            for part in parts[::2]:
                ssls.extend(get_bab_patterns(part))
            ssls
            for part in parts[1::2]:
                if is_support_ssl(part, ssls):
                    count += 1
                    break

    print(count)
