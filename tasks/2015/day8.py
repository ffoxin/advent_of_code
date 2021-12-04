def char_len(s):
    assert s[0] == '"', "Unexpected first string char"
    assert s[-1] == '"', "Unexpected last string char"

    s = s[1:-1]

    str_length = len(s)
    length = 0
    index = 0
    while index < str_length:
        if s[index] == "\\":
            index += 1
            if s[index] == "x":
                index += 2
        index += 1
        length += 1
    return length


def char_len2(s):
    assert s[0] == '"', "Unexpected first string char"
    assert s[-1] == '"', "Unexpected last string char"

    length = len(s)
    length += 2  # initial and trailing quotes
    length += s.count('"') + s.count("\\")

    return length


def puzzle1():
    data = "tasks/2015/data/day8.txt"

    total = 0
    with open(data, "r") as f:
        for line in f.readlines():
            line = line.strip()
            total += len(line)
            total -= char_len(line)
    print(total)


def puzzle2():
    data = "tasks/2015/data/day8.txt"

    total = 0
    with open(data, "r") as f:
        for line in f.readlines():
            line = line.strip()
            total += char_len2(line)
            total -= len(line)
    print(total)
