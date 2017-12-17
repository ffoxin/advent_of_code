from enum import Enum, unique

from main import data_path

DATA = data_path(__file__)


@unique
class Status(Enum):
    GROUP = 1
    GARB = 2
    SKIP = 3


def puzzle1():
    with open(DATA, 'r') as f:
        lines = f.readlines()

    line = lines[0].strip()

    level = 0
    score = 0
    status = [Status.GROUP]
    for ch in line:
        if status[-1] == Status.GROUP:
            if ch == '{':
                level += 1
            elif ch == '}':
                score += level
                level -= 1
            elif ch == '!':
                status.append(Status.SKIP)
            elif ch == '<':
                status.append(Status.GARB)
            else:
                RuntimeError(f'Transition from {status[-1].name} with "{ch}"')
        elif status[-1] == Status.SKIP:
            status.pop()
        elif status[-1] == Status.GARB:
            if ch == '>':
                status.pop()
            elif ch == '!':
                status.append(Status.SKIP)

    print(score)


def puzzle2():
    with open(DATA, 'r') as f:
        lines = f.readlines()

    line = lines[0].strip()

    level = 0
    result = 0
    status = [Status.GROUP]
    for ch in line:
        if status[-1] == Status.GROUP:
            if ch == '{':
                level += 1
            elif ch == '}':
                level -= 1
            elif ch == '!':
                status.append(Status.SKIP)
            elif ch == '<':
                status.append(Status.GARB)
            else:
                RuntimeError(f'Transition from {status[-1].name} with "{ch}"')
        elif status[-1] == Status.SKIP:
            status.pop()
        elif status[-1] == Status.GARB:
            if ch == '>':
                status.pop()
            elif ch == '!':
                status.append(Status.SKIP)
            else:
                result += 1

    print(result)
