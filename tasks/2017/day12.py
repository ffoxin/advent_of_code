from main import data_path

DATA = data_path(__file__)


def puzzle1():
    with open(DATA, 'r') as f:
        lines = f.readlines()

    lines1 = [
        '0 <-> 2',
        '1 <-> 1',
        '2 <-> 0, 3, 4',
        '3 <-> 2, 4',
        '4 <-> 2, 3, 6',
        '5 <-> 6',
        '6 <-> 4, 5',
    ]

    array = list(range(len(lines)))

    for line in lines:
        program, pipes = line.split(' <-> ')
        program = int(program)
        pipes = list(map(int, pipes.split(', ')))

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


def puzzle2():
    with open(DATA, 'r') as f:
        lines = f.readlines()

    lines1 = [
        '0 <-> 2',
        '1 <-> 1',
        '2 <-> 0, 3, 4',
        '3 <-> 2, 4',
        '4 <-> 2, 3, 6',
        '5 <-> 6',
        '6 <-> 4, 5',
    ]

    array = list(range(len(lines)))

    for line in lines:
        program, pipes = line.split(' <-> ')
        program = int(program)
        pipes = list(map(int, pipes.split(', ')))

        for pipe in pipes:
            s = {program, pipe, array[program], array[pipe]}
            min_pipe = min(s)
            array[program] = min_pipe
            array[pipe] = min_pipe

            for i in range(len(array)):
                if array[i] in s:
                    array[i] = min_pipe

    print(len(set(array)))
