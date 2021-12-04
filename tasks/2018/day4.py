from collections import defaultdict
from datetime import datetime
from enum import Enum, unique, auto
from operator import attrgetter, itemgetter

from main import data_path

DATA = data_path(__file__)


@unique
class ActionType(Enum):
    Begin = auto()
    Sleep = auto()
    Wake = auto()


class Record:
    def __init__(self, line):
        timestamp, action = line.split("] ")

        self.timestamp = datetime.strptime(timestamp, "[%Y-%m-%d %H:%M")

        action = action.split(" ")
        if action[0] == "falls":
            self.action = ActionType.Sleep
            self.id = None
        elif action[0] == "wakes":
            self.action = ActionType.Wake
            self.id = None
        elif action[0] == "Guard":
            self.action = ActionType.Begin
            self.id = int(action[1][1:])
        else:
            raise RuntimeError("Unexpected action: {}".format(line))

    def __str__(self):
        return f"<Record {self.timestamp} {self.id} {self.action}>"


def puzzle1():
    with open(DATA, "r") as f:
        lines = f.readlines()

    lines = map(str.strip, lines)

    lines = [Record(line) for line in lines]
    lines = sorted(lines, key=attrgetter("timestamp"))

    guards = defaultdict(lambda: defaultdict(int))
    current = None
    action = None
    timestamp = None
    for line in lines:
        if line.action == ActionType.Begin:
            if action == ActionType.Sleep:
                raise RuntimeError("Hey, he slept before me! {}".format(line))
            current = line.id
            action = ActionType.Wake
        elif line.action == ActionType.Sleep:
            action = line.action
        elif line.action == ActionType.Wake:
            if action == ActionType.Sleep:
                for i in range(timestamp.minute, line.timestamp.minute):
                    guards[current][i] += 1
            action = line.action

        timestamp = line.timestamp

    max_id = 0
    max_sleep = 0
    for guard, data in guards.items():
        slept = sum(data.values())
        if slept > max_sleep:
            max_sleep = slept
            max_id = guard
    most_minute = max(guards[max_id].items(), key=itemgetter(1))[0]
    print(most_minute * max_id)


def puzzle2():
    with open(DATA, "r") as f:
        lines = f.readlines()

    lines = map(str.strip, lines)

    lines = [Record(line) for line in lines]
    lines = sorted(lines, key=attrgetter("timestamp"))

    guards = defaultdict(lambda: defaultdict(int))
    current = None
    action = None
    timestamp = None
    for line in lines:
        if line.action == ActionType.Begin:
            if action == ActionType.Sleep:
                raise RuntimeError("Hey, he slept before me! {}".format(line))
            current = line.id
            action = ActionType.Wake
        elif line.action == ActionType.Sleep:
            action = line.action
        elif line.action == ActionType.Wake:
            if action == ActionType.Sleep:
                for i in range(timestamp.minute, line.timestamp.minute):
                    guards[current][i] += 1
            action = line.action

        timestamp = line.timestamp

    max_id = 0
    max_minute = 0
    max_sleep = 0
    for guard, data in guards.items():
        max_guard = max(data.values())
        if max_guard > max_sleep:
            for minute, slept in data.items():
                if slept == max_guard:
                    max_minute = minute
                    break
            max_sleep = max_guard
            max_id = guard

    print(max_id * max_minute)
