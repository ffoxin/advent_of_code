DATA = 348


def puzzle1():
    step = DATA

    array = [0]
    current = 0
    for i in range(1, 2018):
        current = (current + step) % len(array)
        current += 1
        array.insert(current, i)
    print(array[current + 1])


def puzzle2():
    step = DATA

    current = 0
    array_len = 1
    zero_index = 0
    zero_next = None
    for i in range(1, 50000000):
        current = (current + step) % array_len
        array_len += 1
        if current == zero_index:
            zero_next = i
        elif current < zero_index:
            zero_index += 1
        current += 1
    print(zero_next)
