from main import data_path

DATA = data_path(__file__)


def puzzle1():
    with open(DATA, 'r') as f:
        modules = list(map(int, f.readlines()))

    def calc_fuel(mass):
        return mass // 3 - 2

    assert calc_fuel(12) == 2
    assert calc_fuel(14) == 2
    assert calc_fuel(1969) == 654
    assert calc_fuel(100756) == 33583

    result = sum(map(calc_fuel, modules))

    print(result)


def puzzle2():
    with open(DATA, 'r') as f:
        modules = list(map(int, f.readlines()))

    def calc_single_fuel(mass):
        return mass // 3 - 2

    def calc_full_fuel(mass):
        while True:
            mass = calc_single_fuel(mass)
            if mass > 0:
                yield mass
            else:
                break

    def calc_fuel(mass):
        return sum(calc_full_fuel(mass))

    assert calc_fuel(12) == 2
    assert calc_fuel(1969) == 966
    assert calc_fuel(100756) == 50346

    result = sum(map(calc_fuel, modules))

    print(result)
