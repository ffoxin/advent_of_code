class Triangle:
    def __init__(self, values):
        self._values = [int(value) for value in values]

    def is_possible(self):
        for i in range(3):
            if (
                self._values[i % 3] + self._values[(i + 1) % 3]
                <= self._values[(i + 2) % 3]
            ):
                return False
        return True


def puzzle1():
    data = "tasks/data/day3.txt"

    possible_count = 0
    with open(data, "r") as f:
        for line in f.readlines():
            triangle = Triangle(line.split())
            if triangle.is_possible():
                possible_count += 1

    print(possible_count)


def puzzle2():
    data = "tasks/data/day3.txt"

    possible_count = 0
    with open(data, "r") as f:
        values = []
        for line in f.readlines():
            values += line.split()
            if len(values) == 3 * 3:
                for i in range(3):
                    triangle = Triangle(values[i::3])
                    if triangle.is_possible():
                        possible_count += 1
                values = []

    print(possible_count)
