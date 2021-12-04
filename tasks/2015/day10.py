def look_and_say(value):
    length = len(value)
    pos = 0
    result = ""
    while pos < length:
        index = 0
        current = value[pos + index]
        while pos + index < length and current == value[pos + index]:
            index += 1
        result += "{}{}".format(index, current)
        pos += index
    return result


def puzzle1():
    value = "1113222113"

    for i in range(40):
        value = look_and_say(value)

    print(len(value))


def puzzle2():
    value = "1113222113"

    for i in range(50):
        value = look_and_say(value)

    print(len(value))
