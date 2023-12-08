from main import data_path

DATA = data_path(__file__)


class Link:
    def __init__(self, value):
        self.center, self.planet = value.split(")")


def puzzle1():
    with open(DATA) as f:
        lines = list(map(str.strip, f.readlines()))

    orbits = {}
    for line in lines:
        a, b = line.split(")")
        orbits[b] = a

    total = 0
    for key, value in orbits.items():
        count = 1
        while value != "COM":
            count += 1
            value = orbits[value]
        # print(key, count)
        total += count

    print(total)


def puzzle2():
    with open(DATA) as f:
        lines = list(map(str.strip, f.readlines()))

    orbits = {}
    for line in lines:
        a, b = line.split(")")
        orbits[b] = a

    def find_way(planet):
        way = []
        while planet != "COM":
            next_planet = orbits[planet]
            way.append(next_planet)
            planet = next_planet
        return way

    you = find_way("YOU")
    san = find_way("SAN")

    # print(len(you), you)
    # print(len(san), san)

    index = -1
    while you[index] == san[index]:
        index -= 1

    # print(index)
    total = len(you) + len(san) + 2 * index + 2
    print(total)
