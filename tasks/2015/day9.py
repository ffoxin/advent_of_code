import re


def parse_towns(lines):
    pattern = re.compile("(\w+) to (\w+) = (\d+)")
    towns = {}
    for line in lines:
        line = line.strip()
        town_from, town_to, distance = pattern.match(line).groups()
        if town_from not in towns:
            towns[town_from] = {}
        if town_to not in towns:
            towns[town_to] = {}
        if town_to in towns[town_from] or town_from in towns[town_to]:
            assert False, "Path {} - {} already added".format(town_to, town_from)
        towns[town_from][town_to] = int(distance)
        towns[town_to][town_from] = int(distance)
    return towns


def get_solution(solution, towns):
    if len(solution) < len(towns):
        for town in towns:
            if town not in solution:
                if len(solution) != 0 and town not in towns[solution[-1]]:
                    continue
                for s in get_solution(solution + [town], towns):
                    yield s
    else:
        yield solution


def puzzle1():
    data = "tasks/2015/data/day9.txt"

    with open(data, "r") as f:
        lines = f.readlines()

    towns = parse_towns(lines)
    min_distance = None
    for solution in get_solution([], towns):
        distance = 0
        for i in range(len(solution) - 1):
            town_from = solution[i]
            town_to = solution[i + 1]
            distance += towns[town_from][town_to]
        min_distance = distance if min_distance is None else min(min_distance, distance)

    print(min_distance)


def puzzle2():
    data = "tasks/2015/data/day9.txt"

    with open(data, "r") as f:
        lines = f.readlines()

    towns = parse_towns(lines)
    max_distance = None
    for solution in get_solution([], towns):
        distance = 0
        for i in range(len(solution) - 1):
            town_from = solution[i]
            town_to = solution[i + 1]
            distance += towns[town_from][town_to]
        max_distance = distance if max_distance is None else max(max_distance, distance)

    print(max_distance)
