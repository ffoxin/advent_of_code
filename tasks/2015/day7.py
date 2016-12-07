import re


class Signals:
    pattern_value = re.compile('([a-z]+|\d+) -> ([a-z]+)')
    pattern_not = re.compile('NOT ([a-z]+) -> ([a-z]+)')
    pattern_and = re.compile('([a-z]+|\d+) AND ([a-z]+) -> ([a-z]+)')
    pattern_or = re.compile('([a-z]+) OR ([a-z]+) -> ([a-z]+)')
    pattern_lshift = re.compile('([a-z]+) LSHIFT (\d+) -> ([a-z]+)')
    pattern_rshift = re.compile('([a-z]+) RSHIFT (\d+) -> ([a-z]+)')


def parse_lines(lines):
    prepared = {}
    processed = {}
    for line in lines:
        get_value = Signals.pattern_value.match(line)
        if get_value:
            source, target = get_value.groups()
            if source.isnumeric():
                processed[target] = int(source)
            else:
                prepared[target] = ('=', source)
            continue

        get_not = Signals.pattern_not.match(line)
        if get_not:
            source, target = get_not.groups()
            prepared[target] = ('~', source)
            continue

        get_and = Signals.pattern_and.match(line)
        if get_and:
            source1, source2, target = get_and.groups()
            prepared[target] = ('&', source1, source2)
            continue

        get_or = Signals.pattern_or.match(line)
        if get_or:
            source1, source2, target = get_or.groups()
            prepared[target] = ('|', source1, source2)
            continue

        get_lshift = Signals.pattern_lshift.match(line)
        if get_lshift:
            source1, source2, target = get_lshift.groups()
            prepared[target] = ('<<', source1, int(source2))
            continue

        get_rshift = Signals.pattern_rshift.match(line)
        if get_rshift:
            source1, source2, target = get_rshift.groups()
            prepared[target] = ('>>', source1, int(source2))
            continue

        assert False, 'Line not parsed: {}'.format(line)
    return prepared, processed


def wiring(prepared, processed):
    while prepared:
        for key, value in prepared.items():
            op = value[0]
            if op in ['~', '<<', '>>', '=']:
                source = value[1]
                if source in processed:
                    target = processed[source]
                    if op == '~':
                        target = ~target
                    elif op == '<<':
                        target <<= value[2]
                    elif op == '>>':
                        target >>= value[2]
                    elif op == '=':
                        pass
                    else:
                        assert False, 'Operator not handled: {}'.format(op)

                    processed[key] = target
                    del prepared[key]
                    break
            else:
                source1, source2 = value[1:]
                source1 = int(source1) if source1.isnumeric() else processed.get(source1)
                source2 = int(source2) if source2.isnumeric() else processed.get(source2)
                if source1 is not None and source2 is not None:
                    target = source1
                    if op == '&':
                        target &= source2
                    elif op == '|':
                        target |= source2
                    else:
                        assert False, 'Invalid operator: {}'.format(op)

                    processed[key] = target
                    del prepared[key]
                    break


def puzzle1():
    data = 'tasks/2015/data/day7.txt'

    with open(data, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        prepared, processed = parse_lines(lines)

    wiring(prepared, processed)

    print(processed.get('a'))


def puzzle2():
    data = 'tasks/2015/data/day7.txt'

    with open(data, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        prepared, processed = parse_lines(lines)

    processed['b'] = 3176

    wiring(prepared, processed)

    print(processed.get('a'))
