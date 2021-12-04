def puzzle1():
    data = "tasks/2015/data/day2.txt"

    areas = 0
    with open(data, "r") as f:
        for line in f.readlines():
            dims = [int(i) for i in line.split("x")]
            area = [dims[i] * dims[(i + 1) % 3] for i in range(3)]
            areas += sum(area) * 2 + min(area)
    print(areas)


def puzzle2():
    data = "tasks/2015/data/day2.txt"

    length = 0
    with open(data, "r") as f:
        for line in f.readlines():
            dims = [int(i) for i in line.split("x")]
            bow = 1
            for dim in dims:
                bow *= dim
            max_pos = dims.index(max(dims))
            dims = dims[:max_pos] + dims[max_pos + 1 :]
            length += bow + sum(dims) * 2
    print(length)
