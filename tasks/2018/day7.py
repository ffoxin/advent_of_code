from main import data_path

DATA = data_path(__file__)


class Requirement:
    def __init__(self, line):
        parts = line.split(' ')
        self.start = parts[1]
        self.end = parts[-3]

    def __repr__(self):
        return f'{self.start} -> {self.end}'


def find_next(requirements):
    while requirements:
        starts = set(r.start for r in requirements)
        ends = set(r.end for r in requirements)

        can_start = starts - ends
        result = sorted(can_start)[0]
        requirements = set(r for r in requirements if r.start != result)

        yield result
        if not requirements:
            for i in sorted(ends):
                yield i


def puzzle1():
    with open(DATA, 'r') as f:
        lines = f.readlines()

    requirements = set(map(Requirement, lines))

    print(''.join(i for i in find_next(requirements)))
    print(requirements)


def puzzle2():
    with open(DATA, 'r') as f:
        lines = f.readlines()

    requirements = set(map(Requirement, lines))

    num_workers = 5
    workers = [list() for _ in range(num_workers)]
    second = 0
    in_progress = set()
    result = []
    todo = set(r.start for r in requirements) | set(r.end for r in requirements)
    while True:
        for i in range(len(workers)):
            if workers[i] and len(workers[i]) <= second:
                requirements = set(r for r in requirements if r.start != workers[i][-1])
                in_progress.discard(workers[i][-1])
                todo.discard(workers[i][-1])

        for i in range(len(workers)):
            if len(workers[i]) <= second:
                if requirements:
                    starts = set(r.start for r in requirements) - in_progress
                    ends = set(r.end for r in requirements)
                    to_start = list(sorted(starts - ends))
                else:
                    to_start = list(sorted(todo - in_progress))

                if to_start:
                    to_start = to_start[0]
                    workers[i].extend([' '] * (second - len(workers[i])))
                    workers[i].extend([to_start] * (ord(to_start) - ord('A') + 61))
                    in_progress.add(to_start)
                    result.append(to_start)

        print(second)
        for i in range(num_workers):
            print(' ', workers[i])

        if not todo:
            break
        else:
            second += 1

    print(second)
