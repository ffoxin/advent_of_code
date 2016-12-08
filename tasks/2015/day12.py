import json


def json_sum(data):
    result = 0
    if isinstance(data, dict):
        for value in data.values():
            result += json_sum(value)
    elif isinstance(data, list):
        for value in data:
            result += json_sum(value)
    elif isinstance(data, int):
        result = data

    return result


def json_sum_non_red(data):
    result = 0
    if isinstance(data, dict) and 'red' not in data.values():
        for value in data.values():
            result += json_sum_non_red(value)
    elif isinstance(data, list):
        for value in data:
            result += json_sum_non_red(value)
    elif isinstance(data, int):
        result = data

    return result


def puzzle1():
    data = 'tasks/2015/data/day12.txt'

    with open(data, 'r') as f:
        data = f.read()

    parsed = json.loads(data)
    print(json_sum(parsed))


def puzzle2():
    data = 'tasks/2015/data/day12.txt'

    with open(data, 'r') as f:
        data = f.read()

    parsed = json.loads(data)
    print(json_sum_non_red(parsed))

