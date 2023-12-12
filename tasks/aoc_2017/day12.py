from main import data_path

DATA = data_path(__file__)


def puzzle1() -> None:
    with open(DATA, "r") as f:
        lines = f.readlines()

    array = list(range(len(lines)))

    for line in lines:
        program, pipes = line.split(" <-> ")
        program = int(program)
        pipes = list(map(int, pipes.split(", ")))

        for pipe in pipes:
            s = {program, pipe, array[program], array[pipe]}
            min_pipe = min(s)
            array[program] = min_pipe
            array[pipe] = min_pipe

            for i in range(len(array)):
                if array[i] in s:
                    array[i] = min_pipe

    result = sum(val == 0 for val in array)

    print(result)


def puzzle2() -> None:
    with open(DATA, "r") as f:
        lines = f.readlines()

    array = list(range(len(lines)))

    for line in lines:
        program, pipes = line.split(" <-> ")
        program = int(program)
        pipes = list(map(int, pipes.split(", ")))

        for pipe in pipes:
            s = {program, pipe, array[program], array[pipe]}
            min_pipe = min(s)
            array[program] = min_pipe
            array[pipe] = min_pipe

            for i in range(len(array)):
                if array[i] in s:
                    array[i] = min_pipe

    print(len(set(array)))
