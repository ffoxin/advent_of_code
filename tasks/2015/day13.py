import re


def parse_guests(lines):
    pattern = re.compile('(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)\.')
    guests = {}
    for line in lines:
        line = line.strip()
        parsed = pattern.match(line)
        assert parsed, 'Line not parsed: {}'.format(line)
        source, action, value, target = parsed.groups()
        if source not in guests:
            guests[source] = {}
        if target in guests[source]:
            assert False, 'Path {} - {} already added'.format(source, target)
        assert action in ['gain', 'lose'], 'Invalid action: {}'.format(action)

        guests[source][target] = int(value) * (-1 if action == 'lose' else 1)

    return guests


def get_solution(solution, guests):
    if len(solution) < len(guests):
        for guest in guests:
            if guest not in solution:
                for s in get_solution(solution + [guest], guests):
                    yield s
    else:
        yield solution


def puzzle1():
    data = 'tasks/2015/data/day13.txt'

    with open(data, 'r') as f:
        lines = f.readlines()

    guests = parse_guests(lines)
    guests_count = len(guests)

    max_happiness = None
    for solution in get_solution([], guests):
        happiness = 0
        for i in range(guests_count):
            source = solution[i]
            target = solution[(i + 1) % guests_count]
            happiness += guests[source][target] + guests[target][source]
        max_happiness = happiness if max_happiness is None else max(max_happiness, happiness)

    print(max_happiness)


def puzzle2():
    data = 'tasks/2015/data/day13.txt'

    with open(data, 'r') as f:
        lines = f.readlines()

    guests = parse_guests(lines)
    me = {}
    for key in guests:
        guests[key]['me'] = 0
        me[key] = 0
    guests['me'] = me
    guests_count = len(guests)

    max_happiness = None
    for solution in get_solution([], guests):
        happiness = 0
        for i in range(guests_count):
            source = solution[i]
            target = solution[(i + 1) % guests_count]
            happiness += guests[source][target] + guests[target][source]
        max_happiness = happiness if max_happiness is None else max(max_happiness, happiness)

    print(max_happiness)
